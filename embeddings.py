from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer

_model = None


def get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def embed_sentences(sentences: List[str]) -> np.ndarray:
    if not sentences:
        return np.zeros((0, 384), dtype=float)
    model = get_model()
    return model.encode(sentences, normalize_embeddings=True)
