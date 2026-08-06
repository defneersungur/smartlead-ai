from flask import Blueprint, request, jsonify, render_template
from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

pages = Blueprint('pages', __name__)
api = Blueprint('api', __name__)

@pages.route('/')
def anasayfa():
    return render_template('index.html')

@pages.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@api.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.get_json()
    mesaj = data.get('mesaj')
    gecmis = data.get('gecmis', [])
    
    if not mesaj:
        return jsonify({"basari": False, "hata": "Mesaj eksik"}), 400
    
    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)
        return jsonify({"basari": True, "cevap": cevap}), 200
    except AIServiceError as e:
        return jsonify({"basari": False, "hata": str(e)}), 503


@api.route('/leads', methods=['POST'])
def lead_kaydet():
    data = request.get_json()
    isim = data.get('isim')
    mail = data.get('mail')
    mesaj = data.get('mesaj', '')
    zorluk = data.get('zorluk', '')
    
    if not isim or not mail:
        return jsonify({"basari": False, "hata": "İsim ve mail zorunlu"}), 400
    
    lead_ekle(isim, mail, mesaj, zorluk)
    return jsonify({"basari": True}), 201


@api.route('/leads', methods=['GET'])
def lead_listele():
    leadler = tum_leadler()
    return jsonify({"basari": True, "leadler": leadler}), 200