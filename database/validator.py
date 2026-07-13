import json
from pathlib import Path

from database.datasets import load_dataset

DATASET_DIR = Path("data/datasets")


def validate_json(name):
    """Ověří, že je dataset validní JSONL."""
    path = DATASET_DIR / name

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    json.loads(line)

        return True, "JSON je v pořádku."

    except Exception as e:
        return False, str(e)


def validate_empty(name):
    """Najde prázdné instruction nebo response."""
    problems = []

    for index, item in enumerate(load_dataset(name)):
        if not item.get("instruction", "").strip():
            problems.append(f"Řádek {index+1}: prázdná instruction")

        if not item.get("response", "").strip():
            problems.append(f"Řádek {index+1}: prázdná response")

    return problems


def validate_duplicates(name):
    """Najde duplicitní instrukce."""
    seen = {}
    duplicates = []

    for index, item in enumerate(load_dataset(name)):
        instruction = item["instruction"].strip().lower()

        if instruction in seen:
            duplicates.append(
                f"Řádky {seen[instruction]+1} a {index+1}: '{item['instruction']}'"
            )
        else:
            seen[instruction] = index

    return duplicates


def validate_dataset(name):
    """Spustí všechny kontroly."""

    result = {}

    result["json"] = validate_json(name)
    result["empty"] = validate_empty(name)
    result["duplicates"] = validate_duplicates(name)

    return result
