from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams


qdrant = QdrantClient(":memory:")

COLLECTION_NAME = "documents"

def init_qdrant():
    collections = qdrant.get_collections().collections
    existing_names = [c.name for c in collections]

    if COLLECTION_NAME not in existing_names:
        qdrant.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,          
                distance="Cosine"  
            )
        )
