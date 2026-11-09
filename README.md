# CareerLens AI

**A simple RAG chatbot for exploring my professional experience.**

CareerLens AI turns my resume into a searchable knowledge base. Instead of searching for exact keywords, users can ask questions in natural language and retrieve the most relevant parts of my experience.

This project is also a learning project: I am using it to understand document processing, embeddings, vector databases, and AI application design with Python.

## What it does

The current version can:

- Read a resume text document
- Split the document into searchable chunks
- Convert chunks into embeddings
- Store them in ChromaDB
- Retrieve relevant chunks using semantic search

The Streamlit chat experience and final LLM-generated answers are the next parts of the project.

## How it works

```text
Resume document
      |
      v
Text chunking
      |
      v
Sentence Transformers embeddings
      |
      v
ChromaDB vector database
      |
      v
Semantic search
      |
      v
Relevant resume sections
```

In the final version, an LLM will use the retrieved sections to answer questions and provide grounded responses based on the resume.

## Technology

- Python
- ChromaDB
- Sentence Transformers
- Streamlit
- PyPDF
- python-dotenv

## Run locally

### 1. Clone the repository

```powershell
git clone https://github.com/ali-molaali/ai-resume-rag.git
cd ai-resume-rag
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run this once in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Add a document

Place a text resume at:

```text
data/documents/resume.txt
```

### 5. Build the vector store and search it

```powershell
python -c "from app.document_loader import load_text_file; from app.text_chunker import split_text; from app.vector_store import store_chunks; text = load_text_file('data/documents/resume.txt'); store_chunks(split_text(text))"
```

Then run a semantic search:

```powershell
python -c "from app.vector_store import search_chunks; print(search_chunks('What backend technologies are mentioned?'))"
```

## Project structure

```text
ai-resume-rag/
├── app/
│   ├── document_loader.py
│   ├── main.py
│   ├── text_chunker.py
│   └── vector_store.py
├── data/
│   └── documents/
├── chroma_db/
├── requirements.txt
└── README.md
```

`chroma_db/` is generated locally and is intentionally excluded from Git.

## Roadmap

- [x] Set up the Python project
- [x] Add document loading
- [x] Add recursive text chunking
- [x] Store embeddings in ChromaDB
- [x] Add semantic search
- [ ] Add PDF ingestion
- [ ] Connect retrieval to an LLM
- [ ] Build the Streamlit chat interface
- [ ] Add source references to answers
- [ ] Deploy a live demo on Streamlit Cloud

## Why I built it

I have a strong background in Java development and am expanding my skills in Python and AI engineering. I built CareerLens AI to learn by creating a practical application rather than only studying isolated examples.

The project demonstrates the foundations of a production-oriented RAG workflow: ingestion, chunking, embeddings, vector storage, retrieval, and grounded generation.

## Author

**Ali Molaali**

- GitHub: [ali-molaali](https://github.com/ali-molaali)
