from fastapi import APIRouter
from app.models.request_models import GenerateRequest
from app.models.response_models import GenerateResponse
from app.services.generator_service import GeneratorService
from app.utils.text_utils import build_user_input

router = APIRouter()
generator_service = GeneratorService()


@router.get("/")
def health_check():
    return {"message": "Construction Content Generator API is running"}


@router.post("/generate", response_model=GenerateResponse)
def generate_content(payload: GenerateRequest):
    user_input = build_user_input(payload)

    return generator_service.generate_document(
        document_type=payload.document_type,
        user_input=user_input,
    )