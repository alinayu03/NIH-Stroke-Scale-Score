import streamlit as st

st.markdown(
    "# [NIHSS Calculator](https://www.mdcalc.com/calc/715/nih-stroke-scale-score-nihss)")
st.markdown("Calculates the NIH Stroke Scale for quantifying stroke severity.")
st.markdown("Evidence in this calculator refers to: [Evidence](https://example.com)")

sections = [
    {
        "section_title": "1A: Level of consciousness (May be assessed casually while taking history)",
        "options": [
            'Alert; keenly responsive', 'Arouses to minor stimulation',
            'Requires repeated stimulation to arouse', 'Movements to pain',
            'Postures or unresponsive'
        ],
        "mapping": {
            'Alert; keenly responsive': 0,
            'Arouses to minor stimulation': 1,
            'Requires repeated stimulation to arouse': 2,
            'Movements to pain': 3,
            'Postures or unresponsive': 4
        }
    },
    {
        "section_title": "1B: Ask month and age",
        "options": [
            'Both questions right', '1 question right',
            '0 questions right', 'Dysarthric/intubated/trauma/language barrier',
            'Aphasic'
        ],
        "mapping": {
            'Both questions right': 0,
            '1 question right': 1,
            '0 questions right': 2,
            'Dysarthric/intubated/trauma/language barrier': 1,
            'Aphasic': 2
        }
    },
    {
        "section_title": "1C: 'Blink eyes' & 'squeeze hands' (Pantomime commands if communication barrier)",
        "options": [
            'Performs both tasks',
            'Performs 1 task', 'Performs 0 tasks'
        ],
        "mapping": {
            'Performs both tasks': 0,
            'Performs 1 task': 1,
            'Performs 0 tasks': 2
        }
    },
    {
        "section_title": "2: Horizontal extraocular movements (Only assess horizontal gaze)",
        "options": [
            'Normal',
            'Partial gaze palsy: can be overcome',
            'Partial gaze palsy: corrects with oculocephalic reflex',
            'Forced gaze palsy: cannot be overcome'
        ],
        "mapping": {
            'Normal': 0,
            'Partial gaze palsy: can be overcome': 1,
            'Partial gaze palsy: corrects with oculocephalic reflex': 1,
            'Forced gaze palsy: cannot be overcome': 2
        }
    },
    {
        "section_title": "3: Visual fields",
        "options": [
            'No visual loss', 'Partial hemianopia',
            'Complete hemianopia', 'Patient is bilaterally blind',
            'Bilateral hemianopia'
        ],
        "mapping": {
            'No visual loss': 0,
            'Partial hemianopia': 1,
            'Complete hemianopia': 2,
            'Patient is bilaterally blind': 3,
            'Bilateral hemianopia': 3
        }
    },
    {
        "section_title": "4: Facial palsy (Use grimace if obtunded)",
        "options": [
            'Normal symmetry',
            'Minor paralysis (flat nasolabial fold, smile asymmetry)',
            'Partial paralysis (lower face)',
            'Unilateral complete paralysis (upper/lower face)',
            'Bilateral complete paralysis (upper/lower face)'
        ],
        "mapping": {
            'Normal symmetry': 0,
            'Minor paralysis (flat nasolabial fold, smile asymmetry)': 1,
            'Partial paralysis (lower face)': 2,
            'Unilateral complete paralysis (upper/lower face)': 3,
            'Bilateral complete paralysis (upper/lower face)': 3
        }
    },
    {
        "section_title": "5A: Left arm motor drift (Count out loud and use your fingers to show the patient your count)",
        "options": [
            'No drift for 10 seconds', 'Drift, but doesn\'t hit bed',
            'Drift, hits bed', 'Some effort against gravity',
            'No effort against gravity', 'No movement',
            'Amputation/joint fusion'
        ],
        "mapping": {
            'No drift for 10 seconds': 0,
            'Drift, but doesn\'t hit bed': 1,
            'Drift, hits bed': 2,
            'Some effort against gravity': 2,
            'No effort against gravity': 3,
            'No movement': 4,
            'Amputation/joint fusion': 0
        }
    },
    {
        "section_title": "5B: Right arm motor drift (Count out loud and use your fingers to show the patient your count)",
        "options": [
            'No drift for 10 seconds', 'Drift, but doesn\'t hit bed',
            'Drift, hits bed', 'Some effort against gravity',
            'No effort against gravity', 'No movement',
            'Amputation/joint fusion'
        ],
        "mapping": {
            'No drift for 10 seconds': 0,
            'Drift, but doesn\'t hit bed': 1,
            'Drift, hits bed': 2,
            'Some effort against gravity': 2,
            'No effort against gravity': 3,
            'No movement': 4,
            'Amputation/joint fusion': 0
        }
    },
    {
        "section_title": "6A: Left leg motor drift (Count out loud and use your fingers to show the patient your count)",
        "options": [
            'No drift for 5 seconds', 'Drift, but doesn\'t hit bed',
            'Drift, hits bed', 'Some effort against gravity',
            'No effort against gravity', 'No movement',
            'Amputation/joint fusion'
        ],
        "mapping": {
            'No drift for 5 seconds': 0,
            'Drift, but doesn\'t hit bed': 1,
            'Drift, hits bed': 2,
            'Some effort against gravity': 2,
            'No effort against gravity': 3,
            'No movement': 4,
            'Amputation/joint fusion': 0
        }
    },
    {
        "section_title": "6B: Right leg motor drift (Count out loud and use your fingers to show the patient your count)",
        "options": [
            'No drift for 5 seconds', 'Drift, but doesn\'t hit bed',
            'Drift, hits bed', 'Some effort against gravity',
            'No effort against gravity', 'No effort against gravity', 'No movement',
            'Amputation/joint fusion'
        ],
        "mapping": {
            'No drift for 5 seconds': 0,
            'Drift, but doesn\'t hit bed': 1,
            'Drift, hits bed': 2,
            'Some effort against gravity': 2,
            'No effort against gravity': 3,
            'No movement': 4,
            'Amputation/joint fusion': 0
        }
    },
    {
        "section_title": "7: Limb Ataxia (FNF/heel-shin)",
        "options": [
            'No ataxia', 'Ataxia in 1 Limb',
            'Ataxia in 2 Limbs', 'Does not understand', 'Paralyzed',
            'Amputation/joint fusion'
        ],
        "mapping": {
            'No ataxia': 0,
            'Ataxia in 1 Limb': 1,
            'Ataxia in 2 Limbs': 2,
            'Does not understand': 0,
            'Paralyzed': 0,
            'Amputation/joint fusion': 0
        }
    },
    {
        "section_title": "8: Sensation",
        "options": [
            'Normal; no sensory loss',
            'Mild-moderate loss: less sharp/more dull',
            'Mild-moderate loss: can sense being touched',
            'Complete loss: cannot sense being touched at all',
            'No response and quadriplegic', 'Coma/unresponsive'
        ],
        "mapping": {
            'Normal; no sensory loss': 0,
            'Mild-moderate loss: less sharp/more dull': 1,
            'Mild-moderate loss: can sense being touched': 1,
            'Complete loss: cannot sense being touched at all': 2,
            'No response and quadriplegic': 2,
            'Coma/unresponsive': 2
        }
    },
    {
        "section_title": "9: Language/aphasia (Describe the scene; name the items; read the sentences (see Evidence))",
        "options": [
            'Normal; no aphasia',
            'Mild-moderate aphasia: some obvious changes, without significant limitation',
            'Severe aphasia: fragmentary expression, inference needed, cannot identify materials',
            'Mute/global aphasia: no usable speech/auditory comprehension',
            'Coma/unresponsive'
        ],
        "mapping": {
            'Normal; no aphasia': 0,
            'Mild-moderate aphasia: some obvious changes, without significant limitation': 1,
            'Severe aphasia: fragmentary expression, inference needed, cannot identify materials': 2,
            'Mute/global aphasia: no usable speech/auditory comprehension': 3,
            'Coma/unresponsive': 3
        }
    },
    {
        "section_title": "10: Dysarthria (Read the words (see Evidence))",
        "options": [
            'Normal',
            'Mild-moderate dysarthria: slurring but can be understood',
            'Severe dysarthria: unintelligible slurring or out of proportion to dysphasia', 'Mute/anarthric',
            'Intubated/unable to test'
        ],
        "mapping": {
            'Normal': 0,
            'Mild-moderate dysarthria: slurring but can be understood': 1,
            'Severe dysarthria: unintelligible slurring or out of proportion to dysphasia': 2,
            'Mute/anarthric': 2,
            'Intubated/unable to test': 0
        }
    },
    {
        "section_title": "11: Extinction/inattention",
        "options": [
            'No abnormality',
            'Visual/tactile/auditory/spatial/personal inattention',
            'Extinction to bilateral simultaneous stimulation',
            'Profound hemi-inattention (ex: does not recognize own hand)',
            'Extinction to >1 modality'
        ],
        "mapping": {
            'No abnormality': 0,
            'Visual/tactile/auditory/spatial/personal inattention': 1,
            'Extinction to bilateral simultaneous stimulation': 1,
            'Profound hemi-inattention (ex: does not recognize own hand)': 2,
            'Extinction to >1 modality': 1
        }
    }
]

total_NIHSS_score = 0

for section in sections:
    section_title = section["section_title"]
    options = section["options"]
    mapping = section["mapping"]

    option = st.radio(section_title, options)
    score = mapping[option]
    total_NIHSS_score += score

if st.button("Calculate NIHSS Score"):
    st.write(f"NIHSS Score: {total_NIHSS_score}")
