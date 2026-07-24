from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import health, verify
from app.core.config import settings
from app.utils.logger import log

app = FastAPI(
    title="MobileFaceNet Service",
    description="Layanan verifikasi wajah menggunakan MobileFaceNet dan InsightFace",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(verify.router)

@app.on_event("startup")
async def startup_event():
    log.info("Starting MobileFaceNet Service...")
    log.info(f"Model: {settings.MODEL_NAME}")
    log.info(f"Threshold: {settings.VERIFICATION_THRESHOLD}")
    log.info(f"Provider: {settings.PROVIDERS[0] if settings.PROVIDERS else 'CPU'}")

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down MobileFaceNet Service...")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )