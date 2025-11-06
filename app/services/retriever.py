from app.db.qdrant_client import qdrant, COLLECTION_NAME

def retrieve_context(query_vector, top_k=3):
    results = qdrant.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )
    return [r.payload["text"] for r in results]
