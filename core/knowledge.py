from database.datasets import list_datasets
from database.search import search_text


def find_answer(message):
    """
    Pokusí se najít odpověď v datasetech.

    Vrací:
        response (str)
        nebo None
    """

    for dataset in list_datasets():

        results = search_text(
            dataset,
            message
        )

        if results:
            return results[0]["response"]

    return None
