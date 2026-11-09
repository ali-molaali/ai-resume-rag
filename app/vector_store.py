from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


CHROMA_PATH = Path("chroma_db")
COLLECTION_NAME = "resume_documents"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"


def create_collection():
    """Create or open the persistent resume collection."""
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )


def store_chunks(chunks: list[str]) -> None:
    """Create embeddings and store resume chunks in ChromaDB."""
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    embeddings = model.encode(chunks).tolist()

    collection = create_collection()

    ids = [f"resume-chunk-{index}" for index in range(len(chunks))]
    metadatas = [
        {"source": "resume.txt", "chunk_number": index}
        for index in range(len(chunks))
    ]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def search_chunks(query: str, number_of_results: int = 3) -> list[str]:
    """Find resume chunks most similar to a question."""
    model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    query_embedding = model.encode([query]).tolist()

    collection = create_collection()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=number_of_results,
    )

    return results["documents"][0]