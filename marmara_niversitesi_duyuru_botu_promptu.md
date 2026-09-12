# Marmara Üniversitesi Duyuru Takip ve WhatsApp Bildirim Botu

**Rolün:** Sen uzman bir Python geliştiricisi ve DevOps mühendisisin. Aşağıda detayları verilen projeyi sıfırdan, en iyi pratiklere uygun ve hatasız çalışacak şekilde kodlaman ve dağıtım (deployment) adımlarını bana vermen gerekiyor.

## 1. Proje Özeti
Marmara Üniversitesi'nin web sitesindeki duyuruları her gün takip eden, sadece **yeni** çıkan duyuruları tespit eden ve bunları bana WhatsApp üzerinden mesaj olarak gönderen bir otomasyon betiği (script) yazılacaktır. Kullanıcı bilgisayarını her gün kapattığı için sistem **GitHub Actions** üzerinde sunucusuz (serverless) olarak çalışacak şekilde tasarlanmalıdır.

## 2. Sistem İş Akışı
1. Sistem her gün saat 09:00'da (Türkiye saati ile) GitHub Actions tarafından tetiklenecektir.
2. Kod çalıştığı an itibariyle **09:00 ile 09:20 arasında rastgele bir saatte** duyuruları kontrol etmesi için 0 ile 1200 saniye arasında rastgele bir bekleme (`time.sleep()`) yapacaktır.
3. Bekleme süresi bittikten sonra Marmara Üniversitesi'nin duyuru sayfası kazınacak (scrape edilecek) ve güncel duyurular (Başlık, Tarih, Link) çekilecektir.
4. Çekilen duyurular, önceden kaydedilmiş olan bir veritabanı dosyasıyla (örneğin `duyurular.json`) karşılaştırılacaktır.
5. Sadece önceden kaydedilmemiş **yeni** duyurular filtrelenecektir.
6. Yeni duyuru varsa, Meta WhatsApp Cloud API kullanılarak belirlenen numaraya WhatsApp mesajı olarak gönderilecektir. (Mesaj formatı: "🚨 *Yeni Duyuru:* [Başlık]\n🔗 [Link]")
7. Gönderilen yeni duyurular `duyurular.json` dosyasına eklenecek ve GitHub Actions üzerinden repoya commit edilerek (veya basit bir gist/çevre değişkeni kullanılarak) kaydedilecektir ki ertesi gün tekrar gönderilmesin.

## 3. Teknik Gereksinimler

### 3.1. Kullanılacak Teknolojiler ve Kütüphaneler
* **Dil:** Python 3.x
* **Web Scraping:** `requests` ve `BeautifulSoup4`
* **Zamanlama & Rastgelelik:** `random`, `time` (Standart kütüphaneler)
* **Veri Saklama:** JSON formatında dosya okuma/yazma (`json` kütüphanesi). GitHub Actions üzerinde dosyanın kalıcı olması için kodun sonunda git commit işlemi yapılmalıdır.
* **WhatsApp Entegrasyonu:** Meta WhatsApp Cloud API (`requests` ile API'ye HTTP POST isteği).
* **CI/CD & Otomasyon:** GitHub Actions (`.github/workflows/main.yml`)

### 3.2. Çevresel Değişkenler (Environment Variables)
Kod içinde API anahtarları açıkça yazılmamalı, `os.environ.get()` kullanılarak GitHub Secrets üzerinden alınmalıdır. Gerekli değişkenler:
* `WA_TOKEN` (WhatsApp Cloud API kalıcı erişim belirteci)
* `WA_PHONE_NUMBER_ID` (Gönderici telefon numarası kimliği)
* `TARGET_PHONE_NUMBER` (Mesajın gideceği telefon numarası)

## 4. Senden Beklenen Çıktılar

Lütfen bana şu dosyaları ve açıklamaları hazırla:

1. **`main.py`:** Rastgele bekleme, web scraping, JSON dosyasından eski duyuruları kontrol etme, yeni duyuruları WhatsApp API ile gönderme ve JSON dosyasını güncelleme işlemlerini yapan ana Python kodu. (Hata yakalama - try/except blokları eklenmiş olmalı).
2. **`requirements.txt`:** Kurulması gereken Python kütüphaneleri.
3. **`.github/workflows/main.yml`:** Kodu her gün Türkiye saati ile 09:00'da (Cron UTC ayarına dikkat ederek) çalıştıracak, bağımlılıkları kuracak, `main.py`'yi çalıştıracak ve eğer `duyurular.json` dosyasında bir değişiklik olduysa bunu repoya commit edip pushlayacak GitHub Actions konfigürasyon dosyası.
4. **Kurulum Rehberi:** Meta WhatsApp Cloud API'nin nasıl alınacağı ve GitHub Secrets'a bu değişkenlerin nasıl ekleneceğine dair kısa bir adım adım rehber.

Lütfen kodları yazarken temiz, modüler ve açıklayıcı yorum satırları içeren bir yapı kullan.