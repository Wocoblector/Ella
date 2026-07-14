# ELLA PROJECT CONTEXT v2.1 (MASTER CONTEXT)

Tento dokument je sloučením původního PROJECT_CONTEXT v1.0 a novějších změn projektu.

## Stav projektu

Ella je lokální AI platforma vyvíjená v Pythonu.

Původně vznikla jako AI asistent, postupně se rozšířila o:

- Facts
- Memory
- Documents
- Embeddings
- Vector Search
- RAG
- Source Tracking
- Score Tracking
- Test Suite

## Architektonické principy

- Modulární architektura
- Jedna odpovědnost na modul
- Oddělení logiky od UI
- Preferovat jednoduchá řešení
- Zachovat dlouhodobou rozšiřitelnost

## Aktuální tok systému

Uživatel
↓
ella.py
↓
runtime.py
↓
router.py
↓
Facts / Database / RAG / LLM
↓
Odpověď

Priorita routeru:

1. Facts
2. Database
3. RAG
4. LLM

## Databázová vrstva

Dokončeno:

- datasets.py
- search.py
- validator.py
- statistics.py
- editor.py

## Core vrstva

Dokončeno:

- runtime.py
- router.py
- facts.py
- memory.py
- llm.py

## Facts

Schopnosti:

- ukládání faktů
- načítání faktů
- práce se jménem uživatele

Soubor:

data/memory/facts.json

## Memory

Schopnosti:

- ukládání historie
- načítání historie
- poslední zprávy po spuštění

Soubor:

data/memory/memory.json

## Dokumentový systém

Moduly:

- document_loader.py
- document_chunks.py

Schopnosti:

- načítání dokumentů
- chunking

## Embeddings

Použitá technologie:

- sentence-transformers

## Vector Search

Schopnosti:

- cosine similarity
- relevance scoring
- vyhledávání chunků

## RAG

Dokončeno:

- retrieval
- multi chunk retrieval
- source tracking
- score tracking

Výstup:

SOURCE: dokument

SCORE: relevance

## Testovací systém

Spouštění:

python -m tests.run_tests

Testované části:

- datasets
- search
- validator
- statistics
- editor
- rag

## Dokončené milníky

RAG-01 Dokumenty

RAG-02 Embeddings

RAG-03 Vector Search

RAG-04 Multi Chunk Retrieval

RAG-31 Source Tracking

RAG-32 Score Tracking

## Důležité zkušenosti

Při úpravách kódu vracet celý soubor.

Nevracet malé patche.

Pokud není znám aktuální obsah souboru, nejprve si jej vyžádat.

## TRAIN větev

TRAIN-01 Document → Dataset Generator

TRAIN-02 Dataset Review

TRAIN-03 Dataset Export

TRAIN-04 Training Runner

TRAIN-05 Model Registry

Dlouhodobý cíl:

Document → Dataset → Training → Model

## Budoucí oblasti

- Agent systém
- Planner
- Linux Tools
- Home Assistant
- Voice
- Vision
- GUI

## CHATGPT CONTINUATION PROMPT

- Odpovídej stručně
- Šetři tokeny
- 1 krok = 1 úkol
- Preferuj Python
- Předpokládej Linux
- Při úpravě vracej celý soubor
- Rozlišuj TERMINAL / PYTHON / PYTHON .VENV
- Na konci používej HOTOVO a stručný DALŠÍ KROK

## Instrukce pro nový GPT

1. Přečti PROJECT_CONTEXT.md
2. Přečti TREE_SNAPSHOT.txt
3. Zjisti aktuální stav projektu
4. Zachovej architekturu
5. Pokračuj od TRAIN-01

Konec dokumentu.
