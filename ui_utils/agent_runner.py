import io
import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.join(os.getcwd(), 'crews/interview_researcher/src'))
print("Python Path:", sys.path)

from interview_researcher import main

#from crews.interview_researcher.src.interview_researcher import main


#from crews.interview_researcher.src.interview_researcher.main import main
load_dotenv(os.path.join(os.getcwd(), 'crews/interview_researcher', '.env'))

def run_and_capture_agent(jd_text, candidate_resume_text):
    pass