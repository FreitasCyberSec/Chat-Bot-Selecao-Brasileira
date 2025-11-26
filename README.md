Chatbot RAG - Histórico da Seleção Brasileira
Este repositório contém a implementação de um assistente virtual baseado em Inteligência Artificial Generativa, utilizando a arquitetura RAG (Retrieval-Augmented Generation). O sistema foi projetado para responder a consultas em linguagem natural sobre a história, estatísticas e dados técnicos da Seleção Brasileira de Futebol, garantindo precisão factual através de uma base de conhecimento vetorial curada.

Visão Geral do Projeto
O objetivo principal deste software é demonstrar a aplicação de modelos de linguagem (LLMs) em domínios de conhecimento fechados, mitigando o problema de alucinação comum em modelos generativos. O sistema não depende apenas do conhecimento pré-treinado do modelo, mas consulta uma base de dados vetorial local antes de formular qualquer resposta.

Principais Características
Arquitetura RAG: Integração de recuperação de informação (Information Retrieval) com geração de texto.

Processamento Local (Edge AI): Utilização de modelos de Embeddings open-source (HuggingFace) executados localmente na CPU, eliminando custos de tokenização na indexação.

Interface de API REST: Backend desenvolvido em FastAPI para comunicação assíncrona e escalável.

Base de Dados Vetorial: Implementação do ChromaDB para persistência e busca semântica de alta performance.

LLM de Última Geração: Integração com a API do Google Gemini (modelo gemini-2.0-flash) para a camada de raciocínio e síntese.

Stack Tecnológica
Linguagem: Python 3.10+

Backend Framework: FastAPI / Uvicorn

Orquestração de IA: LangChain

Banco de Dados Vetorial: ChromaDB

Modelo de Embeddings: sentence-transformers/all-MiniLM-L6-v2

Modelo Generativo: Google Gemini 2.0 Flash

Frontend: HTML5, CSS3, JavaScript (Vanilla)

Estrutura do Projeto
Plaintext

/
├── app.py                 # Ponto de entrada da API (Servidor FastAPI)
├── criar_banco.py         # Script de pipeline ETL (Extração e Vetorização)
├── data/
│   └── base_conhecimento_brasil.csv  # Dataset estruturado (Fonte da verdade)
├── chroma_db/             # Diretório de persistência do banco vetorial
├── index.html             # Interface de usuário (Cliente Web)
├── .env                   # Configurações de ambiente e credenciais
├── .gitignore             # Arquivos ignorados pelo versionamento
└── README.md              # Documentação técnica
Instalação e Configuração
Siga as instruções abaixo para configurar o ambiente de desenvolvimento local.

1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. É recomendada a utilização de um ambiente virtual (venv).

2. Instalação de Dependências
Execute o comando abaixo no terminal para instalar todas as bibliotecas necessárias:

Bash

pip install fastapi uvicorn python-dotenv langchain langchain-community langchain-huggingface langchain-google-genai chromadb sentence-transformers
3. Configuração de Variáveis de Ambiente
Crie um arquivo nomeado .env na raiz do projeto para armazenar suas credenciais de segurança. O arquivo deve conter a chave da API do Google:

Snippet de código

GOOGLE_API_KEY=SuaChaveDeApiAqui
4. Inicialização da Base de Conhecimento (ETL)
Antes de iniciar o servidor, é necessário processar o arquivo CSV e gerar os índices vetoriais. Execute o script de ingestão:

Bash

python criar_banco.py
Este processo lerá o arquivo data/base_conhecimento_brasil.csv, converterá os dados textuais em vetores numéricos utilizando o modelo all-MiniLM-L6-v2 e salvará o resultado no diretório chroma_db.

5. Execução do Servidor
Inicie a aplicação backend:

Bash

python app.py
O servidor estará disponível em http://0.0.0.0:8000.

6. Acesso ao Frontend
Para interagir com o sistema, abra o arquivo index.html diretamente em qualquer navegador web moderno. O frontend se comunicará automaticamente com a API local.

Detalhes de Implementação
Pipeline de Recuperação (Retrieval)
O sistema utiliza um parâmetro k=50 na busca vetorial. Isso significa que, para cada pergunta do usuário, o algoritmo recupera os 50 fragmentos de informação mais relevantes semanticamente do banco de dados antes de enviá-los ao modelo generativo. Isso garante um contexto amplo e reduz drasticamente a possibilidade de respostas incorretas.

Engenharia de Prompt
O System Prompt foi configurado com instruções estritas ("System Instructions") para impedir que o modelo utilize conhecimento externo não verificado. O modelo é instruído a declarar explicitamente quando uma informação não consta na base de dados fornecida.

Autores
Projeto desenvolvido como parte dos requisitos da disciplina de Engenharia de Software e Inteligência Artificial.