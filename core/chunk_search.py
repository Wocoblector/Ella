from core.document_chunks import get_chunks


def search_chunks(text):

    words = text.lower().split()

    matches = []

    for chunk in get_chunks():

        score = 0

        content = chunk["content"].lower()

        for word in words:

            if word in content:
                score += 1

        if score > 0:

            matches.append(
                (score, chunk)
            )

    matches.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        chunk
        for score, chunk in matches[:3]
    ]
