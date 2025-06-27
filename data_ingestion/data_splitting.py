from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List

def split_documents(docs: List[Document]) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size = 100,
        chunk_overlap = 20
    )

    return splitter.split_documents(docs)