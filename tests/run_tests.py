from tests.test_datasets import run as test_datasets
from tests.test_search import run as test_search
from tests.test_validator import run as test_validator
from tests.test_statistics import run as test_statistics
from tests.test_editor import run as test_editor


def main():
    print("\n=== ELLA TEST SUITE ===\n")

    test_datasets()
    test_search()
    test_validator()
    test_statistics()
    test_editor()

    print("\n=== HOTOVO ===\n")


if __name__ == "__main__":
    main()
