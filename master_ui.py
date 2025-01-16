import streamlit as st
from features import smart_hire
#, doc_gen_buddy, inter_q_coach, resume_categorization
from ui_utils.custom_css import apply_custom_css

st.set_page_config(layout="wide")

st.sidebar.title("Feature Selection")
features = ["SmartHire", "DocGenBuddy", "InterQCoach", "Resume Categorization", "None"]
selected_feature = st.sidebar.selectbox("Select a feature", features)


# Apply custom CSS
apply_custom_css()

if selected_feature == "None":
    st.title("Welcome to Vijay's GenAI experiments")
elif selected_feature == "SmartHire":
    smart_hire.display()
# elif selected_feature == "DocGenBuddy":
#     doc_gen_buddy.display()
# elif selected_feature == "InterQCoach":
#     inter_q_coach.display()
# elif selected_feature == "Resume Categorization":
#     resume_categorization.display()
