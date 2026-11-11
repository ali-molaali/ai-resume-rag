# CareerLens AI

**A simple RAG chatbot for exploring my professional experience.**

CareerLens AI turns my resume into a searchable knowledge base. Instead of searching for exact keywords, users can ask questions in natural language and retrieve the most relevant parts of my experience.

This project is also a learning project: I am using it to understand document processing, embeddings, vector databases, and AI application design with Python.

## What it does

The current version can:

- Read a resume PDF document
- Split the document into searchable chunks
- Convert chunks into embeddings
- Store them in ChromaDB
- Retrieve relevant chunks using semantic search
- Send retrieved context to Groq
- Generate grounded answers in a Streamlit chat interface

The current chat experience uses retrieval-augmented generation to produce grounded answers.

## How it works

```text
Resume PDF
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
Groq LLM
      |
      v
Grounded answer
```

The LLM receives only the retrieved resume sections, which helps keep answers grounded in the source document.

## Technology

- Python
- ChromaDB
- Sentence Transformers
- Streamlit
- PyPDF
- python-dotenv
- Groq

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

Place the resume PDF at:

```text
data/documents/resume.pdf
```

### 5. Build the vector store

```powershell
python -m app.ingest
```

### 6. Configure the Groq key locally

Create `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your-groq-api-key"
```

Never commit this file or expose the key publicly.

### 7. Run the application

```powershell
python -m streamlit run app/main.py
```

## Project structure

```text
ai-resume-rag/
├── app/
│   ├── document_loader.py
│   ├── ingest.py
│   ├── llm.py
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
- [x] Add PDF ingestion
- [x] Connect retrieval to an LLM
- [x] Build the Streamlit chat interface
- [ ] Add source references to answers
- [ ] Deploy a live demo on Streamlit Cloud

## Learning approach

This project is developed step by step:

1. Explain the goal and logic before editing.
2. Show the exact file and code to change.
3. Explain Python syntax clearly.
4. Make one focused change at a time.
5. Verify the result before continuing.

## Why I built it

I have a strong background in Java development and am expanding my skills in Python and AI engineering. I built CareerLens AI to learn by creating a practical application rather than only studying isolated examples.

The project demonstrates the foundations of a production-oriented RAG workflow: ingestion, chunking, embeddings, vector storage, retrieval, and grounded generation.

## Author

**Ali Molaali**

- GitHub: [ali-molaali](https://github.com/ali-molaali)
