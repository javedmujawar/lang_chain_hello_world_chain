import os

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeSparseVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain_unstructured import UnstructuredLoader

load_dotenv()


if __name__ == "__main__":
    print("Ingestion...")
    print(os.environ['PINECONE_API_KEY'])