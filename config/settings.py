"""App settings, read from environment variables (or a local .env file)."""
import os

from dotenv import load_dotenv

load_dotenv()

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "knowledge_base")
BOT_NAME = os.getenv("BOT_NAME", "Assistant")
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    f"You are {BOT_NAME}, a helpful assistant. Answer the question using the provided context. "
    "If the context does not contain the answer, say so.",
)
FALLBACK_REPLY = os.getenv("FALLBACK_REPLY", "I don't have any knowledge on that yet. Try another question.")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
