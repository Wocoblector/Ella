# VERSION: 4

from core.document_chunks import get_chunks
from core.embeddings import embed

import numpy as np


CHUNK_CACHE = []


def cosine_similarity(a, b):

    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a)
        * np.linalg.norm(b)
    )


def build_cache():

    global CHUNK_CACHE

    if CHUNK_CACHE:
        return

    for chunk in get_chunks():

        CHUNK_CACHE.append({
            "chunk": chunk,
            "vector": embed(
                chunk["content"]
            )
        })


def search_vectors(query, top_k=10):

    build_cache()

    query_vector = embed(query)

    results = []

    for item in CHUNK_CACHE:

        score = cosine_similarity(
            query_vector,
            item["vector"]
        )

        results.append(
            {
                "score": float(score),
                "chunk": item["chunk"]
            }
        )

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:top_k]
