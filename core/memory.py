import json
from pathlib import Path


MEMORY_FILE = Path("data/memory/memory.json")

MEMORY_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


def load_memory():
    """
    Načte paměť ze souboru.
    """

    if not MEMORY_FILE.exists():
        return []

    try:
        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except Exception:
        return []


MEMORY = load_memory()


def save_memory():
    """
    Uloží paměť do souboru.
    """

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            MEMORY,
            file,
            ensure_ascii=False,
            indent=2
        )


def add_message(role, content):
    """
    Přidá zprávu do paměti.
    """

    MEMORY.append({
        "role": role,
        "content": content
    })

    save_memory()


def get_history():
    """
    Vrátí historii.
    """

    return MEMORY


def clear_memory():
    """
    Vymaže paměť.
    """

    MEMORY.clear()

    save_memory()
