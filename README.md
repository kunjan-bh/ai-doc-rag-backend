# PalmMind RAG Backend

This backend supports **Document Ingestion** and **Conversational RAG** (Retrieval-Augmented Generation) using FastAPI.  
It allows multi-turn conversations, semantic search over uploaded documents, and interview booking via chat.

---

## Features

### 1️⃣ Document Ingestion API
- Upload `.pdf` or `.txt` files.
- Extract text and split into chunks (two chunking strategies supported).
- Generate embeddings for document chunks.
- Store embeddings in **Qdrant** for semantic search.
- Save document metadata in **MySQL**.

### 2️⃣ Conversational RAG API
- Custom RAG (no `RetrievalQAChain` dependency).
- Supports multi-turn conversations with chat memory stored in **Redis**.
- Retrieves relevant context from Qdrant embeddings.
- Handles **interview booking**:
  - Detects booking requests in chat using LLM.
  - Stores booking info in **MySQL**.
  - Caches booking info in Redis for quick retrieval.
- Generates responses using document context and session history.

---

## Database & Data Schema

- **MySQL & Redis** are used for persistent and fast-access storage.
- **Qdrant** is used for vector embeddings and semantic search.
- Data schemas are provided in the `db` folder, which includes all tables and example inserts.

---

## Tech Stack

- **Backend:** FastAPI  
- **Database:** MySQL  
- **Vector Database:** Qdrant  
- **Cache / Chat Memory:** Redis  
- **Embeddings:** Custom service (can be swapped with OpenAI/Ollama embeddings)  
- **Python Dependencies:** Listed in `requirements.txt`

---

## Setup Instructions

1. Clone the repository
```bash
git clone <your-repo-url>
cd palm_rag_backend
```


2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. Start MySQL
-Create the database.
-Schema is provided in the db folder.

4. Start Qdrant
-Can be run via Docker or local installation.

5. Start Redis
-Required for chat memory and booking caching.

6. Run FastAPI server
```bash
uvicorn app.main:app --reload
```

7. Access API documentation
-Open http://127.0.0.1:8000/docs

