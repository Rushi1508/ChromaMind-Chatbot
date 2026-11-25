"""Streamlit chat UI: retrieve context from ChromaDB, then answer with the Groq LLM."""
import streamlit as st

from config.settings import BOT_NAME
from knowledge_base import query_knowledge
from llm_response import generate_llm_response


def answer(question: str) -> str:
    docs = query_knowledge(question)
    if isinstance(docs, dict):  # query error
        return docs["error"]
    if isinstance(docs, str):  # empty knowledge base: fallback reply
        return docs
    context = "\n".join(f"- {d}" for d in docs)
    return generate_llm_response(f"Context:\n{context}\n\nQuestion: {question}")


st.title(f"💬 {BOT_NAME}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

if question := st.chat_input("Ask a question"):
    st.chat_message("user").markdown(question)
    with st.spinner("Thinking..."):
        reply = answer(question)
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages += [
        {"role": "user", "content": question},
        {"role": "assistant", "content": reply},
    ]
