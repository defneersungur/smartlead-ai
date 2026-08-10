import os
from dotenv import load_dotenv

#.env dosyasındaki değişikenleri okuma
load_dotenv()

# Tüm ayarları ve gizli anahtarları .env'den okumak için temel yapılandırma sınıfı
class Config:

    #Flask'ın oturum ve güvenlik işlemleri için kullandığı gizli anahtar
    SECRET_KEY = os.environ.get('SECRET_KEY', 'gizli-anahtar-varsayilan')
    #SQLite veritabanı dosyasının yolu
    DATABASE_URL = os.environ.get('DATABASE_URL', 'leads.db')
    #Groq API anahtarı 
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    # kullanılan AI sağlayıcısı

    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    #Hangi domainden gelen isteklerin kabul edileceğini belirler
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')

    # AI asistanının kim olduğunu ve nasıl davranması gerektiğini tanımlama
    BUSINESS_CONTEXT = """ Bir planlama uygulamasinin tanitim sohbetisin. Kullanicilarla
    sicak ve kisa bir sekilde konusursun, onlara nasil yardimci olabilecegini sorarsin. 

    ONEMLI KISITLAMA: Gercek bir plan yapma, gorev onerme, takvim duzenleme
    veya zaman yonetimi tavsiyesi VERMEZSIN - urun henuz gelistirme
    asamasinda. Kullanici planlamayla ilgili bir sey sorsa veya senden
    yardim istese bile, somut bir plan/program/tavsiye onermek yerine,
    urunun yakinda cikacagini ve demo icin asagidan iletisim bilgilerini
    birakabilecegini soylersin.

    Turkce konus, kisa ve sicak cumleler kullan. Sohbetin dogal akmasina
    izin ver, kullaniciyi zorlamiyorsun ama uygun bir noktada iletisim
    bilgisi birakmasini nazikce hatirlatabilirsin. """

# yerel geliştirmede kullanılacak ayarlar
class DevelopmentConfig(Config):
    DEBUG = True

# render ortamında kullanılacak ayarlar
class ProductionConfig(Config):
    DEBUG = False

# ortama göre doğru config sınıfını seçmemizi sağlayan sözlük
# create_app() ile bu sözlükten hangi ortamda olduğumuzu okur 
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
    