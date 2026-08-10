# SmartLead AI — Mushira

Ziyaretçilerle yapay zeka üzerinden sohbet eden ve iletişim bilgilerini (lead) toplayan bir sistem. Bu proje, Mushira adlı AI destekli kişisel planlama asistanı uygulamasının tanıtım/erken erişim sitesi için geliştirilmiştir.

## Ne Yapıyor

Sistem iki arayüzden oluşuyor:

- **Karşılama Sayfası** — ziyaretçiler Mushira ile sohbet edebiliyor, erken erişim için isim/mail/mesaj bırakabiliyor
- **Yönetim Paneli** — toplanan lead kayıtlarını tablo halinde gösteriyor

Backend, Flask ile yazılmış; sohbet Groq API üzerinden çalışıyor; veriler SQLite'ta tutuluyor; frontend Wix Studio (Velo) ile Render'daki bu backend'e bağlanıyor.

## Mimari

smartlead/
├── run.py # Sunucuyu başlatan giriş noktası
├── config.py # Tüm ayarlar ve anahtarlar (.env okur)
├── requirements.txt # Bağımlılık listesi
├── .env # Gizli anahtarlar 
└── app/
├── init.py # Uygulama fabrikası 
├── database.py # Veritabanı işlemleri 
├── routes.py # HTTP rotaları
├── templates/
│ ├── index.html
│ └── dashboard.html
└── services/
└── ai_service.py # Yapay zeka çağrıları

Her katman tek bir sorumluluğa sahip: `database.py` dışında hiçbir yerde SQL, `ai_service.py` dışında hiçbir yerde AI API çağrısı yok.

## Kullanılan Teknolojiler

- **Python 3.14** + **Flask** — backend sunucusu
- **SQLite** — veri saklama (leads tablosu)
- **Groq API** (`llama-3.3-70b-versatile`) — yapay zeka sohbet motoru
- **Wix Studio + Velo** — frontend (Karşılama Sayfası + Yönetim Paneli)
- **Render** — backend'in canlı olarak barındığı yer

## Yerel Olarak Çalıştırma

1. Sanal ortam oluştur ve aktive et:
python -m venv venv
.\venv\Scripts\Activate.ps1

2. Bağımlılıkları kur:
pip install -r requirements.txt

3. `.env` dosyası oluştur, içine API key ekle:

4. Sunucuyu başlat:
python run.py

5. Tarayıcıda `http://127.0.0.1:5000/health` adresine git — `{"durum": "aktif"}` görüyorsan hazırsın.

## API Uç Noktaları

| Metod | Yol | Görev |
|---|---|---|
| GET | `/health` | Sunucu canlılık kontrolü |
| GET | `/` | Karşılama sayfası (teknik/yer tutucu) |
| GET | `/dashboard` | Yönetim paneli (teknik/yer tutucu) |
| POST | `/api/sohbet` | AI'a mesaj gönderir, cevap döner |
| POST | `/api/leads` | Yeni lead kaydeder |
| GET | `/api/leads` | Tüm lead'leri listeler |

**Not:** Gerçek kullanıcı arayüzü Wix Studio'da barınıyor (mushira.app), buradaki `index.html`/`dashboard.html` sadece yönergenin mimari gereksinimini karşılayan basit yer tutuculardır.

## Bağlantılar

- **Canlı Backend (Render):** https://smartlead-ai-fies.onrender.com
- **Site (Wix):** https://mushira.app
- **Yönetim Paneli:** https://mushira.app/dashboard

