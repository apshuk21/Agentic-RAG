from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from uuid import uuid4
from typing import List

def get_embeddings(model: str):
    return OpenAIEmbeddings(model=model)

def get_chroma_vector_store():
    return Chroma(
        collection_name='trade_war_collection',
        embedding_function=get_embeddings('text-embedding-3-large'),
        persist_directory='./chroma_langchain_db'
    )

def add_documents_to_store(docs: List[Document]):
    vector_store = get_chroma_vector_store()
    uuids = [str(uuid4()) for _ in range(len(docs))]

    vector_store.add_documents(documents=docs, ids=uuids)

    return vector_store.as_retriever(
        search_type="mmr", search_kwargs={"k": 5, "fetch_k": 10}
    )
