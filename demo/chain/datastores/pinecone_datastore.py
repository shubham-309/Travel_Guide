import pinecone
from langchain.vectorstores import Pinecone as pinedb
from langchain.embeddings import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone
import os


def init_pinecone():
    print("Pinecone initiated")
    Pinecone(api_key=os.environ["PINECONE_API_KEY"],environment=os.environ["PINECONE_ENV_REGION"])


def get_pinecone_retriever():
    return pinedb.from_existing_index(
        index_name=os.environ["INDEX_NAME"], embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    )
