from app.document_loader import load_pdf_bytes, load_pdf_file
from app.text_chunker import split_text
from app.vector_store import store_chunks
from app.vector_store import reset_collection, store_chunks

def ingest_uploaded_pdfs(files: list[tuple[str, bytes]]) -> None:
    """Create chunks from uploaded PDF files."""
    chunks: list[str] = []
    sources: list[str] = []

    for filename, content in files:
        text = load_pdf_bytes(content)

        if not text:
            raise ValueError(f"No extractable text found in {filename}.")

        file_chunks = split_text(text)
        chunks.extend(file_chunks)
        sources.extend([filename] * len(file_chunks))

    if not chunks:
        raise ValueError("The uploaded PDFs contain no searchable text.")
    reset_collection()
    store_chunks(chunks, sources)
def ingest_resume() -> None:
    text = load_pdf_file("data/documents/resume.pdf")
    chunks = split_text(text)
    store_chunks(chunks)


if __name__ == "__main__":
    ingest_resume()