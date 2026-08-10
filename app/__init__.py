from flask import Flask
from flask_cors import CORS
from config import config
from app.database import init_db
from app.routes import pages, api

# bu dosya tüm parçaları birleştiren bir fabrikadır: ayarlar, db, rotalar
# ve Flask uygulamasını oluşturur

def create_app(config_name='default'):

    app = Flask(__name__)

    #config.py deki doğru sınıfı (development/production) seçer
    app.config.from_object(config[config_name])

    # wix in bu backend' e istek atabilmesi için izin ver
    CORS(app, origins=app.config['CORS_ORIGINS'])

    # db tablosunu app context içinde oluşturur
    with app.app_context():
        init_db(app)

    # sayfaları ve api rotalarını blueprint ile kaydeder
    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix='/api')

    # sunucunun ayakta olduğunu kontrol etmek için basit bir endpoint
    @app.route('/health')
    def health():
        return {"durum": "aktif"}, 200
    
    return app