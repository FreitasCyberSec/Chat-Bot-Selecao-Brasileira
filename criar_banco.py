import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 1. Carrega as variáveis de ambiente (para garantir que o ambiente esteja configurado)
load_dotenv()

# --- CONFIGURAÇÕES DE CAMINHOS ---
# Pega a pasta onde este script está salvo
BASE_DIR = Path(__file__).resolve().parent
# Define onde está o arquivo de dados
DATA_DIR = BASE_DIR / "data"
CSV_FILE = DATA_DIR / "base_conhecimento_brasil.csv" 
# Define onde será salvo o banco vetorial
CHROMA_PATH = BASE_DIR / "chroma_db"

def main():
    print("--- 🇧🇷 INICIANDO O TREINAMENTO DA SELEÇÃO ---")

    # 2. Verificação de Segurança: O arquivo existe?
    if not CSV_FILE.exists():
        print(f"❌ ERRO CRÍTICO: O arquivo não foi encontrado!")
        print(f"   O sistema procurou em: {CSV_FILE}")
        print("   Dica: Verifique se a pasta se chama 'data' ou 'Data' e se o arquivo é .csv")
        return

    # 3. Limpeza: Apagar a memória antiga para não misturar dados
    if CHROMA_PATH.exists():
        print("🧹 Limpando banco de dados antigo...")
        try:
            shutil.rmtree(CHROMA_PATH)
            print("   -> Memória limpa com sucesso.")
        except Exception as e:
            print(f"⚠️  Aviso: Não foi possível apagar a pasta automaticamente. Erro: {e}")
            print("   Tente apagar a pasta 'chroma_db' manualmente se der erro na criação.")

    # 4. Leitura: Carregar o CSV Gigante
    print(f"📂 Lendo o arquivo: {CSV_FILE.name}...")
    try:
        loader = CSVLoader(
            file_path=str(CSV_FILE), 
            source_column="Fato_Ou_Resposta", 
            encoding="utf-8",
            csv_args={
                'delimiter': ',', 
                'quotechar': '"'
            }
        )
        documents = loader.load()
        total_docs = len(documents)
        print(f"   -> {total_docs} informações carregadas na memória.")
        
        if total_docs == 0:
            print("❌ ERRO: O arquivo CSV parece estar vazio ou mal formatado.")
            return

    except Exception as e:
        print(f"❌ Erro ao ler o CSV: {e}")
        return

    # 5. Processamento: Criar a Inteligência (Embeddings)
    print("🧠 Criando conexões neurais (Isso pode demorar um pouco)...")
    
    try:
        # Usa o modelo local (HuggingFace) para não gastar cota da API e ser mais rápido
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Processamento em Lotes (Batch) para garantir estabilidade com muitos dados
        batch_size = 200 
        for i in range(0, total_docs, batch_size):
            batch = documents[i:i+batch_size]
            print(f"   Processando lote {i} até {min(i+batch_size, total_docs)}...")
            
            if i == 0:
                # No primeiro lote, cria o banco
                db = Chroma.from_documents(batch, embeddings, persist_directory=str(CHROMA_PATH))
            else:
                # Nos lotes seguintes, adiciona ao banco existente
                db.add_documents(batch)
                
        print("\n✅ SUCESSO TOTAL! O Cérebro da Seleção está pronto.")
        print("🚀 Agora rode o servidor: python app.py")
        
    except Exception as e:
        print(f"❌ Erro durante o treinamento da IA: {e}")

if __name__ == "__main__":
    main()