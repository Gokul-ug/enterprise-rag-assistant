import os
from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model(model_name: str = None):
    model = model_name or os.environ.get("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

    return HuggingFaceEmbeddings(
        model_name=model,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
