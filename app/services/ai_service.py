import requests
from config import Config

class AIServiceError(Exception):
    pass

class AIService:
    def yanit_uret(self, mesaj, gecmis=None):
        if gecmis is None:
            gecmis = []
        
        if not Config.GROQ_API_KEY:
            return "Şu an demo modundayım, gerçek bir AI cevabı veremiyorum. Lütfen API anahtarını kontrol edin."
        
        messages = [{"role": "system", "content": Config.BUSINESS_CONTEXT}]
        messages.extend(gecmis)
        messages.append({"role": "user", "content": mesaj})
        
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {Config.GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama-3.1-8b-instant",
                    "messages": messages
                }
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            raise AIServiceError(f"Groq API hatası: {str(e)}")
ai_service = AIService()    