# Marmara Üniversitesi Duyuru Takip ve WhatsApp Bildirim Botu

Her gün Türkiye saatiyle 09:00-09:20 arasında, `sites.json`'da listelenen **97
Marmara Üniversitesi sitesinin** (tüm fakülteler, enstitüler, MYO'lar, daire
başkanlıkları, koordinatörlükler — bkz. `site_scan_report.md`) duyuru
sayfalarını eşzamanlı kontrol eder, önceden görülmemiş duyuruları WhatsApp
üzerinden bildirir. Tamamen GitHub Actions üzerinde, sunucusuz çalışır.

**Şablon/çoğaltılabilir tasarım:** Bu repo tek bir kişiye özel değil — Marmara'da
herkes bu repoyu fork'layıp sadece kendi WhatsApp numarasını ve (isterse) hangi
sitelerin izleneceğini ayarlayarak kendi botunu çalıştırabilir. `main.py`'de
kod değişikliği gerekmez.

## Dosyalar

| Dosya | Görev |
|---|---|
| `main.py` | Seçilen siteleri eşzamanlı kazır, karşılaştırır, WhatsApp gönderir |
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
> sadece adım 2-3'teki WhatsApp bilgilerini kendi hesabınızdan alıp kendi
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

### 2) Meta WhatsApp Cloud API bilgilerini alın

1. https://developers.facebook.com adresinden bir **Meta Developer** hesabı açın
   (yoksa mevcut Facebook hesabınızla giriş yapabilirsiniz).
2. **My Apps → Create App** ile yeni bir uygulama oluşturun, tür olarak
   **Business** seçin.
3. Uygulama panelinde **WhatsApp → Getting Started**'a girin. Meta size otomatik
   olarak:
   - Bir **test telefon numarası** ve buna ait **Phone number ID** (`WA_PHONE_NUMBER_ID`) verir.
   - Bir **geçici (24 saatlik) erişim token'ı** verir — bunu kalıcı hale getirmeniz gerekir (adım 4).
4. Kalıcı token için: **App ayarları → Business Settings → System Users**'a gidip
   bir sistem kullanıcısı oluşturun, WhatsApp uygulamanıza `whatsapp_business_messaging`
   ve `whatsapp_business_management` yetkilerini atayın ve buradan **süresiz
   (never expire)** bir erişim token'ı üretin. Bu token'ı `WA_TOKEN` olarak kullanacaksınız.
5. **Bildirim alacak telefon numarasını** (kendi WhatsApp numaranız,
   ülke kodu ile ve `+` işareti olmadan, örn. `905xxxxxxxxx`) test panelindeki
   **"To"** alanına ekleyip doğrulama kodunu girin — Meta test modunda sadece
   burada onaylanmış numaralara mesaj gönderebilir. Bu numara `TARGET_PHONE_NUMBER`
   olacak.
6. (İsteğe bağlı, kalıcı kullanım için) Uygulamayı **App Review**'dan geçirip
   canlıya (Live) alın ve kendi işletme telefon numaranızı ekleyin; test modunda
   kalırsanız 24 saatte bir "Hello World" şablon mesajıyla pencereyi yenilemeniz
   gerekebilir — günlük duyuru botu için bu genelde sorun çıkarmaz çünkü zaten
   her gün mesaj gönderiliyor.

### 3) GitHub Secrets'a ekleyin

Repo sayfasında: **Settings → Secrets and variables → Actions → New repository secret**

| Secret adı | Değer |
|---|---|
| `WA_TOKEN` | Adım 2.4'te aldığınız kalıcı erişim token'ı |
| `WA_PHONE_NUMBER_ID` | Adım 2.3'te aldığınız Phone number ID |
| `TARGET_PHONE_NUMBER` | Bildirimlerin gideceği numara (örn. `905xxxxxxxxx`) |

### 4) Workflow'u test edin

Secrets eklendikten sonra repo sayfasında **Actions → Marmara Duyuru Takip Botu →
Run workflow** ile elle bir kez tetikleyip loglardan doğru çalıştığını doğrulayın
(workflow `workflow_dispatch` ile manuel tetiklemeye açıktır).

Bundan sonra bot her gün otomatik olarak 09:00-09:20 TR arasında çalışacak ve
yeni duyuru çıktığında size WhatsApp mesajı gönderecektir.

## Yerel test

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export WA_TOKEN=... WA_PHONE_NUMBER_ID=... TARGET_PHONE_NUMBER=...
SKIP_RANDOM_DELAY=1 python main.py   # rastgele beklemeyi atlayarak hemen çalıştırır
```
