# VERSION: 4

from core.document_loader import load_documents


IGNORED_FILES = {
    "TREE_SNAPSHOT.txt",
}


def get_chunks():

    chunks = []

    for document in load_documents():

        if document["file"] in IGNORED_FILES:
            continue

        current_chunk = []

        for line in document["content"].splitlines():

            if line.startswith("#") and current_chunk:

                text = "\n".join(
                    current_chunk
                ).strip()

                if len(text) >= 20:

                    chunks.append({
                        "file": document["file"],
                        "content": text,
                    })

                current_chunk = []

            current_chunk.append(line)

        if current_chunk:

            text = "\n".join(
                current_chunk
            ).strip()

            if len(text) >= 20:

                chunks.append({
                    "file": document["file"],
                    "content": text,
                })

    return chunks
