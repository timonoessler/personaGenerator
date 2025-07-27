#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
clean_personas.py

Vereinheitlicht persona_beer_answers_regional.json:
- Entfernt persona_id
- Nutzt nur noch 'persona' als Namens-Feld
- Fasst 'answers' in 'responses' zusammen

Legt Input/Output-Defaults so, dass sie im gleichen Ordner wie das Skript liegen.
"""

import json
import argparse
import os

def parse_args():
    # Basis-Pfad = Ordner, in dem dieses Script liegt
    base = os.path.dirname(os.path.abspath(__file__))
    default_in  = os.path.join(base, "persona_beer_answers_regional.json")
    default_out = os.path.join(base, "persona_beer_answers_clean.json")

    p = argparse.ArgumentParser(description="Clean und unify Persona JSON")
    p.add_argument("-i", "--input",  default=default_in,
                   help="Pfad zur Original-JSON (default: im selben Ordner wie dieses Script)")
    p.add_argument("-o", "--output", default=default_out,
                   help="Pfad zur bereinigten JSON (default: im selben Ordner wie dieses Script)")
    return p.parse_args()

def main():
    args = parse_args()
    with open(args.input, encoding="utf-8") as f:
        data = json.load(f)

    cleaned = []
    for entry in data:
        # 1) Name vereinheitlichen
        name = entry.get("persona") or entry.get("name")
        # 2) Antworten vereinheitlichen
        responses = entry.get("responses") or entry.get("answers", {})
        # 3) Neues Objekt ohne persona_id und ohne name
        cleaned.append({
            "persona": name,
            "responses": responses
        })

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    print(f"✅ Bereinigte JSON geschrieben: {args.output}")

if __name__ == "__main__":
    main()
