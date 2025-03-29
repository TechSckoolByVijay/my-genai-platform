import streamlit as st
from ui_utils.agent_runner import run_and_capture_agent

def display():
    st.title("Doc Gen Buddy")

    # Job Description and Resume Upload
    # col1, col2 = st.columns(2)
    # with col1:
    #     jd_file = st.file_uploader("Upload Job Description", type=["txt", "pdf"], key="jd_file")
    # with col2:
    #     candidate_resume_file = st.file_uploader("Upload Candidate Resume", type=["txt", "pdf"], key="candidate_resume_file")

    repo_url=st.text_input("Enter the GitHub repo URL", key='docgenbuddy_repo_url')
    
    # Execute Agent
    if st.button("Trigger CrewAI Agent"):
        if jd_text and candidate_resume_text:
            result, verbose_logs = run_and_capture_agent(jd_text, candidate_resume_text)
            st.markdown('<br><h3 style="color: #00FFCC; font-family: Arial, sans-serif;">Your interview Q&A report</h3>', unsafe_allow_html=True)
            st.success(result)
            with st.expander("Agent at your service"):
                st.markdown(f'<div class="log-box"><span class="log-info">{verbose_logs}</span></div>', unsafe_allow_html=True)
        else:
            st.warning("Please provide both job description and candidate resume text.")
