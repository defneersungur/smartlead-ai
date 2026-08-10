import sqlite3
from datetime import datetime

#veritabanı ile ilgili tüm işlemler sadece bu dosyada

# db'ye bağlanır ve satırlara sütun adıyla erişim sağlar
def get_db():
    conn = sqlite3.connect('leads.db')
    conn.row_factory = sqlite3.Row
    return conn

#leads tablosunu oluşturur
# uygulama her başlatıldığında create_app içinde çağrılır 
def init_db(app):
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            mail TEXT NOT NULL,
            mesaj TEXT,
            zorluk TEXT,
            tarih TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# yeni lead kaydını db ye ekler
# güvenlik için SQL enjeksiyonuna karşı değerler SQL metnine doğrudan eklenmiyor,
# bunun yerine ? yer tutucuları ile ayrı bir tuple kullanılıyor
def lead_ekle(isim, mail, mesaj, zorluk):
    conn = get_db()
    conn.execute(
        'INSERT INTO leads (isim, mail, mesaj, zorluk) VALUES (?, ?, ?, ?)',
        (isim, mail, mesaj, zorluk)
    )
    conn.commit()
    conn.close()

# tüm lead kayıtlarını yeniden eskiye sıralı şekilde getirir
# her kayda wix repeater için _id alanı eklenir

def tum_leadler():
    conn = get_db()
    leadler = conn.execute('SELECT * FROM leads ORDER BY tarih DESC').fetchall()
    conn.close()
    sonuc = []
    for lead in leadler:
        lead_dict = dict(lead)
        lead_dict['_id'] = str(lead_dict['id'])
        sonuc.append(lead_dict)
    return sonuc