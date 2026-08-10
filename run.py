from app import create_app

# fabrikadan Flask uygulamasını oluşturur
app = create_app()

# bu dosya çalıştırıldığında sunucuyu başlatır: phython run.py
if __name__ == '__main__':
    app.run(port=5000)