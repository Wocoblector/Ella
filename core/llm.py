# VERSION: 4

import requests

from core.persona import PERSONA
from core.memory import get_history


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:7b"


def ask(prompt, context=""):
    """
    Pošle dotaz do Ollamy s personou,
    historií a dokumentovým kontextem.
    """

    history = get_history()

    conversation = ""

    for item in history[-10:]:

        if item["role"] == "user":
            conversation += (
                f"Uživatel: {item['content']}\n"
            )

        elif item["role"] == "assistant":
            conversation += (
                f"Ella: {item['content']}\n"
            )

    full_prompt = f"""
{PERSONA}

DŮLEŽITÉ:

Pokud KONTEXT obsahuje odpověď:

- odpověz pouze podle KONTEXTU
- cituj informace z KONTEXTU
- nepřeformulovávej
- nevytvářej shrnutí
- nevymýšlej nové informace
- pokud je v KONTEXTU seznam, vrať seznam

Nevymýšlej vlastní fakta.

Pokud kontext obsahuje odpověď,
má přednost před tvými znalostmi.

KONTEXT:

{context}

HISTORIE:

{conversation}

Uživatel:
{prompt}

Ella:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": full_prompt,
            "stream": False,
        },
        timeout=120,
    )

    response.raise_for_status()

    data = response.json()

    return data["response"].strip()
