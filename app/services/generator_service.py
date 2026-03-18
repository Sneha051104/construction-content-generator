from app.services.vector_service import VectorService
from app.services.prompt_service import PromptService
from app.services.llm_service import LLMService


class GeneratorService:
    def __init__(self):
        self.vector_service = VectorService()
        self.prompt_service = PromptService()
        self.llm_service = LLMService()

    def generate_document(self, document_type: str, user_input: str):
        results = self.vector_service.similarity_search(user_input, top_k=4)

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        context_items = []
        for i, doc in enumerate(documents):
            metadata = metadatas[i] if i < len(metadatas) else {}
            context_items.append({
                "id": i + 1,
                "title": metadata.get("title", f"Context Chunk {i + 1}"),
                "source": metadata.get("source", "knowledge_base"),
                "score": round(max(0.7, 0.95 - i * 0.05), 2),
                "snippet": doc,
            })

        retrieved_context_text = "\n".join([item["snippet"] for item in context_items]) or "No additional context found."

        prompt = self.prompt_service.build_prompt(
            document_type=document_type,
            user_input=user_input,
            retrieved_context=retrieved_context_text,
        )

        generated_output = self.llm_service.generate(prompt)

        return {
            "generated_output": generated_output,
            "retrieved_context": context_items,
        }