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
    bir AI planlama asistanisin. Sicak, sakin ve yonlendirici bir dille konus. 
    Turkce konus. Kullaniciyi yargilamadan, kucuk iyilestirmeler icin nazikce 
    tesvik et. Sohbetin sonunda, kullaniciyi erken erisim icin iletisim 
    bilgisi birakmaya nazikce yonlendir."""

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
    