def chunk_text(text: str, strategy: str = "fixed", chunk_size: int = 500):
    chunks = []
    if strategy == "fixed":
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i + chunk_size])
    elif strategy == "paragraph":
        chunks = [p.strip() for p in text.split("\n\n") if p.strip()]
    else:
        raise ValueError("Invalid chunking strategy.")
    return chunks
