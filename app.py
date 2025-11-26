import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# 1. Carrega a chave do .env
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

app = FastAPI()

# 2. Configuração de CORS (Permite o site falar com o Python)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CONFIGURAÇÕES ---
CHROMA_PATH = "chroma_db"

print("🛡️  Iniciando Servidor (Modelo Gemini 2.0 Flash)...")

rag_chain = None

try:
    # 3. Cérebro Local (Banco de Dados)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    
    # Recupera bastante contexto (50 documentos)
    retriever = vector_store.as_retriever(search_kwargs={"k": 50})
    
    # 4. Cérebro da IA (CORRIGIDO PARA O MODELO DA SUA LISTA)
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash",  # <--- USANDO O MODELO QUE APARECEU NO SEU PRINT
        temperature=0.0, 
        google_api_key=api_key
    )

    # 5. Prompt Anti-Alucinação
    template = """
    Você é o Canarinho, o assistente oficial da Seleção Brasileira.
    Sua missão é responder perguntas usando ESTRITAMENTE os dados fornecidos abaixo.
    
    REGRAS:
    1. Use SOMENTE o "Contexto Oficial" abaixo.
    2. Se a resposta não estiver no contexto, diga: "Desculpe, torcedor. Não encontrei essa informação nos meus arquivos."
    3. Seja simpático e use emojis.
    
    Contexto Oficial:
    {context}
    
    Pergunta do Torcedor: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    
    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    rag_chain = (
        {"context": retriever | RunnableLambda(format_docs), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    print("✅ Servidor Conectado e Pronto!")

except Exception as e:
    print(f"❌ Erro ao carregar: {e}")

class UserRequest(BaseModel):
    prompt: str

@app.post("/api/chat")
async def chat(request: UserRequest):
    if not rag_chain:
        return {"resposta": "Erro de conexão com a IA. Verifique se o modelo está correto."}
    try:
        print(f"Recebendo pergunta: {request.prompt}")
        resposta = rag_chain.invoke(request.prompt)
        return {"resposta": resposta}
    except Exception as e:
        print(f"ERRO DETALHADO: {e}") 
        return {"resposta": "Houve um erro tático no servidor. Tente de novo."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)