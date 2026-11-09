import streamlit as st

from app.vector_store import search_chunks
from app.llm import generate_answer


st.set_page_config(
    page_title="CareerLens AI",
    page_icon="📄",
)

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