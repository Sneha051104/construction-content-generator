from huggingface_hub import InferenceClient
from app.config import HF_TOKEN, HF_MODEL, HF_PROVIDER


class LLMService:
    def __init__(self):
        if not HF_TOKEN:
            raise ValueError("HF_TOKEN is missing in .env")
        if not HF_MODEL:
            raise ValueError("HF_MODEL is missing in .env")

        if HF_PROVIDER and HF_PROVIDER.lower() != "auto":
            self.client = InferenceClient(
                provider=HF_PROVIDER,
                api_key=HF_TOKEN,
            )
        else:
            self.client = InferenceClient(
                api_key=HF_TOKEN,
            )

    def generate(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model=HF_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional assistant for construction documentation. Write formal, structured, concise reports."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=700,
            temperature=0.4,
        )

        return completion.choices[0].message.content.strip()