#!/usr/bin/env python3
"""Marmara Üniversitesi duyuru takip ve WhatsApp bildirim botu.

Akış:
1) `sites.json`'daki (aktif) her sitenin duyuru sayfasını eşzamanlı çeker.
2) `duyurular.json`'daki (site başına ayrı) daha önce görülmüş duyurularla karşılaştırır.
3) Her site için gerçekten yeni olan duyuruları WhatsApp Cloud API ile gönderir.
4) `duyurular.json`'u güncel duyurularla günceller.

Yeni bir Marmara sitesi eklemek için tek yapman gereken `sites.json`'a bir
kayıt eklemek (host + notices_url) — main.py'de kod değişikliği gerekmez.
Kendi kopyanı çalıştırmak istiyorsan sadece GitHub Secrets'taki WhatsApp
bilgilerini ve istersen `sites.json`'daki `enabled` alanlarını ayarlaman yeterli.

Git commit/push işlemi bilerek burada değil, GitHub Actions workflow'unda
yapılıyor (bkz. .github/workflows/main.yml) — script'in tek sorumluluğu
veri çekmek ve bildirim göndermek.
"""

import concurrent.futures
import json
import logging
import os
import random
import sys
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SITES_FILE = os.path.join(PROJECT_DIR, "sites.json")
DATA_FILE = os.path.join(PROJECT_DIR, "duyurular.json")

# GitHub Actions cron'u zaten 09:00 TR civarında tetikliyor; script ek olarak
# 0-1200 saniye (0-20 dk) rastgele bekleyerek her gün farklı bir saatte
# kontrol yapılmasını sağlıyor (bkz. proje talimatı madde 2.2).
MAX_RANDOM_DELAY_SECONDS = 1200

# Tek seferde en fazla bu kadar site eşzamanlı çekilir — hem hızlı olsun hem de
# üniversite sunucularına makul bir yükten fazlası binmesin.
MAX_WORKERS = 8
REQUEST_TIMEOUT = (10, 20)  # (connect, read) saniye

# WhatsApp gönderimleri arasında Meta Cloud API'ye art arda çok hızlı istek
# atmamak için kibarca bekleme.
WHATSAPP_SEND_DELAY_SECONDS = 0.5

WA_API_VERSION = os.environ.get("WA_API_VERSION", "v21.0")
WA_TOKEN = os.environ.get("WA_TOKEN")
WA_PHONE_NUMBER_ID = os.environ.get("WA_PHONE_NUMBER_ID")
TARGET_PHONE_NUMBER = os.environ.get("TARGET_PHONE_NUMBER")

# Yerel testte (`SKIP_RANDOM_DELAY=1 python main.py`) rastgele beklemeyi atlamak için.
SKIP_RANDOM_DELAY = os.environ.get("SKIP_RANDOM_DELAY") == "1"

HEADERS = {
    # Bazı okul sunucuları tarayıcı User-Agent'ı olmayan istekleri engelliyor.
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    )
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("marmara-duyuru-bot")


def random_delay():
    """09:00-09:20 arası rastgele bir saatte kontrol edebilmek için bekler."""
    if SKIP_RANDOM_DELAY:
        logger.info("SKIP_RANDOM_DELAY=1: rastgele bekleme atlanıyor.")
        return
    delay = random.randint(0, MAX_RANDOM_DELAY_SECONDS)
    logger.info("Rastgele bekleme: %s saniye.", delay)
    time.sleep(delay)


def load_sites():
    """sites.json'dan aktif (enabled) siteleri yükler."""
    try:
        with open(SITES_FILE, "r", encoding="utf-8") as f:
            all_sites = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        logger.error("sites.json okunamadı: %s", exc)
        return []

    enabled = [s for s in all_sites if s.get("enabled", True)]
    logger.info("sites.json: %d/%d site aktif.", len(enabled), len(all_sites))
    return enabled


def fetch_site_notices(site):
    """Bir sitenin duyuru sayfasını kazır ve [{baslik, tarih, link}] listesi döner.

    Site erişilemezse veya beklenen HTML yapısı yoksa None döner (bu site bu
    çalıştırmada atlanır, diğer siteleri etkilemez).
    """
    host = site["host"]
    url = site["notices_url"]

    try:
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as exc:
        logger.warning("[%s] duyuru sayfası çekilemedi: %s", host, exc)
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    container = soup.select_one("div.blog-pull-right")
    if container is None:
        logger.warning("[%s] beklenen HTML yapısı bulunamadı (site teması değişmiş olabilir).", host)
        return None

    base = f"https://{host}"
    notices = []
    for row in container.select("div.row.mb-15"):
        title_tag = row.select_one("h4")
        date_tag = row.select_one("h6")
        link_tag = row.select_one("a[href]")

        if title_tag is None or link_tag is None:
            continue

        notices.append({
            "baslik": title_tag.get_text(strip=True),
            "tarih": date_tag.get_text(strip=True) if date_tag else "",
            "link": urljoin(base, link_tag["href"]),
        })

    return notices


def fetch_all_sites(sites):
    """Tüm aktif siteleri eşzamanlı çeker. {host: notices} döner (başarısız olanlar dahil değil)."""
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_site = {executor.submit(fetch_site_notices, s): s for s in sites}
        for future in concurrent.futures.as_completed(future_to_site):
            site = future_to_site[future]
            try:
                notices = future.result()
            except Exception as exc:  # Bir sitedeki beklenmeyen hata tüm taramayı düşürmesin.
                logger.error("[%s] beklenmeyen hata: %s", site["host"], exc)
                continue
            if notices is not None:
                results[site["host"]] = notices
                logger.info("[%s] %d duyuru bulundu.", site["host"], len(notices))
    return results


def load_known():
    """duyurular.json'daki site başına daha önce görülmüş duyuruları yükler. {host: [...]} döner."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        logger.error("duyurular.json okunamadı, boş veriyle devam ediliyor: %s", exc)
        return {}


def save_known(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info("duyurular.json güncellendi (%d site).", len(data))
    except OSError as exc:
        logger.error("duyurular.json yazılamadı: %s", exc)


def send_whatsapp_message(text):
    """Meta WhatsApp Cloud API ile TARGET_PHONE_NUMBER'a metin mesajı gönderir."""
    if not (WA_TOKEN and WA_PHONE_NUMBER_ID and TARGET_PHONE_NUMBER):
        logger.error(
            "WhatsApp ortam değişkenleri eksik (WA_TOKEN / WA_PHONE_NUMBER_ID / "
            "TARGET_PHONE_NUMBER). Mesaj gönderilemiyor."
        )
        return False

    url = f"https://graph.facebook.com/{WA_API_VERSION}/{WA_PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WA_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": TARGET_PHONE_NUMBER,
        "type": "text",
        "text": {"body": text, "preview_url": True},
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        logger.info("WhatsApp mesajı gönderildi.")
        return True
    except requests.RequestException as exc:
        detail = ""
        if getattr(exc, "response", None) is not None:
            detail = f" | Yanıt: {exc.response.text}"
        logger.error("WhatsApp mesajı gönderilemedi: %s%s", exc, detail)
        return False


def main():
    logger.info("Marmara Üniversitesi duyuru botu başlatıldı.")
    random_delay()

    sites = load_sites()
    if not sites:
        logger.error("sites.json'da aktif site bulunamadı, işlem sonlandırılıyor.")
        sys.exit(1)

    site_by_host = {s["host"]: s for s in sites}
    current_by_host = fetch_all_sites(sites)

    if not current_by_host:
        logger.warning("Hiçbir siteden duyuru çekilemedi, işlem sonlandırılıyor.")
        sys.exit(0)

    known_by_host = load_known()
    updated_known = dict(known_by_host)
    new_items = []  # [(site, notice)]

    for host, notices in current_by_host.items():
        site = site_by_host[host]

        # Bu host duyurular.json'da hiç yoksa (yeni deploy edilmiş bot ya da
        # sites.json'a yeni eklenmiş bir site), mevcut duyuruları "yeni" sayıp
        # toplu bildirim göndermek yerine sadece referans olarak kaydediyoruz.
        if host not in known_by_host:
            logger.info(
                "[%s] ilk kez görülüyor, bildirim gönderilmeden referans "
                "olarak kaydedilecek (%d duyuru).",
                host, len(notices),
            )
            updated_known[host] = notices
            continue

        known_links = {n["link"] for n in known_by_host[host]}
        site_new = [n for n in notices if n["link"] not in known_links]
        if site_new:
            logger.info("[%s] %d yeni duyuru bulundu.", host, len(site_new))
            new_items.extend((site, n) for n in site_new)

        updated_known[host] = notices

    if not new_items:
        logger.info("Toplamda yeni duyuru yok.")
    else:
        logger.info("Toplam %d yeni duyuru WhatsApp ile gönderilecek.", len(new_items))
        sent = 0
        for site, notice in new_items:
            message = f"🚨 *Yeni Duyuru [{site['name']}]:* {notice['baslik']}\n🔗 {notice['link']}"
            try:
                if send_whatsapp_message(message):
                    sent += 1
            except Exception as exc:  # Beklenmeyen bir hata tüm çalıştırmayı düşürmesin.
                logger.error("[%s] duyuru gönderilirken beklenmeyen hata: %s", site["host"], exc)
            time.sleep(WHATSAPP_SEND_DELAY_SECONDS)

        if sent < len(new_items):
            logger.warning("%d/%d yeni duyuru WhatsApp ile gönderilebildi.", sent, len(new_items))

    save_known(updated_known)


if __name__ == "__main__":
    main()
