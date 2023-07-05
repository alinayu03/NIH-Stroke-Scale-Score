import streamlit as st


def calculate_nihss(score_dict):
    score = 0
    score += score_dict["level_of_consciousness"]
    score += score_dict["left_arm_motor"]
    score += score_dict["right_arm_motor"]
    score += score_dict["left_leg_motor"]
    score += score_dict["right_leg_motor"]
    score += score_dict["limb_ataxia"]
    score += score_dict["sensory"]
    score += score_dict["language"]
    score += score_dict["dysarthria"]
    score += score_dict["extinction_inattention"]
    return score


def main():
    st.title("NIH Stroke Scale/Score (NIHSS) Calculator")

    st.write(
        "Please enter the scores for each component of the NIH Stroke Scale/Score (NIHSS).")
    st.write("Use the following scale:")
    st.write("- 0: Normal")
    st.write("- 1: Mild")
    st.write("- 2: Moderate")
    st.write("- 3: Severe")

    score_dict = {}
    score_dict["level_of_consciousness"] = st.slider(
        "Level of Consciousness", 0, 3, 0)
    score_dict["left_arm_motor"] = st.slider("Left Arm Motor", 0, 3, 0)
    score_dict["right_arm_motor"] = st.slider("Right Arm Motor", 0, 3, 0)
    score_dict["left_leg_motor"] = st.slider("Left Leg Motor", 0, 3, 0)
    score_dict["right_leg_motor"] = st.slider("Right Leg Motor", 0, 3, 0)
    score_dict["limb_ataxia"] = st.slider("Limb Ataxia", 0, 3, 0)
    score_dict["sensory"] = st.slider("Sensory", 0, 3, 0)
    score_dict["language"] = st.slider("Language", 0, 3, 0)
    score_dict["dysarthria"] = st.slider("Dysarthria", 0, 3, 0)
    score_dict["extinction_inattention"] = st.slider(
        "Extinction/Inattention", 0, 3, 0)

    if st.button("Calculate NIHSS Score"):
        score = calculate_nihss(score_dict)
        st.write("NIHSS Score:", score)


if __name__ == "__main__":
    main()
