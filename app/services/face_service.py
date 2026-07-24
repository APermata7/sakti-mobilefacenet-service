from typing import Tuple, Optional
from app.infrastructure.ml.model_loader import get_model
from app.utils.image_utils import download_image, cosine_similarity, validate_face_image
from app.core.config import settings
from app.utils.logger import log

class FaceService:
    
    def __init__(self):
        self._model = None
        self.threshold = settings.VERIFICATION_THRESHOLD
    
    @property
    def model(self):
        if self._model is None:
            log.info("Loading model (lazy)...")
            self._model = get_model()
            log.info("Model loaded successfully")
        return self._model
    
    def verify(self, reference_url: str, selfie_url: str) -> Tuple[bool, float, Optional[str]]:
        log.info(f"Memulai verifikasi wajah")
        
        try:
            log.debug("Mengunduh gambar referensi...")
            ref_img = download_image(reference_url)
            if ref_img is None:
                return False, 0.0, "Gagal mengunduh gambar referensi"
            
            log.debug("Mengunduh gambar selfie...")
            selfie_img = download_image(selfie_url)
            if selfie_img is None:
                return False, 0.0, "Gagal mengunduh gambar selfie"
            
            is_valid, msg = validate_face_image(ref_img)
            if not is_valid:
                return False, 0.0, f"Gambar referensi tidak valid: {msg}"
            
            is_valid, msg = validate_face_image(selfie_img)
            if not is_valid:
                return False, 0.0, f"Gambar selfie tidak valid: {msg}"
            
            log.debug("Ekstrak embedding referensi...")
            ref_emb = self.model.get_embedding(ref_img)
            if ref_emb is None:
                return False, 0.0, "Tidak ada wajah terdeteksi pada gambar referensi"
            
            log.debug("Ekstrak embedding selfie...")
            selfie_emb = self.model.get_embedding(selfie_img)
            if selfie_emb is None:
                return False, 0.0, "Tidak ada wajah terdeteksi pada gambar selfie"
            
            similarity = cosine_similarity(ref_emb, selfie_emb)
            match = similarity >= self.threshold
            
            log.info(f"Hasil verifikasi: cocok={match}, similarity={similarity:.4f}")
            
            return match, similarity, None
            
        except Exception as e:
            log.error(f"Error verifikasi: {e}")
            return False, 0.0, f"Error verifikasi: {str(e)}"