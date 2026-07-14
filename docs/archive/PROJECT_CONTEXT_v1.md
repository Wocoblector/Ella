# ELLA PROJECT CONTEXT v1.0

> Tento dokument slouží jako hlavní technická dokumentace projektu Ella a zároveň jako kontext pro pokračování vývoje v novém ChatGPT chatu.

---

# 1. Přehled projektu

## Název projektu

Ella

## Typ projektu

Lokální AI asistent vyvíjený v Pythonu.

## Hlavní cíl

Vytvořit modulární AI systém, který bude možné dlouhodobě rozšiřovat bez nutnosti měnit jeho architekturu.

Ella není jednorázový program, ale platforma pro vývoj vlastního AI asistenta.

Projekt je navržen tak, aby běžel lokálně a aby jednotlivé části systému byly od sebe co nejvíce oddělené.

---

# 2. Dlouhodobá vize

Ella má být osobní AI asistent schopný:

* komunikovat v češtině,
* pracovat lokálně,
* využívat různé LLM modely,
* využívat datasety,
* používat paměť,
* plánovat úkoly,
* používat externí nástroje,
* pracovat s Linuxem,
* spolupracovat s Home Assistant,
* být dlouhodobě rozšiřitelná.

Cílem není vytvořit další chatbot.

Cílem je vytvořit vlastní AI platformu.

---

# 3. Filozofie projektu

Při návrhu projektu byly stanoveny následující zásady.

## Modularita

Každý modul má přesně definovanou odpovědnost.

Nikdy nebude jeden soubor řešit více různých problémů.

---

## Jedna odpovědnost

Každý modul řeší pouze jednu oblast.

Například:

* database pouze databázovou vrstvu,
* chat pouze komunikaci,
* runtime pouze běh systému,
* router pouze rozhodování,
* memory pouze práci s pamětí.

---

## Znovupoužitelnost

Moduly nesmí být závislé na konkrétním uživatelském rozhraní.

Stejný modul musí být možné použít:

* z terminálu,
* z GUI,
* z webového rozhraní,
* z API.

---

## Oddělení logiky

Logika programu nesmí být promíchaná s komunikací s uživatelem.

Například:

database/datasets.py

obsahuje pouze práci s daty.

database/editor.py

obsahuje pouze komunikaci s uživatelem.

---

## Postupný vývoj

Projekt nebude vytvářen najednou.

Nejdříve vznikne stabilní základ.

Teprve potom budou přidávány nové schopnosti.

---

# 4. Architektura systému

Ella používá vrstvenou architekturu.

Každá vrstva komunikuje pouze s vrstvou pod sebou.

Schéma:

Layer 1
UI / Chat

↓

Layer 2
Runtime

↓

Layer 3
Router

↓

Layer 4
Knowledge
LLM
Tools

↓

Layer 5
Memory

↓

Layer 6
Storage

Toto rozdělení je základním pravidlem celého projektu.

Vyšší vrstva nesmí obcházet nižší.

---

# 5. Aktuální struktura projektu

Projekt je aktuálně rozdělen přibližně takto:

config/
Nastavení projektu.

context/
Nástroje pro vytváření projektového kontextu.

core/
Hlavní logika systému.

database/
Databázová vrstva.

chat/
Komunikace.

data/
Všechna data projektu.

docs/
Dokumentace.

tester/
Pomocné nástroje.

tests/
Automatické testy.

tools/
Budoucí nástroje.

ella.py

Hlavní vstupní bod programu.

---

# 6. Stav projektu

Hotové:

* základ adresářové struktury,
* databázová vrstva,
* práce s JSONL datasety,
* vyhledávání,
* validace,
* statistiky,
* editor datasetů,
* testovací struktura.

Rozpracované:

* automatické testy,
* runtime,
* router,
* chat,
* memory,
* LLM,
* context exporter.

Neimplementované:

* agent,
* planner,
* Home Assistant,
* Linux tools,
* voice,
* vision,
* learning,
* GUI.

---

Konec části 1.


# 7. Popis jednotlivých modulů

## config/

Obsahuje globální konfiguraci projektu.

Příklady:

* cesty k adresářům,
* názvy modelů,
* výchozí nastavení,
* systémové konstanty.

Veškerá konfigurace projektu bude soustředěna zde.

---

## context/

Obsahuje nástroje pro práci s projektovým kontextem.

Účel:

* analyzovat projekt,
* vytvořit přehled projektu,
* exportovat kontext pro nový ChatGPT chat,
* kontrolovat správnost vytvořeného kontextu.

Plánované moduly:

* analyzer.py
* builder.py
* exporter.py
* validator.py

Budoucím cílem je, aby Ella dokázala vytvořit aktuální projektový kontext automaticky.

---

## core/

Obsahuje hlavní logiku systému.

Sem patří například:

* runtime,
* router,
* LLM komunikace,
* persona,
* práce s pamětí.

Core neobsahuje uživatelské rozhraní.

Core pouze řídí běh systému.

---

## database/

Databázová vrstva.

Je první dokončenou vrstvou projektu.

Obsahuje:

datasets.py

Práce s JSONL datasety.

Veřejné funkce:

* list_datasets()
* load_dataset()
* save_dataset()
* add_record()
* edit_record()
* delete_record()

---

search.py

Vyhledávání v datasetech.

Odpovědnost:

Vyhledávání záznamů.

---

validator.py

Kontrola datasetů.

Odpovědnost:

* validace,
* hledání chyb,
* kontrola duplicit.

---

statistics.py

Statistiky datasetů.

Například:

* počet datasetů,
* počet záznamů,
* statistiky projektu.

---

editor.py

Uživatelské rozhraní databázové vrstvy.

Obsahuje pouze komunikaci s uživatelem.

Neobsahuje logiku práce se soubory.

Využívá funkce z datasets.py.

---

## data/

Obsahuje všechna data projektu.

Například:

datasets/

JSONL datasety.

exports/

Exporty.

logs/

Logy.

memory/

Budoucí paměť.

models/

Lokální AI modely.

Veškerá data jsou oddělena od zdrojových kódů.

---

## chat/

Vrstva komunikace.

Odpovídá pouze za komunikaci s uživatelem.

Bude obsahovat:

* historii,
* správu relace,
* tvorbu odpovědi.

Chat nebude rozhodovat, odkud odpověď pochází.

To bude úkol routeru.

---

## tools/

Moduly umožňující Elle komunikovat s okolním světem.

Například:

* Linux,
* Home Assistant,
* internet,
* soubory,
* systémové nástroje.

Každý nástroj bude samostatný modul.

---

## tests/

Automatické testy projektu.

Každý hlavní modul bude mít vlastní test.

Například:

* test_datasets.py
* test_search.py
* test_validator.py
* test_statistics.py
* test_editor.py

Cílem je ověřit funkčnost projektu jedním příkazem.

---

# 8. Architektonická pravidla

Během vývoje byla stanovena následující pravidla.

1. Každý modul řeší jednu oblast.

2. Funkce nesmí být zbytečně duplikovány.

3. Logika musí být oddělena od uživatelského rozhraní.

4. Moduly musí být znovupoužitelné.

5. Nové funkce se přidávají pouze tehdy, pokud mají jasně definovanou odpovědnost.

6. Architektura má přednost před rychlým řešením.

7. Každá větší změna musí zachovat přehlednost projektu.

---

Konec části 2.

# 9. Aktuální stav projektu

Tento dokument popisuje stav projektu v okamžiku ukončení první etapy vývoje.

## Dokončené části

### Struktura projektu

Byla vytvořena základní adresářová struktura projektu.

Projekt je rozdělen na samostatné moduly s jasně definovanou odpovědností.

---

### Databázová vrstva

Dokončené moduly:

* database/datasets.py
* database/search.py
* database/validator.py
* database/statistics.py
* database/editor.py

Tyto moduly tvoří první stabilní vrstvu projektu.

---

### Testovací prostředí

Byl vytvořen adresář tests/.

Byla připravena struktura automatických testů.

Samotné testy budou doplněny v další etapě.

---

### Dokumentace

Byl založen dokument PROJECT_CONTEXT.md.

Od této chvíle představuje hlavní technickou dokumentaci projektu.

---

# 10. Nejbližší plán vývoje

Další vývoj bude pokračovat po jednotlivých etapách.

## Etapa 2

Dokončit databázovou vrstvu.

Úkoly:

* vytvořit automatické testy,
* vytvořit test runner,
* ověřit stabilitu všech databázových modulů.

Po dokončení bude databázová vrstva považována za uzavřenou.

---

## Etapa 3

Vybudovat Core.

Postupně implementovat:

* runtime,
* router,
* persona,
* memory,
* llm.

Cílem bude vytvořit funkční AI jádro.

---

## Etapa 4

Chat.

Napojení:

* runtime,
* router,
* databáze,
* LLM.

Vznikne první kompletní konverzační systém Elly.

---

## Etapa 5

Tools.

Budou přidávány jednotlivé nástroje.

Například:

* Linux,
* Home Assistant,
* práce se soubory,
* systémové příkazy.

---

## Etapa 6

Samostatnost.

Budoucí oblasti:

* plánování,
* učení,
* agent,
* dlouhodobá paměť,
* rozšiřování znalostí.

---

# 11. Pravidla vývoje

Při pokračování projektu musí být dodržována následující pravidla.

1. Zachovávat modulární architekturu.

2. Nepřesouvat odpovědnost mezi moduly bez důvodu.

3. Každý nový modul musí mít jasně definovanou úlohu.

4. Před implementací nejprve navrhnout architekturu.

5. Zdrojové kódy musí být čitelné a jednoduché.

6. Upřednostňovat dlouhodobě udržitelné řešení před rychlým řešením.

7. Po dokončení větší části aktualizovat PROJECT_CONTEXT.md.

8. Každý důležitý úkol označovat identifikátorem.

Používané prefixy:

* [ARCH]
* [DB]
* [CORE]
* [CHAT]
* [MEM]
* [LLM]
* [TOOLS]
* [CTX]
* [TEST]
* [BUG]
* [DOC]

---

# 12. Instrukce pro nový ChatGPT

Tento dokument slouží jako výchozí kontext.

Nový ChatGPT by měl:

* nejprve přečíst PROJECT_CONTEXT.md,
* pochopit architekturu projektu,
* pokračovat podle roadmapy,
* respektovat rozdělení odpovědností mezi moduly,
* nenavrhovat řešení, která porušují architekturu projektu.

Při úpravě zdrojových kódů není nutné znovu zasílat celý projekt.

Stačí zaslat:

* PROJECT_CONTEXT.md,
* soubor nebo modul, který se bude upravovat.

Projekt je navržen tak, aby jednotlivé moduly bylo možné upravovat samostatně.

---

# 13. Poznámka autora projektu

Projekt Ella je dlouhodobý projekt zaměřený na vytvoření vlastního modulárního AI asistenta.

Hlavním cílem není vytvořit pouze chatbota, ale stabilní platformu, kterou bude možné mnoho let rozšiřovat o nové schopnosti bez nutnosti měnit její základní architekturu.

Proto má návrh architektury, dokumentace a testování stejnou důležitost jako samotný zdrojový kód.

---

---

# 14. Doplňující projektové dokumenty

Tento dokument (`PROJECT_CONTEXT.md`) je hlavní dokumentace architektury projektu Ella.

Pro úplné pochopení aktuálního stavu projektu existují další doplňující dokumenty ve složce:

```text
docs/
```

## PROJECT_STATE.md

Obsahuje aktuální technický stav projektu.

Obsah:

* skutečný stav implementace,
* stav jednotlivých modulů,
* hotové a rozpracované části,
* poslední dokončené úkoly,
* další doporučený postup.

Při pokračování vývoje je doporučeno si tento dokument vyžádat a přečíst.

---

## TREE_SNAPSHOT.txt

Obsahuje aktuální fyzickou strukturu projektu.

Obsah:

* seznam složek,
* seznam souborů,
* aktuální organizace projektu.

Slouží ke kontrole rozdílu mezi navrženou architekturou a skutečným stavem projektu.

---

# Instrukce pro nový ChatGPT

Před zahájením dalšího vývoje:

1. Nejprve analyzuj tento dokument `PROJECT_CONTEXT.md`.

2. Pokud potřebuješ znát aktuální stav implementace, vyžádej si:

```text
docs/PROJECT_STATE.md
```

3. Pokud potřebuješ znát aktuální strukturu souborů, vyžádej si:

```text
docs/TREE_SNAPSHOT.txt
```

4. Nezačínej implementovat nové části, dokud není jasný aktuální stav projektu.

Tyto dokumenty společně tvoří základní kontext projektu Ella.

---

Konec dokumentace.




