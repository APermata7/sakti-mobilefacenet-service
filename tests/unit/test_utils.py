import pytest
import numpy as np
from app.utils.image_utils import cosine_similarity, validate_face_image

class TestUtils:
    
    def test_cosine_similarity_identical(self):
        emb1 = np.array([1.0, 0.0, 0.0])
        emb2 = np.array([1.0, 0.0, 0.0])
        sim = cosine_similarity(emb1, emb2)
        assert sim == 1.0
    
    def test_cosine_similarity_orthogonal(self):
        emb1 = np.array([1.0, 0.0, 0.0])
        emb2 = np.array([0.0, 1.0, 0.0])
        sim = cosine_similarity(emb1, emb2)
        assert sim == 0.0
    
    def test_cosine_similarity_none(self):
        sim = cosine_similarity(None, np.array([1.0, 0.0]))
        assert sim == 0.0
    
    def test_validate_face_image_valid(self):
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        is_valid, msg = validate_face_image(img)
        assert is_valid is True
        assert msg == "Valid"
    
    def test_validate_face_image_none(self):
        is_valid, msg = validate_face_image(None)
        assert is_valid is False
        assert "None" in msg
    
    def test_validate_face_image_small(self):
        img = np.zeros((10, 10, 3), dtype=np.uint8)
        is_valid, msg = validate_face_image(img)
        assert is_valid is False
        assert "kecil" in msg