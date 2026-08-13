# AI-Powered Enterprise Document Assistant

A reproducible RAG (Retrieval-Augmented Generation) demo that processes enterprise PDFs, builds embeddings, stores them in ChromaDB and answers user questions using an LLM (Gemini / Google Generative AI).

This repository was packaged from a Colab notebook (original notebook retained separately). The original development and testing happened in Google Colab; this repo provides a modular, reproducible structure to run the pipeline locally.


## 📌 Key Highlights

✅ Enterprise document understanding  
✅ Retrieval-based question answering  
✅ Reduced hallucination through grounded generation  
✅ Persistent vector search  
✅ Explainable answers with references  

---

## 🏗️ Architecture

The system follows a complete RAG pipeline:

```text
                Documents
                    |
                    v
            Document Loaders
                    |
                    v
          Text Cleaning & Processing
                    |
                    v
              Semantic Chunking
                    |
                    v
              Embedding Model
                    |
                    v
          ChromaDB Vector Database
                    |
                    v
              MMR Retriever
                    |
                    v
             Prompt Engineering
                    |
                    v
              Gemini LLM
                    |
                    v
          Answer + Source References
```

---

## 📄 Features

### Multi-Format Document Support

Supports ingestion of multiple enterprise document formats:

- **PDF** - Portable Document Format
- **DOCX** - Microsoft Word Documents
- **TXT** - Plain Text Files
- **CSV** - Comma Separated Values
- **XLSX** - Excel Spreadsheets
- **PPTX** - PowerPoint Presentations

---

## Getting Started

### Prerequisites

- Python 3.8+
- Google Generative AI API Key

### Installation

1. **Create a Python virtual environment** (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. **Set your LLM API key** as an environment variable (DO NOT commit your key):

```bash
set GEMINI_API_KEY=your_api_key_here
```

3. **Place sample documents** in `sample_data/` or point to your own folder.

4. **Run the Streamlit demo**:

```bash
streamlit run app/streamlit_app.py
```

---

## 📝 Notes

- The original Colab notebook used during development is available in your workspace. Before publishing, ensure no secrets are included in committed notebooks.
- This repo is a reproducible packaging of that Colab workflow into modular Python files and a small demo.

---

## 🤝 Contributing

- Move `RAG_repo/RAG_Project_2.ipynb` into `notebook/` if you want the full notebook included (sanitize API keys first).

