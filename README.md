# Marmara Üniversitesi Duyuru Takip ve WhatsApp Bildirim Botu

Her gün Türkiye saatiyle 09:00-09:20 arasında `https://www.marmara.edu.tr/allnotices`
sayfasını kontrol eder, önceden görülmemiş duyuruları WhatsApp üzerinden bildirir.
Tamamen GitHub Actions üzerinde, sunucusuz çalışır.

## Dosyalar

| Dosya | Görev |
|---|---|
| `main.py` | Scraping, karşılaştırma, WhatsApp gönderimi |
| `requirements.txt` | Python bağımlılıkları |
| `duyurular.json` | Daha önce görülmüş/gönderilmiş duyuruların kaydı (bot tarafından otomatik oluşturulur/güncellenir) |
| `.github/workflows/main.yml` | Günlük zamanlama, çalıştırma ve `duyurular.json`'u repoya commit'leme |

**Not:** İlk çalıştırmada `duyurular.json` yoktur; bot o an sayfada gördüğü tüm
duyuruları sadece referans olarak kaydeder, WhatsApp bildirimi göndermez. Böylece
kurulum anında sitede zaten var olan duyurular için toplu bildirim yağmuruna
maruz kalmazsınız — bot bundan sonra çıkan **gerçekten yeni** duyuruları bildirir.

## Kurulum

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
