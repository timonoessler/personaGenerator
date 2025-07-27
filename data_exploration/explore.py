import pandas as pd
import matplotlib.pyplot as plt

def explore_single(df: pd.DataFrame, key: str, meta: dict, color: str = 'C0'):
    codes  = list(meta['labels'].keys())
    labels = [meta['labels'][c] for c in codes]

    series = df[key].fillna(-99).astype(int)
    counts = series.value_counts().reindex(codes, fill_value=0)
    perc   = counts / counts.sum() * 100

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(labels, counts.values, color=color)
    ax.set_title(meta['text'])
    ax.set_ylabel('Anzahl')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    summary = pd.DataFrame({
        'Antwort': labels,
        'Anzahl':  counts.values,
        'Prozent': perc.round(1)
    })
    return fig, summary

def explore_multiple(df: pd.DataFrame, key: str, meta: dict, colors=('C0','C1','C2')):
    codes  = list(meta['labels'].keys())      
    labels = [meta['labels'][c] for c in codes]

    series = df[key].fillna(-99).astype(int)
    counts = series.value_counts().reindex(codes, fill_value=0)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(labels, counts.values, color=colors)
    ax.set_title(meta['text'])
    ax.set_ylabel('Anzahl')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    summary = pd.DataFrame({
        'Antwort': labels,
        'Anzahl':  counts.values
    })
    return fig, summary

def explore_freetext(df: pd.DataFrame, key: str, meta: dict, color='C0'):
    texts  = df[key].dropna().astype(str)
    counts = texts.value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.barh(counts.index[::-1], counts.values[::-1], color=color)
    ax.set_title(meta['text'] + ' (Top 10)')
    ax.set_xlabel('Häufigkeit')
    plt.tight_layout()

    summary = counts.rename('Anzahl').to_frame()
    return fig, summary
