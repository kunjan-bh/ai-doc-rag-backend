from fastapi import FastAPI
from app.api import ingestion

app = FastAPI(title="PalmMind RAG Backend")

app.include_router(ingestion.router)

@app.get("/")
def root():
    return {"message": "Backend is running!"}
