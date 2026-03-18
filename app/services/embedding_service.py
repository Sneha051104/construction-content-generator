from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL


class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed_text(self, text: str):
        return self.model.encode(text).tolist()

    def embed_texts(self, texts: list[str]):
        return self.model.encode(texts).tolist()