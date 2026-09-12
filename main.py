#!/usr/bin/env python3
"""Marmara Üniversitesi duyuru takip ve WhatsApp bildirim botu.

Akış:
1) Duyuru sayfasını (https://www.marmara.edu.tr/allnotices) çeker.
2) `duyurular.json` içindeki daha önce görülmüş duyurularla karşılaştırır.
3) Yeni duyuruları WhatsApp Cloud API üzerinden gönderir.
4) `duyurular.json`'u güncel duyuru listesiyle günceller.

Git commit/push işlemi bilerek burada değil, GitHub Actions workflow'unda
yapılıyor (bkz. .github/workflows/main.yml) — script'in tek sorumluluğu
veri çekmek ve bildirim göndermek.
"""

import json
import logging
import os
import random
import sys
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.marmara.edu.tr"
NOTICES_URL = f"{BASE_URL}/allnotices"
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "duyurular.json")

# GitHub Actions cron'u zaten 09:00 TR civarında tetikliyor; script ek olarak
# 0-1200 saniye (0-20 dk) rastgele bekleyerek her gün farklı bir saatte
# kontrol yapılmasını sağlıyor (bkz. proje talimatı madde 2.2).
MAX_RANDOM_DELAY_SECONDS = 1200

WA_API_VERSION = os.environ.get("WA_API_VERSION", "v21.0")
WA_TOKEN = os.environ.get("WA_TOKEN")
WA_PHONE_NUMBER_ID = os.environ.get("WA_PHONE_NUMBER_ID")
TARGET_PHONE_NUMBER = os.environ.get("TARGET_PHONE_NUMBER")

# Yerel testte (`SKIP_RANDOM_DELAY=1 python main.py`) rastgele beklemeyi atlamak için.
SKIP_RANDOM_DELAY = os.environ.get("SKIP_RANDOM_DELAY") == "1"

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


def fetch_notices():
    """Duyuru sayfasını kazır ve [{baslik, tarih, link}] listesi döner."""
    headers = {
        # Bazı okul sunucuları tarayıcı User-Agent'ı olmayan istekleri engelliyor.
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(NOTICES_URL, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.RequestException as exc:
        logger.error("Duyuru sayfası çekilemedi: %s", exc)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    container = soup.select_one("div.blog-pull-right")
    if container is None:
        logger.error("Duyuru listesi konteyneri bulunamadı; site yapısı değişmiş olabilir.")
        return []

    notices = []
    for row in container.select("div.row.mb-15"):
        title_tag = row.select_one("h4")
        date_tag = row.select_one("h6")
        link_tag = row.select_one("a[href]")

        if title_tag is None or link_tag is None:
            continue

        title = title_tag.get_text(strip=True)
        date = date_tag.get_text(strip=True) if date_tag else ""
        link = urljoin(BASE_URL, link_tag["href"])

        notices.append({"baslik": title, "tarih": date, "link": link})

    logger.info("Sayfadan %d duyuru bulundu.", len(notices))
    return notices


def load_known_notices():
    """duyurular.json içindeki daha önce görülmüş duyuruları yükler."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        logger.error("duyurular.json okunamadı, boş liste ile devam ediliyor: %s", exc)
        return []


def save_notices(notices):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(notices, f, ensure_ascii=False, indent=2)
        logger.info("duyurular.json güncellendi (%d duyuru).", len(notices))
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

    current_notices = fetch_notices()
    if not current_notices:
        logger.warning("Hiç duyuru çekilemedi, işlem sonlandırılıyor.")
        sys.exit(0)

    known_notices = load_known_notices()
    known_links = {n["link"] for n in known_notices}

    # duyurular.json ilk kez oluşturuluyorsa (repo'da hiç kayıt yoksa), mevcut
    # tüm duyuruları "yeni" sayıp toplu WhatsApp bildirimi göndermek yerine
    # sadece referans olarak kaydediyoruz. Bot ancak bundan sonraki çalıştırmalarda
    # gerçekten yeni çıkan duyuruları bildirir.
    is_first_run = not os.path.exists(DATA_FILE)
    if is_first_run:
        logger.info(
            "duyurular.json bulunamadı: ilk çalıştırma. Mevcut %d duyuru bildirim "
            "gönderilmeden referans olarak kaydedilecek.",
            len(current_notices),
        )
        save_notices(current_notices)
        return

    new_notices = [n for n in current_notices if n["link"] not in known_links]

    if not new_notices:
        logger.info("Yeni duyuru yok.")
        return

    logger.info("%d yeni duyuru bulundu.", len(new_notices))

    sent_notices = []
    for notice in new_notices:
        message = f"🚨 *Yeni Duyuru:* {notice['baslik']}\n🔗 {notice['link']}"
        try:
            if send_whatsapp_message(message):
                sent_notices.append(notice)
        except Exception as exc:  # Beklenmeyen bir hata tüm çalıştırmayı düşürmesin.
            logger.error("Duyuru gönderilirken beklenmeyen hata: %s", exc)

    # Sadece başarıyla gönderilenleri değil, sayfada görünen TÜM güncel duyuruları
    # kaydediyoruz; aksi halde gönderimi başarısız olan bir duyuru her çalıştırmada
    # tekrar tekrar denenip eski duyurular listeden düşebilir.
    save_notices(current_notices)

    if len(sent_notices) < len(new_notices):
        logger.warning(
            "%d yeni duyurudan sadece %d'i WhatsApp ile gönderilebildi.",
            len(new_notices),
            len(sent_notices),
        )


if __name__ == "__main__":
    main()
