from database.search import (
    search_instruction,
    search_response,
    search_text,
)


def run():
    print("TEST: search.py")

    dataset = "test.jsonl"

    result = search_instruction(
        dataset,
        "Python"
    )

    assert len(result) > 0

    result = search_response(
        dataset,
        "Programovací"
    )

    assert len(result) > 0

    result = search_text(
        dataset,
        "Python"
    )

    assert len(result) > 0

    print("PASS")


if __name__ == "__main__":
    run()
