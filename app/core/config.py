import os
import json
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MODEL_NAME: str = os.getenv("MODEL_NAME", "buffalo_l")
    FACE_DET_SIZE: int = int(os.getenv("FACE_DET_SIZE", "640"))
    VERIFICATION_THRESHOLD: float = float(os.getenv("VERIFICATION_THRESHOLD", "0.65"))
    
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "5002"))
    RELOAD: bool = os.getenv("RELOAD", "false").lower() == "true"
    
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "logs/app.log")
    
    PROVIDERS: List[str] = json.loads(os.getenv("PROVIDERS", '["CPUExecutionProvider"]'))
    ALLOWED_ORIGINS: List[str] = json.loads(os.getenv("ALLOWED_ORIGINS", '["*"]'))

settings = Settings()