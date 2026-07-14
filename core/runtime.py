# VERSION: 4

from core.router import route
from core.memory import (
    add_message,
    get_history,
)
from core.facts import set_fact


def process_message(message):
    """
    Zpracuje zprávu uživatele.
    """

    text = message.strip()
    lower_text = text.lower()

    if lower_text.startswith("jmenuji se "):
        name = text[11:].strip()

        if name:
            set_fact(
                "name",
                name
            )

    add_message(
        "user",
        message
    )

    result = route(message)

    response = result["response"]

    score_text = ""

    if result["source"] == "rag":

        source_text = result.get(
            "document",
            "unknown"
        )

        score_text = (
            f"\nSCORE: "
            f"{result.get('score', 0)}"
        )

    else:
        source_text = result["source"]

    add_message(
        "assistant",
        response
    )

    return (
        f"{response}\n\n"
        f"SOURCE: {source_text}"
        f"{score_text}"
    )


def show_memory():
    """
    Vrátí historii konverzace.
    """

    return get_history()
