from database.datasets import load_dataset


def search_instruction(name, text):
    """Vyhledá podle instrukce."""
    text = text.lower()

    return [
        item
        for item in load_dataset(name)
        if text in item["instruction"].lower()
    ]


def search_response(name, text):
    """Vyhledá podle odpovědi."""
    text = text.lower()

    return [
        item
        for item in load_dataset(name)
        if text in item["response"].lower()
    ]


def search_text(name, text):
    """Vyhledá v instrukci i odpovědi."""
    text = text.lower()

    return [
        item
        for item in load_dataset(name)
        if (
            text in item["instruction"].lower()
            or text in item["response"].lower()
        )
    ]
