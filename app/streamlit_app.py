import os
import streamlit as st
from pathlib import Path

from src.document_loader import load_documents
from src.chunking import split_documents
from src.embeddings import get_embedding_model
from src.vector_store import get_vectorstore, get_retriever
from src.rag_pipeline import ask_question

st.set_page_config(page_title='Enterprise Document Assistant')

DATA_FOLDER = os.environ.get('DATA_FOLDER', './sample_data')
VECTOR_DB = os.environ.get('VECTOR_DB', './chroma_db')

st.title('AI Enterprise Document Assistant')

st.markdown('Upload documents into `sample_data/` then build embeddings with the pipeline.')

if st.button('Preview sample files'):
    files = list(Path(DATA_FOLDER).glob('*'))
    st.write([f.name for f in files])

question = st.text_input('Ask a question about your documents')

if st.button('Ask'):
    try:
        embedding_fn = get_embedding_model()
        # Load vectorstore (assumes already indexed)
        vectorstore = get_vectorstore(persist_directory=VECTOR_DB, embedding_function=embedding_fn)
        retriever = get_retriever(vectorstore)

        result = ask_question(retriever, question)

        st.subheader('Answer')
        st.write(result['answer'])

        st.subheader('Sources')
        for s in result['sources']:
            st.write('-', s)

    except Exception as e:
        st.error(str(e))
        st.info('Make sure you set GEMINI_API_KEY and have an indexed ChromaDB.')
