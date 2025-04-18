
import requests
from bs4 import BeautifulSoup
from app.utils.helpers import chunk_text
from app.services.embedding import get_openai_embedding
import chromadb

# Chroma setup
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="rag_collection")

def extract_text_from_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = "\n".join([p.get_text() for p in paragraphs])
    return text

def store_in_vector_db(url: str):
    text = extract_text_from_url(url)
    chunks = chunk_text(text)
    embeddings = get_openai_embedding(chunks)

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            ids=[f"{url}-{i}"],
            embeddings=[embedding],
            metadatas=[{"source": url, "chunk_id": i}],
            documents=[chunk]
        )