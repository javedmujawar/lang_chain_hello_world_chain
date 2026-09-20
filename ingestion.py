import os

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeSparseVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain_unstructured import UnstructuredLoader

load_dotenv()


if __name__ == "__main__":
    print("Ingestion...")
    loader = UnstructuredLoader(
        file_path="./mediumblog1.txt", chunking_strategy="basic", max_characters=1000000
    )
    document = loader.load()
    print("Splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"Created {len(texts)} chunks")

    embeddings = OpenAIEmbeddings(openai_api_key= os.environ.get("OPENAI_API_KEY"))

    print("ingesting...")
    PineconeSparseVectorStore.from_documents(texts,embeddings,index_name=os.environ["INDEX_NAME"])
    print("Finish")