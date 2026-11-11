import sys
from pathlib import Path

import streamlit as st

# Streamlit Cloud can execute this file with the app directory as sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.ingest import ingest_resume
from app.vector_store import create_collection, search_chunks
from app.llm import generate_answer


st.set_page_config(
    page_title="CareerLens AI",
    page_icon="📄",
)


@st.cache_resource
def ensure_resume_indexed() -> None:
    """Create the resume index on deployments where it does not exist yet."""
    collection = create_collection()

    if collection.count() == 0:
        ingest_resume()


ensure_resume_indexed()

st.title("CareerLens AI")
st.write("Ask questions about my professional experience.")

question = st.chat_input("Ask a question about the resume")

if question:
    st.chat_message("user").write(question)

    results = search_chunks(question)

    with st.chat_message("assistant"):
        api_key = st.secrets["GROQ_API_KEY"]

        answer = generate_answer(
            question=question,
            context=results,
            api_key=api_key,
        )

        st.write(answer)