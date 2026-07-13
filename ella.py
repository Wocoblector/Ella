from core.runtime import (
    process_message,
    show_memory,
)


def show_last_messages(limit=6):
    """
    Zobrazí poslední zprávy.
    """

    history = show_memory()

    if not history:
        return

    print("\nPoslední zprávy:\n")

    for item in history[-limit:]:

        if item["role"] == "user":
            print(f"Ty: {item['content']}")

        elif item["role"] == "assistant":
            print(f"Ella: {item['content']}")

    print()


def main():

    show_last_messages()

    print("=" * 40)
    print("ELLA AI v1.0")
    print("=" * 40)

    while True:

        message = input("\nTy: ").strip()

        if not message:
            continue

        if message.lower() in (
            "konec",
            "exit",
            "quit",
        ):
            print("\nElla: Ukončuji.")
            break

        response = process_message(message)

        print(f"\nElla: {response}")


if __name__ == "__main__":
    main()
