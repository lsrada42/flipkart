from langchain_astradb import AstraDBVectorStore
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from dotenv import load_dotenv
import os
from flipkart import data_converter
from flipkart.data_converter import dataconverter

load_dotenv()

GROQ_API = os.getenv("GROQ_API")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
HF_TOKEN = os.getenv("HF_TOKEN")

embeddings = HuggingFaceInferenceAPIEmbeddings(api_key = HF_TOKEN, model_name = 'BAAI/bge-base-en-v1.5')

def data_ingestion(status):
    vstore = AstraDBVectorStore(
    embedding= embeddings,
    collection_name= "flipkart",
    api_endpoint = ASTRA_DB_API_ENDPOINT,
    token = ASTRA_DB_APPLICATION_TOKEN,
    namespace = ASTRA_DB_KEYSPACE
)
    storage = status
    
    if storage is None: 
        docs = dataconverter()
        insert_ids = vstore.add_documents(docs)
    else: 
        return vstore, []
    
    return vstore, insert_ids


if __name__ == "__main__":
    vstore, insert_ids = data_ingestion("skip")
    print(f"\n Inserted {len(insert_ids)} documents.")
    results = vstore.similarity_search("Can you tell me the low budget sound basshead?")
    for res in results: 
        print(f"\n {res.page_content} [{res.metadata}]")