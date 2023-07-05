import streamlit as st

st.markdown("## NIHSS")
st.markdown("# Calculates the NIH Stroke Scale for quantifying stroke severity.")

mapping1A = {
    'Alert; keenly responsive': 0,
    'Arouses to minor stimulation': 1,
    'Requires repeated stimulation to arouse': 2,
    'Movements to pain': 3,
    'Postures or unresponsive': 4
}

mapping1B = {
    'Both questions right': 0,
    '1 question right': 1,
    '0 questions right': 2,
    'Dysarthric/intubated/trauma/language barrier': 1,
    'Aphasic': 2
}

option1A = st.radio(
    '1A: Level of consciousness',
    ('Alert; keenly responsive', 'Arouses to minor stimulation',
     'Requires repeated stimulation to arouse', 'Movements to pain',
     'Postures or unresponsive')
)

option1B = st.radio(
    '1B',
    ('Both questions right', '1 question right',
     '0 questions right', 'Dysarthric/intubated/trauma/language barrier',
     'Aphasic')
)

score1A = mapping1A[option1A]
score1B = mapping1B[option1B]

NIHSS_score = score1A + score1B
st.write(f"NIHSS Score: {NIHSS_score}")
