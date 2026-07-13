from database.statistics import (
    dataset_stats,
    project_stats,
)


def run():
    print("TEST: statistics.py")

    ds = dataset_stats("test.jsonl")

    assert "records" in ds

    pr = project_stats()

    assert "datasets" in pr
    assert "records" in pr

    print("PASS")


if __name__ == "__main__":
    run()
