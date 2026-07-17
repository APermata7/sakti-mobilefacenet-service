import requests
import numpy as np
import cv2
from PIL import Image
import io
from typing import Optional, Tuple
from app.utils.logger import log

def download_image(url: str, timeout: int = 30) -> Optional[np.ndarray]:
    try:
        log.debug(f"Mengunduh gambar dari: {url}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        resp = requests.get(url, timeout=timeout, headers=headers)
        resp.raise_for_status()
        
        img = Image.open(io.BytesIO(resp.content))
        img = img.convert('RGB')
        
        img_np = np.array(img)
        img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        
        log.debug(f"Berhasil mengunduh gambar: {img_bgr.shape}")
        return img_bgr
        
    except requests.exceptions.RequestException as e:
        log.error(f"Gagal mengunduh gambar dari {url}: {e}")
        return None
    except Exception as e:
        log.error(f"Error memproses gambar: {e}")
        return None

def cosine_similarity(emb1: np.ndarray, emb2: np.ndarray) -> float:
    if emb1 is None or emb2 is None:
        return 0.0
    
    emb1 = emb1.flatten()
    emb2 = emb2.flatten()
    
    dot = np.dot(emb1, emb2)
    norm1 = np.linalg.norm(emb1)
    norm2 = np.linalg.norm(emb2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    return float(dot / (norm1 * norm2 + 1e-8))

def validate_face_image(image: np.ndarray) -> Tuple[bool, str]:
    if image is None:
        return False, "Gambar kosong (None)"
    
    if len(image.shape) != 3:
        return False, f"Gambar harus 3 channel, saat ini {len(image.shape)}"
    
    if image.shape[2] != 3:
        return False, f"Gambar harus RGB/BGR, saat ini {image.shape[2]}"
    
    h, w = image.shape[:2]
    if h < 20 or w < 20:
        return False, f"Gambar terlalu kecil: {w}x{h}"
    
    if h > 5000 or w > 5000:
        return False, f"Gambar terlalu besar: {w}x{h}"
    
    return True, "Valid"