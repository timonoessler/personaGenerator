import streamlit as st
from meta import question_meta
from data_loader import load_data, load_synth_json
from explore import explore_single, explore_multiple, explore_freetext

ORIG_PATH  = 'Koehler_Iselborn_Rohdatensatz_Zenodo.xlsx'
SYNTH_PATH = 'persona_beer_answers_regional.json'

df_orig = load_data(ORIG_PATH)
df_synth = load_synth_json(SYNTH_PATH)

st.set_page_config(layout='wide')
st.title("Fragebogen-Explorer Generation Z")
st.markdown("Vergleich: Original vs. Synthetische Personas")

# alle nicht-group keys
frage_keys = [k for k, m in question_meta.items() if m['type'] != 'group']

# Query-Params auslesen
params    = st.query_params
param_sel = params.get('selection', [None])[0]
if param_sel not in frage_keys:
    param_sel = frage_keys[0]
param_cmp = params.get('compare', ['true'])[0].lower() in ('1', 'true', 'yes')

# Sidebar
selection = st.sidebar.selectbox(
    "Frage wählen:",
    frage_keys,
    index=frage_keys.index(st.session_state.selection),
    format_func=lambda k: f"{k}: {question_meta[k]['text']}",
    key='selection'
)

if 'compare' not in st.session_state:
    cmp = params.get('compare', ['false'])[0].lower()
    st.session_state.compare = cmp in ['1', 'true', 'yes']

compare = st.sidebar.checkbox(
    "Vergleich mit Synthese",
    value=st.session_state.compare,
    key='compare'
)

meta = question_meta[selection]
if 'parent' in meta:
    parent = question_meta[meta['parent']]['text']
    st.markdown(f"### {meta['parent']} – {parent}")
    st.markdown(f"#### {selection} – {meta['text']}")
else:
    st.markdown(f"### {selection} – {meta['text']}")

orig_col, synth_col = st.columns(2)

with orig_col:
    st.subheader("Original")
    if meta['type'] == 'single':
        fig_o, summary_o = explore_single(df_orig, selection, meta)
    elif meta['type'] == 'multiple':
        fig_o, summary_o = explore_multiple(df_orig, selection, meta)
    else:
        fig_o, summary_o = explore_freetext(df_orig, selection, meta)
    st.pyplot(fig_o, use_container_width=True)
    st.markdown(summary_o.to_html(index=False), unsafe_allow_html=True)

with synth_col:
    if compare:
        st.subheader("Synthetisch")
        if meta['type'] == 'single':
            fig_s, summary_s = explore_single(df_synth, selection, meta, color='green')
        elif meta['type'] == 'multiple':
            fig_s, summary_s = explore_multiple(
                df_synth, selection, meta,
                colors=('green', 'lightgreen', 'gray')
            )
        else:
            fig_s, summary_s = explore_freetext(df_synth, selection, meta, color='green')
        st.pyplot(fig_s, use_container_width=True)
        st.markdown(summary_s.to_html(index=False), unsafe_allow_html=True)

# URL-Params immer synchronisieren
st.experimental_set_query_params(
    selection=[selection],
    compare=[str(compare).lower()]
)
