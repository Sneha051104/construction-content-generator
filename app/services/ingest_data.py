from pathlib import Path
from app.services.vector_service import VectorService

DATA_DIR = Path("app/data/knowledge_base")


def load_documents():
    docs = []
    metas = []

    for file_path in DATA_DIR.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")
        chunks = [line.strip() for line in content.splitlines() if line.strip()]

        for idx, chunk in enumerate(chunks, start=1):
            docs.append(chunk)
            metas.append({
                "title": f"{file_path.stem.replace('_', ' ').title()} - Chunk {idx}",
                "source": file_path.name,
            })

    return docs, metas


if __name__ == "__main__":
    vector_service = VectorService()
    docs, metas = load_documents()
    vector_service.add_documents(docs, metas)
    print(f"Ingested {len(docs)} chunks successfully.")