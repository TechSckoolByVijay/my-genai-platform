import io
import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.join(os.getcwd(), 'crews/interview_researcher/src'))
from interview_researcher import main

#from crews.interview_researcher.src.interview_researcher.main import main
load_dotenv(os.path.join(os.getcwd(), 'crews/interview_researcher', '.env'))

def run_and_capture_agent(jd_text, candidate_resume_text):
    # Create a StringIO buffer to capture stdout
    captured_output = io.StringIO()
    
    # Redirect stdout to capture the print statements from the agent
    sys.stdout = captured_output

    try:
        # Call the main function that runs your agent
        #result = main.run_my_agent(jd_text,candidate_resume_text)
        result = main.run_my_agent(jd_text,candidate_resume_text,2,"none")
    except Exception as e:
        result = f"Error occurred: {e}"
    
    # Restore the original stdout (terminal)
    sys.stdout = sys.__stdout__
    
    # Return the final result and the captured verbose logs
    verbose_logs = captured_output.getvalue()  # Get everything that was printed
    return result, verbose_logs
