import os
import insightface
from insightface.app import FaceAnalysis
from typing import List
from app.core.config import settings
from app.utils.logger import log

class MobileFaceNetModel:
    
    def __init__(self):
        self.model_name = settings.MODEL_NAME
        self.det_size = settings.FACE_DET_SIZE
        self.providers = settings.PROVIDERS
        self.app = None
        self._load_model()
    
    def _load_model(self):
        try:
            log.info(f"Memuat model MobileFaceNet: {self.model_name}")
            log.info(f"Deteksi ukuran: {self.det_size}")
            log.info(f"Provider: {self.providers}")
            
            os.makedirs('models_data', exist_ok=True)
            
            self.app = FaceAnalysis(
                name=self.model_name,
                root='models_data',
                providers=self.providers
            )
            
            self.app.prepare(
                ctx_id=0,
                det_size=(self.det_size, self.det_size)
            )
            
            log.info("Model berhasil dimuat")
            
        except Exception as e:
            log.error(f"Gagal memuat model: {e}")
            raise RuntimeError(f"Gagal memuat InsightFace model: {e}")
    
    def get_embedding(self, image):
        try:
            faces = self.app.get(image)
            
            if not faces:
                log.warning("Tidak ada wajah terdeteksi dalam gambar")
                return None
            
            face = sorted(faces, key=lambda x: x.det_score, reverse=True)[0]
            embedding = face.embedding
            
            log.debug(f"Berhasil ekstrak embedding: {len(embedding)} dimensi")
            return embedding
            
        except Exception as e:
            log.error(f"Error mendapatkan embedding: {e}")
            return None
    
    def detect_faces(self, image) -> List:
        try:
            faces = self.app.get(image)
            log.debug(f"Ditemukan {len(faces)} wajah")
            return faces
        except Exception as e:
            log.error(f"Error mendeteksi wajah: {e}")
            return []

_model = None

def get_model() -> MobileFaceNetModel:
    global _model
    if _model is None:
        _model = MobileFaceNetModel()
    return _model