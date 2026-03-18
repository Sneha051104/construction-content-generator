from pydantic import BaseModel
from typing import List


class ContextItem(BaseModel):
    id: int
    title: str
    source: str
    score: float
    snippet: str


class GenerateResponse(BaseModel):
    generated_output: str
    retrieved_context: List[ContextItem]