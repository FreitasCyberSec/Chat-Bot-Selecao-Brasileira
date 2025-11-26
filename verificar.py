import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Carrega a chave
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    print("❌ ERRO: Não achei a chave no arquivo .env")
else:
    print(f"🔑 Chave encontrada (início): {api_key[:5]}...")
    
    # 2. Configura
    genai.configure(api_key=api_key)
    
    print("\n🔎 PERGUNTANDO AO GOOGLE QUAIS MODELOS VOCÊ TEM...")
    try:
        # Lista todos os modelos disponíveis para sua conta
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ Disponível: {m.name}")
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")