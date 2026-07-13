from pathlib import Path
import json

# Cesta k datasetům
DATASET_DIR = Path("data/datasets")


def list_datasets():
    """Vrátí seznam všech datasetů."""
    return sorted(file.name for file in DATASET_DIR.glob("*.jsonl"))


def load_dataset(name):
    """Načte dataset a vrátí seznam záznamů."""
    path = DATASET_DIR / name

    if not path.exists():
        return []

    data = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            data.append(json.loads(line))

    return data


def save_dataset(name, data):
    """Uloží celý dataset."""
    path = DATASET_DIR / name

    with open(path, "w", encoding="utf-8") as file:
        for record in data:
            file.write(
                json.dumps(record, ensure_ascii=False) + "\n"
            )


def add_record(name, instruction, response):
    """Přidá nový záznam."""
    data = load_dataset(name)

    data.append({
        "instruction": instruction,
        "response": response
    })

    save_dataset(name, data)


def edit_record(name, index, instruction, response):
    """Upraví záznam."""
    data = load_dataset(name)

    if 0 <= index < len(data):
        data[index]["instruction"] = instruction
        data[index]["response"] = response

        save_dataset(name, data)


def delete_record(name, index):
    """Smaže záznam."""
    data = load_dataset(name)

    if 0 <= index < len(data):
        del data[index]
        save_dataset(name, data)
