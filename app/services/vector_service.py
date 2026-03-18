import chromadb
from app.config import CHROMA_DB_PATH, COLLECTION_NAME
from app.services.embedding_service import EmbeddingService


class VectorService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME)

    def add_documents(self, documents: list[str], metadatas: list[dict]):
        if not documents:
            return

        existing_count = self.collection.count()
        ids = [f"doc_{existing_count + i}" for i in range(len(documents))]
        embeddings = self.embedding_service.embed_texts(documents)

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings,
        )

    def similarity_search(self, query: str, top_k: int = 4):
        if self.collection.count() == 0:
            return {"documents": [[]], "metadatas": [[]]}

        query_embedding = self.embedding_service.embed_text(query)

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )