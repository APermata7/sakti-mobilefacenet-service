from fastapi import APIRouter
from app.api.schemas.face import HealthResponse
from app.core.config import settings

router = APIRouter(tags=["Health"])

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="ok",
        service="mobilefacenet-service",
        version="1.0.0",
        model=settings.MODEL_NAME,
        threshold=settings.VERIFICATION_THRESHOLD,
        provider=settings.PROVIDERS[0] if settings.PROVIDERS else "CPU"
    )