from typing import List, Dict, Any, Tuple

import numpy as np

from embeddings import embed_sentences
from parser import jd_sections_to_sentences, extract_candidate_bullets


def cosine_similarity_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    if a.size == 0 or b.size == 0:
        return np.zeros((a.shape[0], b.shape[0]), dtype=float)
    return np.matmul(a, b.T)


def rank_bullets_for_jd(
    jd_sections: Dict[str, List[str]],
    profile: Dict[str, Any],
    top_k: int = 10,
) -> List[Dict[str, Any]]:
    jd_sentences = jd_sections_to_sentences(jd_sections)
    bullet_entries = extract_candidate_bullets(profile)

    jd_texts = jd_sentences
    bullet_texts = [b["bullet"] for b in bullet_entries]

    jd_vecs = embed_sentences(jd_texts)
    bullet_vecs = embed_sentences(bullet_texts)

    sim_matrix = cosine_similarity_matrix(bullet_vecs, jd_vecs)
    max_sim_per_bullet = sim_matrix.max(axis=1) if sim_matrix.size > 0 else np.array([])

    scored_bullets: List[Tuple[float, Dict[str, Any]]] = []
    for idx, entry in enumerate(bullet_entries):
        score = float(max_sim_per_bullet[idx]) if max_sim_per_bullet.size > 0 else 0.0
        new_entry = dict(entry)
        new_entry["score"] = score
        scored_bullets.append((score, new_entry))

    scored_bullets.sort(key=lambda x: x[0], reverse=True)
    top_bullets = [e for _, e in scored_bullets[:top_k]]
    return top_bullets
