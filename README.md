🇧🇷 Arena CBF - Chatbot Inteligente da Seleção
Um assistente virtual especialista na história da Seleção Brasileira de Futebol, construído com arquitetura RAG (Retrieval-Augmented Generation) para garantir respostas precisas, livres de alucinações e baseadas em dados históricos reais.

 Sobre o Projeto
Este projeto é uma aplicação Fullstack que utiliza Inteligência Artificial para responder perguntas sobre a Seleção Brasileira. Diferente de chats comuns (como o ChatGPT puro), este bot utiliza uma Base de Conhecimento Curada (Vector Database) contendo registros de mais de 1.000 partidas, perfis de jogadores, táticas históricas e curiosidades culturais.

O sistema foi projetado para atuar como uma enciclopédia interativa, cobrindo desde o primeiro jogo em 1914 até o ciclo da Copa de 2026.

 Funcionalidades Principais
 Inteligência Híbrida: Utiliza Embeddings Locais (HuggingFace) para busca semântica rápida e gratuita, e Google Gemini 2.0 para geração de respostas naturais.

 Sistema Anti-Alucinação: Configurado com temperatura zero e prompts restritivos para responder apenas com base nos dados oficiais, garantindo precisão histórica.

 Base de Dados Massiva: Contém registros detalhados de todos os jogos, fichas técnicas de lendas (Pelé, Garrincha, Marta), táticas de Copas e folclore do futebol.

 Interface Imersiva: Frontend temático ("Arena Virtual") com identidade visual da CBF, responsivo e com feedback visual de carregamento.

 Tecnologias Utilizadas
Backend (API & AI)
Linguagem: Python

Framework Web: FastAPI (Servidor Assíncrono)

Orquestração de IA: LangChain

Banco de Dados Vetorial: ChromaDB (Persistência Local)

Embeddings: sentence-transformers/all-MiniLM-L6-v2 (HuggingFace)

LLM (Modelo de Linguagem): Google gemini-2.0-flash

Frontend (Interface)
Linguagens: HTML5, CSS3, JavaScript (Vanilla)

Estilização: CSS Customizado com animações e responsividade.

Comunicação: Fetch API para consumo do endpoint REST.

 Estrutura do Projeto
CHAT_SELECAO/
│
├── chroma_db/          # O "Cérebro" (Banco de dados vetorial gerado)
├── data/
│   └── base_conhecimento_brasil.csv  # Fonte da Verdade (+1000 registros)
│
├── app.py              # Servidor FastAPI (Backend)
├── criar_banco.py      # Script ETL (Extração e Ingestão de Dados)
├── index.html          # Interface de Usuário (Frontend)
├── .env                # Variáveis de Ambiente (API Keys)
└── README.md           # Documentação
 Como Rodar Localmente
Siga os passos abaixo para executar o projeto na sua máquina.

1. Pré-requisitos
Python instalado.

Uma chave de API do Google (Gemini).

2. Instalação das Dependências
No terminal, instale as bibliotecas necessárias:

Bash

pip install fastapi uvicorn python-dotenv langchain langchain-community langchain-huggingface langchain-google-genai chromadb sentence-transformers
3. Configuração de Ambiente
Crie um arquivo chamado .env na raiz do projeto e adicione sua chave:

Snippet de código

GOOGLE_API_KEY=SuaChaveAquiSemEspacos
4. Ingestão de Dados (Criar o Cérebro)
Execute o script que lê o CSV e cria o banco vetorial. Isso deve ser feito na primeira vez ou sempre que os dados mudarem.

Bash

python criar_banco.py
(Aguarde a mensagem "✅ SUCESSO TOTAL!")

5. Iniciar o Servidor
Suba a API Backend:

Bash

python app.py
(O servidor iniciará em http://0.0.0.0:8000)

6. Acessar
Abra o arquivo index.html no seu navegador. Pronto! O bot está operante.

 Detalhes da Engenharia de Dados
O arquivo base_conhecimento_brasil.csv foi estruturado para cobrir cinco dimensões do conhecimento:

Fatos: Resultados exatos de partidas (1914-2025).

Biografias: Perfis de jogadores e técnicos lendários.

Tática: Evolução dos esquemas (do 4-2-4 de 58 ao 4-3-3 moderno).

Cultura: Músicas de torcida, mascotes, apelidos e frases famosas.

Tabus e Polêmicas: Histórias de bastidores, "maldições" e recordes.

 Autor
Desenvolvido como parte de um projeto acadêmico de Engenharia de Software e Inteligência Artificial.

“Brasil, o país do futebol.” 🇧🇷