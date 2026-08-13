import os
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.documents import Document

import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI


SYSTEM_PROMPT = """
You are an AI Enterprise Document Assistant.

Answer the user's question ONLY using the retrieved document context.

Rules:
1. Do not use outside knowledge.
2. If the answer is not found, reply exactly:
   "I couldn't find this information in the uploaded documents."
3. Be clear and concise.
4. At the end, include the sources used.

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{question}")
])


def format_context(documents):
    formatted_context = []

    for doc in documents:
        source = Path(doc.metadata.get("source", "Unknown")).name
        page = doc.metadata.get("page", "N/A")

        formatted_context.append(f"Source : {source}\nPage   : {page}\n\nContent:\n{doc.page_content}")

    return "\n\n".join(formatted_context)


def build_messages(retriever, question: str):
    documents = retriever.invoke(question)
    context = format_context(documents)
    messages = prompt.format_messages(context=context, question=question)
    return messages, documents


def generate_response(messages, model_name: str = "gemini-3.5-flash", temperature: float = 0.0):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set in environment")

    genai.configure(api_key=api_key)

    llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key, temperature=temperature)

    response = llm.invoke(messages)
    return response.content


def ask_question(retriever, question: str):
    messages, documents = build_messages(retriever, question)
    answer = generate_response(messages)

    sources = []
    seen = set()
    for doc in documents:
        source = Path(doc.metadata.get("source", "Unknown")).name
        page = doc.metadata.get("page", "N/A")
        ref = f"{source} (Page {page})"
        if ref not in seen:
            seen.add(ref)
            sources.append(ref)

    return {"question": question, "answer": answer, "sources": sources}
