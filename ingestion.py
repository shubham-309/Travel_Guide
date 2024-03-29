import os

from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone as pinedb
from pinecone import Pinecone


# initialize PineCone.
pc = Pinecone(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENV_REGION"],
)


# Function to put vector dataset in pinecone vector DB
def ingest_docs():
    INDEX_NAME = os.environ["INDEX_NAME"]
    print(INDEX_NAME)
    loader = DirectoryLoader("documents/2019", glob="**/*.pdf")
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents) }documents")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    documents = text_splitter.split_documents(documents=raw_documents)
    print(f"Splitted into {len(documents)} chunks")

    print(f"Going to add {len(documents)} to Pinecone")
    embeddings = OpenAIEmbeddings()
    pinedb.from_documents(documents, embeddings, index_name=INDEX_NAME)

    print("****Loading to vectorestore done ***")


# set Environment Variables and ingest Data on pinecone
if __name__ == "__main__":
    ingest_docs()
