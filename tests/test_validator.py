from database.validator import validate_dataset


def run():
    print("TEST: validator.py")

    result = validate_dataset("test.jsonl")

    assert "json" in result
    assert "empty" in result
    assert "duplicates" in result

    print("PASS")


if __name__ == "__main__":
    run()
