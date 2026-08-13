# AI-Powered Enterprise Document Assistant

A reproducible RAG (Retrieval-Augmented Generation) demo that processes enterprise PDFs, builds embeddings, stores them in ChromaDB and answers user questions using an LLM (Gemini / Google Generative AI).

This repository was packaged from a Colab notebook (original notebook retained separately). The original development and testing happened in Google Colab; this repo provides a modular, reproducible structure to run the pipeline locally.

Quick overview

Problem
  ↓
PDF Upload
  ↓
PDF Parsing
  ↓
Text Chunking
  ↓
Sentence Transformer Embeddings
  ↓
ChromaDB
  ↓
Semantic Retrieval
  ↓
Gemini (LLM)
  ↓
Context-Aware Answer

Getting started

1. Create a Python virtual environment (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Set your LLM API key as an environment variable (DO NOT commit your key):

```bash
set GEMINI_API_KEY=your_api_key_here
```

3. Place sample documents in `sample_data/` (or point to your own folder).

4. Run the Streamlit demo:

```bash
streamlit run app/streamlit_app.py
```

Notes
- The original Colab notebook used during development is available in your workspace. Before publishing, ensure no secrets are included in committed notebooks.
- This repo is a reproducible packaging of that Colab workflow into modular Python files and a small demo.

Contributing

- Move `RAG_repo/RAG_Project_2.ipynb` into `notebook/` if you want the full notebook included (sanitize API keys first).
