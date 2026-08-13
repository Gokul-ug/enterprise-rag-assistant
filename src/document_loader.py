from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader,
)

LOADER_MAPPING = {
    ".pdf": PyPDFLoader,
    ".docx": Docx2txtLoader,
    ".txt": TextLoader,
    ".md": TextLoader,
    ".csv": CSVLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".pptx": UnstructuredPowerPointLoader,
}


def load_documents(data_folder: str) -> List[Document]:
    """Load supported documents from `data_folder`."""

    data_path = Path(data_folder)
    documents = []

    if not data_path.exists():
        return documents

    for file_path in data_path.iterdir():
        if not file_path.is_file():
            continue

        extension = file_path.suffix.lower()

        if extension not in LOADER_MAPPING:
            print(f"Skipping unsupported: {file_path.name}")
            continue

        try:
            loader = LOADER_MAPPING[extension](str(file_path))
            docs = loader.load()
            documents.extend(docs)
            print(f"Loaded: {file_path.name}")
        except Exception as e:
            print(f"Error loading {file_path.name}: {e}")

    return documents
