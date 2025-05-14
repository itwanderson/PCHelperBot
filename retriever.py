import chromadb
from sentence_transformers import SentenceTransformer
from utils.chunker import chunk_pdf
import os

# Initialize client with persistence
client = chromadb.PersistentClient(path="./db/chromadb")
collection = client.get_or_create_collection(name="pc_manuals")

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def index_documents():
    folder = "data/manuals/"
    try:
        for filename in os.listdir(folder):
            if filename.endswith(".pdf"):
                filepath = os.path.join(folder, filename)
                chunks = chunk_pdf(filepath)
                embeddings = embedder.encode(chunks).tolist()
                for idx, embedding in enumerate(embeddings):
                    collection.add(
                        documents=[chunks[idx]],
                        embeddings=[embedding],
                        metadatas=[{"source": filename}],
                        ids=[f"{filename}_{idx}"]
                    )
        client.persist()
    except Exception as e:
        print(f"Error during indexing: {e}")

def search(query, top_k=5):
    query_embedding = embedder.encode([query])[0].tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas"]
    )
    return results
