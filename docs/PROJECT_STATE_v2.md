# ELLA PROJECT STATE v2.0

> Aktuální stav projektu Ella po implementaci paměti, faktů, dokumentů a první RAG vrstvy.

---

# 1. Základní informace

## Název projektu

Ella

## Verze

v2.0

## Typ projektu

Lokální modulární AI asistent vytvořený v Pythonu.

## Aktuální fáze

První funkční AI jádro.

Ella již disponuje:

* pamětí,
* fakty,
* znalostní databází,
* dokumentovým systémem,
* základním RAG,
* integrací Ollama.

---

# 2. Aktuální struktura projektu

## Core

```text
core/

├── chunk_search.py
├── document_chunks.py
├── document_loader.py
├── document_search.py
├── facts.py
├── knowledge.py
├── llm.py
├── memory.py
├── persona.py
├── router.py
└── runtime.py
```

## Data

```text
data/

├── datasets/
│   └── test.jsonl
│
└── memory/
    ├── facts.json
    └── memory.json
```

## Dokumentace

```text
docs/

├── PROJECT_CONTEXT.md
├── PROJECT_STATE.md
├── PROJECT_STATE_v2.md
└── test.txt
```

---

# 3. Implementované systémy

## Paměť

Stav:

✅ HOTOVO

Soubor:

```text
core/memory.py
```

Funkce:

* ukládání historie,
* načítání historie,
* mazání historie,
* persistentní ukládání.

Datový soubor:

```text
data/memory/memory.json
```

---

## Fakta

Stav:

✅ HOTOVO

Soubor:

```text
core/facts.py
```

Funkce:

* ukládání faktů,
* načítání faktů,
* přepis existujících hodnot.

Datový soubor:

```text
data/memory/facts.json
```

Příklad:

```json
{
    "name": "Pepa"
}
```

---

## Znalostní databáze

Stav:

✅ HOTOVO

Soubor:

```text
core/knowledge.py
```

Zdroj:

```text
data/datasets/test.jsonl
```

Funkce:

* vyhledávání připravených odpovědí,
* použití před LLM.

---

## Ollama

Stav:

✅ HOTOVO

Soubor:

```text
core/llm.py
```

Model:

```text
qwen2.5:3b
```

Funkce:

* komunikace s Ollama API,
* práce s historií,
* práce s kontextem.

---

# 4. Dokumentový systém

## Načítání dokumentů

Stav:

✅ HOTOVO

Soubor:

```text
core/document_loader.py
```

Podporované formáty:

```text
*.txt
*.md
```

---

## Chunks

Stav:

✅ HOTOVO

Soubor:

```text
core/document_chunks.py
```

Funkce:

* rozdělení dokumentů na odstavce,
* příprava dat pro RAG.

Aktuální počet chunků:

```text
278
```

---

## Vyhledávání

Stav:

✅ HOTOVO

Soubory:

```text
core/document_search.py
core/chunk_search.py
```

Funkce:

* hledání relevantních znalostí,
* skórování výsledků,
* vrácení nejlepších chunků.

---

# 5. Router

Stav:

✅ HOTOVO

Soubor:

```text
core/router.py
```

Rozhodovací logika:

```text
Facts
↓
Knowledge
↓
RAG
↓
LLM
```

---

# 6. RAG v1

Stav:

✅ HOTOVO

Implementováno:

```text
Dotaz
↓
Chunk Search
↓
Nejlepší odstavce
↓
Ollama Context
↓
Odpověď
```

Příklad:

```text
Ty:
Co je projekt Ella?

Ella:
Projekt Ella je lokální AI asistent...
```

---

# 7. Python prostředí

Stav:

✅ HOTOVO

Virtuální prostředí:

```text
.venv
```

Použití:

```bash
source .venv/bin/activate
```

---

# 8. Externí knihovny

## chromadb

Stav:

✅ NAINSTALOVÁNO

Účel:

Budoucí vektorová databáze.

---

## sentence-transformers

Stav:

🟡 PŘIPRAVUJE SE

Účel:

Generování embeddingů.

---

# 9. Roadmapa

## Dokončeno

```text
[MEM-01] Persistentní paměť
[FACT-01] Fakta
[DOC-01] Dokumenty
[DOC-02] Chunks
[DOC-03] Vyhledávání
[DOC-04] RAG v1
```

## Aktuálně

```text
[RAG-02]
Sentence Transformers
```

## Následuje

```text
[RAG-03]
Embeddingy

[RAG-04]
ChromaDB

[RAG-05]
Sémantické vyhledávání
```

---

# 10. Dlouhodobá vize

Ella má být schopna:

* komunikovat přirozeně,
* učit se z dokumentů,
* vytvářet projektový kontext,
* analyzovat vlastní projekt,
* používat nástroje,
* pracovat s Linuxem,
* využívat více AI modelů,
* dlouhodobě se rozšiřovat bez změny architektury.

---

Konec dokumentu

ELLA PROJECT STATE v2.0
