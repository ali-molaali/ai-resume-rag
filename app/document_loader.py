from pathlib import Path

from pypdf import PdfReader


def load_text_file(file_path: str) -> str:
    """Read a UTF-8 text file and return its contents."""
    path = Path(file_path)
    return path.read_text(encoding="utf-8")


def load_pdf_file(file_path: str) -> str:
    """Extract and return text from all pages in a PDF file."""
    reader = PdfReader(file_path)
    pages = [page.extract_text() or "" for page in reader.pages]

    return "\n".join(pages).strip()
