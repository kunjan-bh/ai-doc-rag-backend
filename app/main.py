from fastapi import FastAPI
from app.api import ingestion, chat

app = FastAPI(title="RAG Backend")

app.include_router(ingestion.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Backend is running!"}
