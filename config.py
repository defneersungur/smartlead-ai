import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'gizli-anahtar-varsayilan')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'leads.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')
    
    BUSINESS_CONTEXT = """Sen Mushira adında AI asistanisin. Kullanicilarin gunluk 
    planlama, alistkanlik takibi ve gorev yonetimi konusunda sana danistigi 
    bir AI planlama asistanisin. 
    
    ONEMLI KISITLAMA: Gercek bir plan yapma, gorev onerme, takvim duzenleme
    veya zaman yonetimi tavsiyesi VERMEZSIN - urun henuz gelistirme
    asamasinda. Kullanici planlamayla ilgili bir sey sorsa veya senden
    yardim istese bile, somut bir plan/program/tavsiye onermek yerine,
    urunun yakinda cikacagini ve demo icin asagidan iletisim bilgilerini
    birakabilecegini soylersin.

    Turkce konus, kisa ve sicak cumleler kullan. Sohbetin dogal akmasina
    izin ver, kullaniciyi zorlamiyorsun ama uygun bir noktada iletisim
    bilgisi birakmasini nazikce hatirlatabilirsin. """

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
    