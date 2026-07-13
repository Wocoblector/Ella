# VERSION: 7

from core.knowledge import find_answer
from core.llm import ask
from core.facts import get_fact
from core.vector_search import search_vectors


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

        context = chunks[0]["chunk"]["content"]

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
