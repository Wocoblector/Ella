import json
from pathlib import Path


FACTS_FILE = Path("data/memory/facts.json")

FACTS_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


def load_facts():

    if not FACTS_FILE.exists():
        return {}

    try:
        with open(
            FACTS_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except Exception:
        return {}


FACTS = load_facts()


def save_facts():

    with open(
        FACTS_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            FACTS,
            file,
            ensure_ascii=False,
            indent=2
        )


def set_fact(key, value):

    FACTS[key] = value

    save_facts()


def get_fact(key):

    return FACTS.get(key)


def get_all_facts():

    return FACTS
