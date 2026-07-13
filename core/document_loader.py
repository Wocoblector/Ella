from pathlib import Path


DOCS_DIR = Path("docs")


def load_documents():
    """
    Načte všechny txt a md dokumenty.
    """

    documents = []

    for pattern in ("*.txt", "*.md"):

        for file in DOCS_DIR.glob(pattern):

            try:

                content = file.read_text(
                    encoding="utf-8"
                )

                documents.append({
                    "file": file.name,
                    "content": content,
                })

            except Exception:
                pass

    return documents
