import requests
from config import Config

# bu dosya Groq ile ilgili tüm çağrıları içerir


#Grop API ye bağlanırken bir sorun olursa bu özel hata sınıfı fırlatılır
# routes.py içinde yakalanır ve kullanıcıya uygun bir mesaj döndürülür
class AIServiceError(Exception):
    pass

# kullanıcı mesajını alır, Groq API ye gönderir ve yanıtı döndürür
class AIService:
    def yanit_uret(self, mesaj, gecmis=None):
        if gecmis is None:
            gecmis = []
        # API anahtarı yoksa demo modu mesajı döndür"
        if not Config.GROQ_API_KEY:
            return "Şu an demo modundayım, gerçek bir AI cevabı veremiyorum. Lütfen API anahtarını kontrol edin."

        #Groq un mesaj sırası: sistem mesajı, konuşma geçmişi, kullanıcının yeni mesajı
        messages = [{"role": "system", "content": Config.BUSINESS_CONTEXT}]
        messages.extend(gecmis)
        messages.append({"role": "user", "content": mesaj})

        # Groq API ye POST isteği gönderir ve yanıtı döndürür
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {Config.GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openai/gpt-oss-120b",
                    "messages": messages,
                    "temperature": 0.5,
                    "max_tokens": 150
                }
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            # Groq API çağrısı sırasında bir hata oluşursa özel hata fırlatılır
            raise AIServiceError(f"Groq API hatası: {str(e)}")
        
# AIService sınıfının bir örneği oluşturulur ve routes.py içinde kullanılır
ai_service = AIService()    