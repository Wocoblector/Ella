from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

vector = model.encode(
    "Projekt Ella je lokální AI asistent."
)

print(len(vector))
