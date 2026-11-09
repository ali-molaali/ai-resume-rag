from app.document_loader import load_pdf_file
from app.text_chunker import split_text
from app.vector_store import store_chunks


def ingest_resume() -> None:
    text = load_pdf_file("data/documents/resume.pdf")
    chunks = split_text(text)
    store_chunks(chunks)


if __name__ == "__main__":
    ingest_resume()