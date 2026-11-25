"""
Handles ChromaDB knowledge base management.
"""
import os
import logging
import chromadb
from sentence_transformers import SentenceTransformer
from config.settings import CHROMA_DB_PATH, COLLECTION_NAME, FALLBACK_REPLY


# Logging Setup
logging.basicConfig(level=logging.INFO)

# Ensure ChromaDB directory exists
os.makedirs(CHROMA_DB_PATH, exist_ok=True)

# Initialize ChromaDB Client
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chroma_client.get_or_create_collection(COLLECTION_NAME)

# Load Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Functions for Knowledge Base Management
def add_knowledge(id: str, text: str, metadata: dict):
    """
    Adds (or overwrites) a knowledge entry in ChromaDB.
    """
    try:
        embedding = model.encode(text).tolist()
        collection.upsert(
            ids=[id],
            documents=[text],
            metadatas=[metadata],
            embeddings=[embedding]
        )
        logging.info(f"✅ Knowledge added with ID: {id}")
        return {"message": f"✅ Knowledge added with ID: {id}"}
    except Exception as e:
        logging.error(f"❌ Failed to add knowledge: {str(e)}")
        return {"error": f"❌ Failed to add knowledge: {str(e)}"}

def update_knowledge(id: str, new_text: str, new_metadata: dict):
    """
    Updates an existing knowledge entry in ChromaDB.
    """
    delete_knowledge(id)  # Remove old entry
    return add_knowledge(id, new_text, new_metadata)

def delete_knowledge(id: str):
    """
    Deletes a knowledge entry from ChromaDB.
    """
    try:
        collection.delete(ids=[id])
        logging.info(f"🗑️ Knowledge with ID {id} deleted.")
        return {"message": f"🗑️ Knowledge with ID {id} deleted."}
    except Exception as e:
        logging.error(f"❌ Failed to delete knowledge: {str(e)}")
        return {"error": f"❌ Failed to delete knowledge: {str(e)}"}

def query_knowledge(query_text: str, n_results: int = 3):
    """
    Retrieves the most relevant knowledge from ChromaDB.
    """
    try:
        logging.debug(f"🟢 Querying ChromaDB for: {query_text}")
        embedding = model.encode(query_text).tolist()
        results = collection.query(query_embeddings=[embedding], n_results=n_results)
        logging.debug(f"🔍 ChromaDB Query Results: {results}")

        if results.get("documents") and results["documents"][0]:
            return results["documents"][0]  # Top n_results documents, most relevant first

        logging.warning("⚠️ No relevant knowledge found.")
        return FALLBACK_REPLY
    except Exception as e:
        logging.error(f"❌ Query Error: {str(e)}")
        return {"error": f"❌ Failed to query knowledge: {str(e)}"}
