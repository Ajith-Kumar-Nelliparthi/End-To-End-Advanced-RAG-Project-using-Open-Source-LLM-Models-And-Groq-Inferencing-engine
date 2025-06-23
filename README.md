# Complete RAG Project

A production-ready Retrieval-Augmented Generation (RAG) system built with FastAPI, LangChain, HuggingFace, Groq LLM, and AstraDB (Cassandra) vector store. This project demonstrates how to ingest web content, embed documents, store and retrieve them using a vector database, and answer user questions via a REST API.

---

## Features

- **Web Data Ingestion**: Load and split web pages into manageable text chunks.
- **Embeddings**: Generate embeddings using HuggingFace models (configurable).
- **Vector Store**: Store and retrieve document vectors using AstraDB (Cassandra) via CassIO.
- **LLM Integration**: Use Groq's Llama3-8B-8192 model for answer generation.
- **RAG Pipeline**: Retrieval-augmented generation with context-aware prompting.
- **REST API**: FastAPI endpoint for querying the RAG system.

---

## Project Structure

```
rag_project/
  app/                # FastAPI application
    main.py
  config/             # Configuration and settings
    settings.py
  src/
    embeddings/       # Embedding model loader
      embedder.py
    ingestion/        # Data loader and splitter
      loader.py
    llm/              # LLM integration
      groq_llm.py
    pipeline/         # RAG chain construction
      rag_chain.py
    vectorstore/      # Vector store integration
      astra_store.py
```

---

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/Ajith-Kumar-Nelliparthi/End-To-End-Advanced-RAG-Project-using-Open-Source-LLM-Models-And-Groq-Inferencing-engine.git
cd Complete_Rag_Project
```

### 2. Install Dependencies

It's recommended to use Python 3.12 (see [.python-version](.python-version)).

```sh
pip install -r requirements.txt
```

Or with [uv](https://github.com/astral-sh/uv):

```sh
uv pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the project root with the following variables:

```env
GROQ_API_KEY=your_groq_api_key
ASTRA_DB_TOKEN=your_astra_db_token
ASTRA_DB_ID=your_astra_db_id
```

---

## Usage

### Start the API Server

```sh
uvicorn rag_project.app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### Ask Questions

Send a GET request to `/ask` with your question:

```sh
curl "http://127.0.0.1:8000/ask?query=What is an agent in AI?"
```

Response:
```json
{
  "answer": "..."
}
```

---

## How It Works

1. **Ingestion**: Loads and splits web content (see [`src.ingestion.loader`](rag_project/src/ingestion/loader.py)).
2. **Embedding**: Generates vector embeddings for each chunk ([`src.embeddings.embedder`](rag_project/src/embeddings/embedder.py)).
3. **Vector Store**: Stores embeddings in AstraDB ([`src.vectorstore.astra_store`](rag_project/src/vectorstore/astra_store.py)).
4. **RAG Pipeline**: Retrieves relevant chunks and generates answers using Groq LLM ([`src.pipeline.rag_chain`](rag_project/src/pipeline/rag_chain.py)).
5. **API**: Exposes an `/ask` endpoint ([`app.main`](rag_project/app/main.py)).

---

## Configuration

- **Embedding Model**: Set via `EMBED_MODEL` in [`config.settings`](rag_project/config/settings.py).
- **Web URLs**: Modify the `urls` list in [`app.main`](rag_project/app/main.py) to change the data source.

---

## License

This project is licensed under the [GNU GPL v3](LICENSE).

---

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq](https://groq.com/)
- [HuggingFace](https://huggingface.co/)
- [AstraDB / CassIO](https://cassio.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
