from database.datasets import (
    load_dataset,
    add_record,
    edit_record,
    delete_record,
)


def run():
    print("TEST: datasets.py")

    dataset = "test.jsonl"

    data_before = load_dataset(dataset)
    original_count = len(data_before)

    add_record(
        dataset,
        "Test instruction",
        "Test response"
    )

    data = load_dataset(dataset)

    assert len(data) == original_count + 1

    edit_record(
        dataset,
        len(data) - 1,
        "Edited instruction",
        "Edited response"
    )

    data = load_dataset(dataset)

    assert data[-1]["instruction"] == "Edited instruction"
    assert data[-1]["response"] == "Edited response"

    delete_record(
        dataset,
        len(data) - 1
    )

    data = load_dataset(dataset)

    assert len(data) == original_count

    print("PASS")


if __name__ == "__main__":
    run()
