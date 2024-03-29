from chain.datastores.pinecone_datastore import *


def init_datastore(type):
    match type:
        case "Pinecone":
            init_pinecone()
            return


def get_retriever(type):
    match type:
        case "Pinecone":
            return get_pinecone_retriever()
