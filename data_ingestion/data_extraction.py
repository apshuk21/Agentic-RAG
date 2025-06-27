from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from typing import List

def get_web_loaders(urls: List[str]):
    return [WebBaseLoader(url) for url in urls]

def get_extracted_data(urls: List[str]) -> List[Document]:
    docs = [loader.load() for loader in get_web_loaders(urls)]
    return [doc for sub_docs in docs for doc in sub_docs]