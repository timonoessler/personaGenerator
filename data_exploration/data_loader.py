import pandas as pd
import streamlit as st
from meta import question_meta
import json

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, na_values=[-99])
    df = df.fillna(-99)
    all_q = [c for c in df.columns if c.startswith('Q')]
    freetext_cols = ['Q3']
    numeric_q = [c for c in all_q if c not in freetext_cols]
    df[numeric_q] = df[numeric_q].astype('Int64')
    return df

@st.cache_data
def load_synth_json(path: str) -> pd.DataFrame:
    with open(path, encoding='utf-8') as f:
        personas = json.load(f)

    rows = []
    for persona_obj in personas:
        if len(persona_obj)==1 and list(persona_obj.keys())[0] != "persona":
            name, answers = next(iter(persona_obj.items()))
        elif "persona" in persona_obj:
            name = persona_obj["persona"]
            answers = {k: v for k,v in persona_obj.items() if k != "persona"}
        else:
            raise ValueError("Unbekanntes JSON-Format in load_synth_json")

        row = {}
        for frage_text, val in answers.items():
            num = frage_text.split()[1]
            if num == '3':
                row['Q3'] = val
                continue

            if isinstance(val, dict):
                if num == '17':
                    for sub_label, subv in val.items():
                        for col, meta in question_meta.items():
                            if col.startswith('Q17') and meta.get('text') == sub_label:
                                row[col] = int(subv) if isinstance(subv, (int,str)) and str(subv).isdigit() else -99
                                break
                    continue

                for subk, subv in val.items():
                    if subk.startswith('Situation'):
                        idx = int(subk.split()[1]) - 1
                    else:
                        idx = int(subk) - 1
                    letter = chr(ord('A') + idx)
                    col = f"Q{num}{letter}"
                    row[col] = int(subv) if isinstance(subv, (int,str)) and str(subv).isdigit() else -99

            else:
                col = f"Q{num}"
                row[col] = int(val) if isinstance(val, (int,str)) and str(val).lstrip('-').isdigit() else -99

        rows.append(row)

    df = pd.DataFrame(rows)

    for col, meta in question_meta.items():
        if col not in df.columns:
            df[col] = pd.NA if meta['type']=='freetext' else -99

    q_cols = [c for c,m in question_meta.items() if m['type']!='freetext']
    df[q_cols] = df[q_cols].astype('Int64')

    return df