# VERSION: 2

from sentence_transformers import SentenceTransformer


MODEL_NAME = (
    "paraphrase-multilingual-MiniLM-L12-v2"
)

_model = None


def get_model():

    global _model

    if _model is None:

        _model = SentenceTransformer(
            MODEL_NAME
        )

    return _model


def embed(text):

    model = get_model()

    return model.encode(text)
