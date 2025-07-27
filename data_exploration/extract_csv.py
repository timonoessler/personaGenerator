#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_csv.py

Liest persona_beer_answers_regional.json ein und schreibt alle Personas mit
allen einzelnen Antwort-Merkmalen in eine CSV und zusätzlich in eine Excel-Datei.
Unterstützt Single-Value-, Text- und verschachtelte Dict-Antworten; wandelt
Sub-Keys sauber in Excel-taugliche Spaltennamen um.
"""

import json
import re
import argparse
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(
        description="JSON mit Persona-Antworten in CSV und XLSX umwandeln"
    )
    parser.add_argument(
        "-i", "--input",
        default="persona_beer_answers_regional.json",
        help="Pfad zur Input-JSON-Datei"
    )
    parser.add_argument(
        "-o", "--output",
        default="beer_responses_clean.csv",
        help="Pfad zur Ausgabedatei (CSV). XLSX wird automatisch mit gleicher Basis angelegt."
    )
    return parser.parse_args()


def sanitize_subkey(s: str) -> str:
    """
    Ersetzt alle Nicht-Wort-Zeichen (inkl. Leerzeichen, Slash, Kommas etc.)
    durch Unterstrich, so dass die Spalte Excel-tauglich wird.
    """
    return re.sub(r"[^\w]", "_", s)


def sort_key(col: str):
    """
    Sortiert Spalten so, dass:
      1. nach Frage-Nummer (Frage 1 vor Frage 2 …)
      2. numerische Sub-Keys in aufsteigender Zahl
      3. alphabetische Sub-Keys
      4. alle sonstigen Spalten am Ende
    """
    m = re.match(r"Frage (\d+)(?:_(.*))?$", col)
    if m:
        qnum = int(m.group(1))
        sub = m.group(2) or ""
        if sub.isdigit():
            return (qnum, 0, int(sub))
        else:
            return (qnum, 1, sub.lower())
    else:
        return (float("inf"), 0, col.lower())


def main():
    args = parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    cols_set = set()
    for persona_entry in data:
        responses = persona_entry.get("responses", {})
        for question, answer in responses.items():
            if isinstance(answer, dict):
                for subkey in answer:
                    safe = sanitize_subkey(subkey)
                    cols_set.add(f"{question}_{safe}")
            else:
                cols_set.add(question)

    all_columns = ["persona"] + sorted(cols_set, key=sort_key)

    rows = []
    for persona_entry in data:
        row = {c: "" for c in all_columns}
        row["persona"] = persona_entry.get("persona", "")
        for question, answer in persona_entry.get("responses", {}).items():
            if isinstance(answer, dict):
                for subkey, value in answer.items():
                    col = f"{question}_{sanitize_subkey(subkey)}"
                    row[col] = value
            else:
                row[question] = answer
        rows.append(row)

    df = pd.DataFrame(rows, columns=all_columns)

    print("Erkannte Spalten:", all_columns)

    df.to_csv(args.output, index=False, encoding="utf-8")
    print(f"✅ CSV geschrieben: {args.output}")

    xlsx_path = re.sub(r"\.csv$", ".xlsx", args.output, flags=re.IGNORECASE)
    df.to_excel(xlsx_path, index=False)
    print(f"✅ XLSX geschrieben: {xlsx_path}")


if __name__ == "__main__":
    main()
