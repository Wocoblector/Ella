from core.document_chunks import get_chunks
from core.vector_search import search_vectors


def run():
    print("TEST: rag")

    chunks = get_chunks()

    assert len(chunks) > 0

    results = search_vectors(
        "Co je projekt Ella?"
    )

    assert len(results) > 0

    assert results[0]["score"] > 0

    print("PASS")


if __name__ == "__main__":
    run()
