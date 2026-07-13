from database.datasets import (
    list_datasets,
    load_dataset,
    add_record,
    edit_record,
    delete_record,
)


def choose_dataset():
    """Vrátí název vybraného datasetu."""

    datasets = list_datasets()

    if not datasets:
        print("Žádné datasety.")
        return None

    print("\nDatasety:\n")

    for i, name in enumerate(datasets, 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("\nVyber dataset: "))
        return datasets[choice - 1]

    except Exception:
        print("Neplatná volba.")
        return None


def show_dataset(name):
    """Vypíše obsah datasetu."""

    data = load_dataset(name)

    if not data:
        print("\nDataset je prázdný.")
        return

    print()

    for i, item in enumerate(data, 1):
        print(f"[{i}]")
        print(f"Instruction: {item['instruction']}")
        print(f"Response   : {item['response']}")
        print("-" * 40)


def add_dialog():
    """Interaktivní přidání záznamu."""

    dataset = choose_dataset()

    if not dataset:
        return

    instruction = input("Instruction: ").strip()
    response = input("Response: ").strip()

    add_record(dataset, instruction, response)

    print("\n✔ Záznam přidán.")


def edit_dialog():
    """Interaktivní úprava záznamu."""

    dataset = choose_dataset()

    if not dataset:
        return

    show_dataset(dataset)

    try:
        index = int(input("\nČíslo záznamu: ")) - 1

        instruction = input("Nová instruction: ").strip()
        response = input("Nová response: ").strip()

        edit_record(dataset, index, instruction, response)

        print("\n✔ Záznam upraven.")

    except Exception as e:
        print(f"\nChyba: {e}")


def delete_dialog():
    """Interaktivní smazání záznamu."""

    dataset = choose_dataset()

    if not dataset:
        return

    show_dataset(dataset)

    try:
        index = int(input("\nČíslo záznamu: ")) - 1

        confirm = input("Opravdu smazat? (a/n): ").lower()

        if confirm == "a":
            delete_record(dataset, index)
            print("\n✔ Záznam smazán.")
        else:
            print("\nZrušeno.")

    except Exception as e:
        print(f"\nChyba: {e}")
