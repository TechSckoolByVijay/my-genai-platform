import streamlit as st
from features import smart_hire,doc_gen_buddy
#, doc_gen_buddy, inter_q_coach, resume_categorization
from ui_utils.custom_css import apply_custom_css

 
# import os
# import sys
# from dotenv import load_dotenv

#from crews.interview_researcher.src.interview_researcher.main import main
# load_dotenv()
# os.environ['LANGCHAIN_TRACING_V2']=os.getenv('LANGCHAIN_TRACING_V2')
# os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
# os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')

st.set_page_config(layout="wide")

st.sidebar.title("Feature Selection")
features = [ "None","SmartHire", "Keto Diet Planner", "Stock Market", "DocGenBuddy", "InterQCoach", "Resume Categorization"]
selected_feature = st.sidebar.selectbox("Select a feature", features)



# Apply custom CSS
apply_custom_css()

if selected_feature == "None":
    st.title("Welcome to Vijay's GenAI experiments")
elif selected_feature == "SmartHire":
    #pass
    smart_hire.display()
elif selected_feature == "DocGenBuddy":
    #pass
    doc_gen_buddy.display()
# elif selected_feature == "InterQCoach":
#     inter_q_coach.display()
# elif selected_feature == "Resume Categorization":
#     resume_categorization.display()
