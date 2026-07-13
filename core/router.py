# VERSION: 8

from core.knowledge import find_answer
from core.llm import ask
from core.facts import get_fact
from core.vector_search import search_vectors


MIN_RAG_SCORE = 0.30
MAX_CONTEXT_CHUNKS = 5


def route(message):
    """
    Rozhodne, odkud získat odpověď.
    """

    text = (
        message.lower()
        .strip()
        .replace("?", "")
    )

    if text in (
        "jak se jmenuji",
        "jak se jmenuju",
        "jaké je moje jméno",
    ):

        name = get_fact("name")

        if name:
            return {
                "source": "facts",
                "response": f"Jmenuješ se {name}."
            }

    response = find_answer(message)

    if response:
        return {
            "source": "database",
            "response": response
        }

    chunks = search_vectors(message)

    if chunks:

        best_score = chunks[0]["score"]

        if best_score >= MIN_RAG_SCORE:

            context_parts = []

            for item in chunks[:MAX_CONTEXT_CHUNKS]:

                if item["score"] < MIN_RAG_SCORE:
                    continue

                context_parts.append(
                    item["chunk"]["content"]
                )

            if context_parts:

                context = "\n\n".join(
                    context_parts
                )

                response = ask(
                    message,
                    context=context
                )

                return {
                    "source": "rag",
                    "response": response
                }

    response = ask(message)

    return {
        "source": "llm",
        "response": response
    }
