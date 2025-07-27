# Data Exploration Generation Z

Interaktive Exploration eines Bier-Fragebogens (Köhler & Iselborn) für die Generation Z.  
Mit Streamlit-App zur Visualisierung von Original- und synthetischen Personas-Daten.

---

## Projektstruktur

data_exploration/
├── init.py
├── app.py
├── data_loader.py
├── explore.py
├── meta.py
├── Bierkonsum_GenZ_Antworten_generiert.csv
├── Koehler_Iselborn_Rohdatensatz_Zenodo.xlsx
├── requirements.txt
└── README.md

- **app.py**  
  Streamlit-Frontend, das Fragen aus `meta.py` lädt, Original- und Synthese-Datensätze per Checkbox vergleicht und Plots/Tables nebeneinander rendert.

- **data_loader.py**  
  Funktionen `load_data()` (Original-Excel) und `load_synth_data()` (synthetische CSV) zum Einlesen, NaN/`-99`-Handling, Label→Code-Mapping und Typ-Casting.

- **explore.py**  
  drei Explorer-Funktionen  
  - `explore_single()`: Single-Choice-Fragen  
  - `explore_multiple()`: Multiple-Choice (Ja/Nein)  
  - `explore_freetext()`: Freitext-Fragen (Top-10-Analyse)

- **meta.py**  
  `question_meta`-Dictionary mit allen Fragen (Q0–Q17E), Fragetexten, Antwort-Labels und Typ (single, multiple, freetext).

- **Koehler_Iselborn_Rohdatensatz_Zenodo.xlsx**  
  Originaler Rohdatensatz (536 Befragte, Q0–Q17E).

- **Bierkonsum_GenZ_Antworten_generiert.csv**  
  Synthetisch generierte Personas-Daten (100 Datensätze, gleiche Fragenstruktur).

- **requirements.txt**  
  Alle Python-Abhängigkeiten für das Projekt.

- **README.md**  
  Projektbeschreibung, Installations- und Bedienungsanleitung.

---

## Voraussetzungen

- Python 3.8+  
- Windows, macOS oder Linux  
- (optional) Virtuelle Umgebung (`venv` / `conda`)

---

## Installation

1. Repository klonen / in Projektordner wechseln  
   ```bash
   git clone <dein-repo-url>
   cd data_exploration

2. Virtuelle Umgebung erstellen und aktivieren

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate         # Windows PowerShell
   ```

3. Abhängigkeiten installieren
   ```bash
   pip install -r requirements.txt
   ```

4. Streamlit-App starten
   ```bash
   streamlit run app.py
   ```

### Bedienung
Frage auswählen
In der linken Sidebar wählst Du per Dropdown eine Frage (Q0–Q17E) aus.

Original- vs. Synthese-Vergleich
Mit Checkbox „Vergleich mit Synthese“ schaltest Du die Ansicht um:

Aus: Nur Original-Daten

An: Zwei Spalten, links Original, rechts synthetische Personas

Kennzahlen
Oben siehst Du “Gesamt valid” (Anzahl nicht--99) und “Keine Angabe” (Anzahl -99).

Visualisierung & Tabelle
Plot und Detail-Tabelle stehen nebeneinander, passend zu Fragetyp:

Single-Choice: Balkendiagramm

Multiple-Choice: Zwei Balken für Ja/Nein

Freitext: Top-10 horizontaler Balken

