import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN", "")
HF_MODEL = os.getenv("HF_MODEL", "")
HF_PROVIDER = os.getenv("HF_PROVIDER", "hf-inference")

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "chroma_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "construction_knowledge")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")