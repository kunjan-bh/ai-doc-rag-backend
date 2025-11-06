from fastapi import APIRouter, UploadFile, File, Form
import uuid
import os
from enum import Enum

from app.services.file_reader import extract_text_from_file
from app.services.chunking import chunk_text
from app.services.embeddings import get_embeddings
from app.db.qdrant_client import qdrant, COLLECTION_NAME, init_qdrant
from qdrant_client.models import PointStruct
from app.db.sql_client import save_document_metadata, save_chunk_metadata

# ------------------------------
# Enum for chunking strategy
# ------------------------------
class ChunkStrategy(str, Enum):
    fixed = "fixed"
    paragraph = "paragraph"

router = APIRouter(prefix="/ingest", tags=["Document Ingestion"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
init_qdrant()


@router.post("/")
async def ingest_document(
    file: UploadFile = File(...),
    chunk_strategy: ChunkStrategy = Form(ChunkStrategy.fixed)  # Enum dropdown
):
    strategy = chunk_strategy.value  # Convert Enum to string

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_file(file_path)
    chunks = chunk_text(text, strategy=strategy)
    embeddings = get_embeddings(chunks)

    document_id = str(uuid.uuid4())

    points = [
        PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={"text": chunk}
        )
        for chunk, vector in zip(chunks, embeddings)
    ]

    qdrant.upsert(collection_name=COLLECTION_NAME, points=points)
    save_document_metadata(document_id, file.filename, file.filename.split(".")[-1])

    for idx, chunk in enumerate(chunks):
        chunk_id = str(uuid.uuid4())
        save_chunk_metadata(chunk_id, document_id, idx, chunk)

    return {
        "status": "success",
        "chunks_stored": len(chunks),
        "document_id": document_id
    }
