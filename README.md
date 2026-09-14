# Marmara Üniversitesi Duyuru Takip ve Telegram Bildirim Botu

Her gün Türkiye saatiyle 09:00-09:20 arasında, `sites.json`'da listelenen **97
Marmara Üniversitesi sitesinin** (tüm fakülteler, enstitüler, MYO'lar, daire
başkanlıkları, koordinatörlükler — bkz. `site_scan_report.md`) duyuru
sayfalarını eşzamanlı kontrol eder, önceden görülmemiş duyuruları Telegram
üzerinden bildirir. Tamamen GitHub Actions üzerinde, sunucusuz çalışır.

**Şablon/çoğaltılabilir tasarım:** Bu repo tek bir kişiye özel değil — Marmara'da
herkes bu repoyu fork'layıp sadece kendi Telegram botunu ve (isterse) hangi
sitelerin izleneceğini ayarlayarak kendi botunu çalıştırabilir. `main.py`'de
kod değişikliği gerekmez.

## Dosyalar

| Dosya | Görev |
|---|---|
| `main.py` | Seçilen siteleri eşzamanlı kazır, karşılaştırır, Telegram gönderir |
| `secilecek_siteler.txt` | **Asıl kontrol dosyası** — hangi sitelerin izleneceğini buradan, düz metin olarak ayarlarsınız (bkz. aşağıda) |
| `sites.json` | Site kataloğu (isim, host, duyuru URL'si) — genelde dokunmanız gerekmez, sadece yeni bir site eklerken |
| `requirements.txt` | Python bağımlılıkları |
| `duyurular.json` | Site başına daha önce görülmüş duyuruların kaydı (bot tarafından otomatik oluşturulur/güncellenir) |
| `.github/workflows/main.yml` | Günlük zamanlama, çalıştırma ve `duyurular.json`'u repoya commit'leme |
| `site_list.txt`, `site_scan_report.md`, `matched_sites.json` | `sites.json`'ın nasıl üretildiğine dair keşif/tarama çıktıları (referans, bot bunları kullanmaz) |

**Not:** Bir site `duyurular.json`'da ilk kez görülüyorsa (yeni kurulum ya da
sonradan seçime eklenmiş bir site), o sitenin mevcut duyuruları "yeni" sayıp
toplu bildirim göndermek yerine sadece referans olarak kaydedilir. Böylece ne
ilk kurulumda ne de sonradan bir site eklediğinizde toplu bildirim yağmuruna
maruz kalmazsınız — bot yalnızca gerçekten yeni çıkan duyuruları bildirir.

## `secilecek_siteler.txt` — hangi siteleri izleyeceğinizi ayarlamak

Programcı olmayan biri de kolayca düzenleyebilsin diye JSON değil, düz metin
kullanıyoruz. Dosyanın mantığı:

```
HEPSI

# --- Aşağıdaki 97 site referans listesidir (isim -> host) ---
# Adalet Meslek Yüksekokulu -> adalet.marmara.edu.tr
# Hukuk Fakültesi -> hukuk.marmara.edu.tr
# Tıp Fakültesi -> tip.marmara.edu.tr
...
```

- **`#` ile başlayan satırlar pasiftir**, bot onları yok sayar.
- **`HEPSI` satırı aktifken** (varsayılan durum budur — repo bu haliyle gelir),
  alttaki liste tamamen yok sayılır ve **97 sitenin tamamı** izlenir. Kod
  değişikliği veya başka hiçbir ayar gerekmez.
- **Sadece belirli siteleri izlemek istiyorsanız:**
  1. `HEPSI` satırının başına `#` koyup pasif hale getirin.
  2. Alttaki listede istediğiniz sitelerin başındaki `#` işaretini silin.
     Sadece # işareti kalkan satırlar aktif olur.
- **Yeni bir Marmara sitesi eklemek** için (aynı temayı kullanıyorsa —
  `https://<alt-alan-adı>/allnotices` adresini tarayıcıda açıp "Aktif Duyurular"
  görüyorsanız kullanır) önce `sites.json`'a `{"name", "host", "notices_url"}`
  şeklinde bir kayıt ekleyin, sonra burada adını yorumdan çıkarıp aktif edin
  (veya zaten `HEPSI` modundaysanız otomatik dahil olur).

## Kurulum

> **Başka bir Marmara öğrencisi/personeli misiniz?** Bu repoyu GitHub'da fork'layın,
> sadece adım 2-3'teki Telegram bilgilerini kendi hesabınızdan alıp kendi
> fork'unuzun Secrets'ına ekleyin. `secilecek_siteler.txt` varsayılan olarak
> `HEPSI` modundadır (97 site), isterseniz yukarıdaki bölümdeki gibi daraltabilirsiniz.
> Kod değişikliği gerekmez.

### 1) Repoyu oluşturun ve pushlayın

```bash
cd /home/emin/Desktop/marmaraduyurutakip
git init
git add .
git commit -m "Marmara duyuru takip botu"
git branch -M main
git remote add origin <GITHUB_REPO_URL>
git push -u origin main
```

> Repo **private** olabilir, workflow yine de çalışır.

### 2) Telegram bot'unuzu oluşturun

1. Telegram'da **@BotFather**'ı açın, `/newbot` yazın, bir isim ve kullanıcı adı
   verin (kullanıcı adı `bot` ile bitmeli, örn. `marmara_duyuru_bot`).
2. BotFather size bir **bot token** verecek (örn. `123456789:AAExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`).
   Bu değer `TELEGRAM_BOT_TOKEN` olacak.
3. Kendi Telegram'ınızdan yeni botunuzu bulup **/start** yazın (bota ilk mesajı
   siz göndermeden bot size mesaj gönderemez — Telegram'ın tek şartı bu, sonra
   süresiz geçerli).
4. `chat_id`'nizi öğrenmek için tarayıcıda şu adresi açın (TOKEN'ı kendi
   token'ınızla değiştirin):
   `https://api.telegram.org/bot<TOKEN>/getUpdates`
   Dönen JSON'da `"message":{"chat":{"id": ...}}` alanındaki sayı sizin
   `chat_id`'niz — bu değer `TELEGRAM_CHAT_ID` olacak. (Hiçbir şey görünmüyorsa
   önce adım 3'teki `/start`'ı gönderdiğinizden emin olun.)

### 3) GitHub Secrets'a ekleyin

Repo sayfasında: **Settings → Secrets and variables → Actions → New repository secret**

| Secret adı | Değer |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Adım 2.2'de BotFather'dan aldığınız token |
| `TELEGRAM_CHAT_ID` | Adım 2.4'te `getUpdates`'ten okuduğunuz chat_id |

### 4) Workflow'u test edin

Secrets eklendikten sonra repo sayfasında **Actions → Marmara Duyuru Takip Botu →
Run workflow** ile elle bir kez tetikleyip loglardan doğru çalıştığını doğrulayın
(workflow `workflow_dispatch` ile manuel tetiklemeye açıktır).

Bundan sonra bot her gün otomatik olarak 09:00-09:20 TR arasında çalışacak ve
yeni duyuru çıktığında size Telegram mesajı gönderecektir.

## Yerel test

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=... TELEGRAM_CHAT_ID=...
SKIP_RANDOM_DELAY=1 python main.py   # rastgele beklemeyi atlayarak hemen çalıştırır
```
