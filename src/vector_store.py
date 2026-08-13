from pathlib import Path
from langchain_chroma import Chroma


def get_vectorstore(documents=None, persist_directory: str = "./chroma_db", collection_name: str = "enterprise_documents", embedding_function=None):
    db_path = Path(persist_directory)

    if db_path.exists() and any(db_path.iterdir()):
        print("Loading existing ChromaDB...")
        return Chroma(persist_directory=persist_directory, embedding_function=embedding_function, collection_name=collection_name)

    print("Creating a new ChromaDB...")
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        persist_directory=persist_directory,
        collection_name=collection_name,
    )

    return vectorstore


def get_retriever(vectorstore, k: int = 5, fetch_k: int = 20):
    return vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": k, "fetch_k": fetch_k})
