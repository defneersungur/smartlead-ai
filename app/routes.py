from flask import Blueprint, request, jsonify, render_template
from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

# sayfaları gösteren rotalar için ayrı bit blueprint
pages = Blueprint('pages', __name__)

# veri/api rotaları için ayrı bir blueprint
api = Blueprint('api', __name__)

@pages.route('/')
def anasayfa():
    # ziyaretçilerin gördüğü ana sayfa
    return render_template('index.html')

@pages.route('/dashboard')
def dashboard():
    # admin paneli, tüm leadleri listeler
    return render_template('dashboard.html')

# ziyaretçi mesajını alır, ai_service ile Groq'a iletilir,Groq'un yanıtı JSON olarak döndürülür
@api.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.get_json()
    mesaj = data.get('mesaj')
    gecmis = data.get('gecmis', [])

    # mesaj boşsa hata döndürür:400 
    if not mesaj:
        return jsonify({"basari": False, "hata": "Mesaj eksik"}), 400
    
    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)
        return jsonify({"basari": True, "cevap": cevap}), 200
    except AIServiceError as e:
        # Groq API çağrısı sırasında bir hata oluşursa bir hata JSON' döndür
        return jsonify({"basari": False, "hata": str(e)}), 503

# formdan gelen lead verilerini alır, database.py ile db ye kaydeder
@api.route('/leads', methods=['POST'])
def lead_kaydet():
    data = request.get_json()
    isim = data.get('isim')
    mail = data.get('mail')
    mesaj = data.get('mesaj', '')
    zorluk = data.get('zorluk', '')

    # isim ve mail alanları boşsa hata döndürür:400
    if not isim or not mail:
        return jsonify({"basari": False, "hata": "İsim ve mail zorunlu"}), 400
    
    lead_ekle(isim, mail, mesaj, zorluk)
    return jsonify({"basari": True}), 201

#db deki tüm leadleri listeler, repeater bu veriyi kullanır
@api.route('/leads', methods=['GET'])
def lead_listele():
    leadler = tum_leadler()
    return jsonify({"basari": True, "leadler": leadler}), 200