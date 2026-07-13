from core.document_loader import load_documents


IGNORED_FILES = {
    "TREE_SNAPSHOT.txt",
}


def search_documents(text):

    words = text.lower().split()

    matches = []

    for document in load_documents():

        if document["file"] in IGNORED_FILES:
            continue

        lines = document["content"].splitlines()

        for line in lines:

            line = line.strip()

            if not line:
                continue

            line_lower = line.lower()

            score = 0

            for word in words:

                if word in line_lower:
                    score += 1

            if score > 0:

                matches.append(
                    (score, line)
                )

    matches.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        line
        for score, line in matches[:3]
    ]
