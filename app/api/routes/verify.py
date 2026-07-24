from fastapi import APIRouter, HTTPException, status
from app.api.schemas.face import (
    FaceVerificationRequest,
    FaceVerificationResponse
)
from app.services.face_service import FaceService
from app.core.config import settings
from app.utils.logger import log

router = APIRouter(prefix="/api/v1", tags=["Face Verification"])

face_service = FaceService()

@router.post("/verify", response_model=FaceVerificationResponse)
async def verify_faces(request: FaceVerificationRequest):
    try:
        match, similarity, error = face_service.verify(
            str(request.reference_url),
            str(request.selfie_url)
        )
        
        if error:
            return FaceVerificationResponse(
                success=False,
                match=False,
                similarity=0.0,
                threshold=settings.VERIFICATION_THRESHOLD,
                message=error
            )
        
        return FaceVerificationResponse(
            success=True,
            match=match,
            similarity=similarity,
            threshold=settings.VERIFICATION_THRESHOLD,
            message="Verifikasi berhasil"
        )
        
    except Exception as e:
        log.error(f"Endpoint verifikasi error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )