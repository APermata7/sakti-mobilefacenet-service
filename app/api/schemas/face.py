from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List

class FaceVerificationRequest(BaseModel):
    reference_url: HttpUrl = Field(..., description="URL foto referensi")
    selfie_url: HttpUrl = Field(..., description="URL foto selfie")
    
    class Config:
        json_schema_extra = {
            "example": {
                "reference_url": "https://res.cloudinary.com/example/reference.jpg",
                "selfie_url": "https://res.cloudinary.com/example/selfie.jpg"
            }
        }

class FaceVerificationResponse(BaseModel):
    success: bool
    match: bool
    similarity: float
    threshold: float
    message: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "match": True,
                "similarity": 0.85,
                "threshold": 0.70,
                "message": "Verifikasi berhasil"
            }
        }

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    model: str
    threshold: float
    provider: str