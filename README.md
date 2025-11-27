# ⚽ Chatbot RAG - Histórico da Seleção Brasileira

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-8E75B2?logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/Orchestration-LangChain-1C3C3C?logo=langchain&logoColor=white)

Este repositório contém a implementação de um assistente virtual baseado em **Inteligência Artificial Generativa**, utilizando a arquitetura **RAG (Retrieval-Augmented Generation)**.

O sistema foi projetado para responder a consultas em linguagem natural sobre a história, estatísticas e dados técnicos da Seleção Brasileira de Futebol, garantindo precisão factual através de uma base de conhecimento vetorial curada.

---

## 📖 Visão Geral do Projeto

O objetivo principal deste software é demonstrar a aplicação de modelos de linguagem (LLMs) em domínios de conhecimento fechados, mitigando o problema de "alucinação" comum em modelos generativos.

**Diferencial:** O sistema não depende apenas do conhecimento pré-treinado do modelo, mas consulta uma base de dados vetorial local antes de formular qualquer resposta.

---

## ✨ Principais Características

* **Arquitetura RAG:** Integração de recuperação de informação (Information Retrieval) com geração de texto.
* **Processamento Local (Edge AI):** Utilização de modelos de Embeddings open-source (HuggingFace) executados localmente na CPU, eliminando custos de tokenização na indexação.
* **Interface de API REST:** Backend desenvolvido em FastAPI para comunicação assíncrona e escalável.
* **Base de Dados Vetorial:** Implementação do **ChromaDB** para persistência e busca semântica de alta performance.
* **LLM de Última Geração:** Integração com a API do **Google Gemini (modelo gemini-2.0-flash)** para a camada de raciocínio e síntese.

---

## 🛠️ Stack Tecnológica

| Componente | Tecnologia |
| :--- | :--- |
| **Linguagem** | Python 3.10+ |
| **Backend Framework** | FastAPI / Uvicorn |
| **Orquestração de IA** | LangChain |
| **Banco Vetorial** | ChromaDB |
| **Embeddings** | sentence-transformers/all-MiniLM-L6-v2 |
| **Modelo Generativo** | Google Gemini 2.0 Flash |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |

---

## 📂 Estrutura do Projeto

```plaintext
/
├── app.py                      # Ponto de entrada da API (Servidor FastAPI)
├── criar_banco.py              # Script de pipeline ETL (Extração e Vetorização)
├── data/
│   └── base_conhecimento_brasil.csv  # Dataset estruturado (Fonte da verdade)
├── chroma_db/                  # Diretório de persistência do banco vetorial
├── index.html                  # Interface de usuário (Cliente Web)
├── .env                        # Configurações de ambiente e credenciais
├── .gitignore                  # Arquivos ignorados pelo versionamento
└── README.md                   # Documentação técnica