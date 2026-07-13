from pathlib import Path

from database.datasets import load_dataset

DATASET_DIR = Path("data/datasets")


def dataset_stats(name):
    """Vrátí statistiky jednoho datasetu."""

    data = load_dataset(name)

    return {
        "dataset": name,
        "records": len(data),
        "instructions": len(
            [x for x in data if x.get("instruction", "").strip()]
        ),
        "responses": len(
            [x for x in data if x.get("response", "").strip()]
        )
    }


def project_stats():
    """Vrátí statistiky všech datasetů."""

    result = {
        "datasets": 0,
        "records": 0
    }

    for file in DATASET_DIR.glob("*.jsonl"):
        result["datasets"] += 1
        result["records"] += len(load_dataset(file.name))

    return result
