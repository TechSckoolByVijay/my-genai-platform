import streamlit as st
from ui_utils.agent_runner import run_and_capture_agent

def display():
    st.title("SmartHire Agent")

    # Job Description and Resume Upload
    col1, col2 = st.columns(2)
    with col1:
        jd_file = st.file_uploader("Upload Job Description", type=["txt", "pdf"], key="jd_file")
    with col2:
        candidate_resume_file = st.file_uploader("Upload Candidate Resume", type=["txt", "pdf"], key="candidate_resume_file")

    # Text Inputs
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        jd_text = st.text_area("Your Job Description", key="jd_text", value='''In-depth understanding of various AI and Generative AI techniques and their practical applications. Design and develop custom ML, Gen AI, NLP, and LLM models Experience working with AI frameworks in Python with libraries like Pytorch,Pandas, NumPy, SciPy,Langchain etc. Prompt engineering, training and fine-tuning Large language models Evaluate model performance using relevant metrics and perform hyperparameter optimization. Develop methods for addressing bias, fairness, and ethical concerns in LLM development. Experience with Explainable AI (XAI) techniques and ethical considerations in AI development. Proficiency in cloud platforms like Azure, or GCP for AI workloads''')
    with col2:
        candidate_resume_text = st.text_area("Candidate Resume Text", key="candidate_resume_text", value='''Page 1 of 3
Vijay Saini
Generative AI Specialist & Cloud Architect with Azure DevOps Expertise
Cloud Architect and Generative AI Specialist with over 10 years of experience in designing and implementing
microservices architectures, CI/CD workflows, and automated cloud solutions. Detail-oriented and results- driven, I have a strong track record of enhancing system reliability and operational efficiency through innovative
solutions in Generative AI and infrastructure automation, particularly within Microsoft Azure environments.
vijaysainiprofessional@gmail.com 97844 04866
Bengaluru, India linkedin.com/in/vijay-saini-10759a8b
stackoverflow.com/users/5881105/vijay
SKILLS
Generative AI Retrieval-Augmented Generation (RAG) AIOps Azure AI LangChain , LangSmith and LangGraph
Custom GPTs & GenAI Agent Prompt Engineering LLM Certified Kubernetes Professional - CKAD & KCNA
Architecture Design Containerization Site Reliability Engineering Serverless computing GitHub Actions
Infrastructure as Code - Terraform Microservices Cloud Migration CI/CD PowerShell & Python Microsoft Azure
Microsoft Certified: DevOps Engineer Expert
WORK EXPERIENCE
Lead Architect – GenAI & DevOps
PwC US
05/2023 - Present, Bengaluru, India PwC (PricewaterhouseCoopers) is a global professional services firm offering audit, tax, and consulting services. It helps organizations solve complex business challenges, optimize operations, and drive innovation across industries.
Developed a multi-region hub and spoke cloud architecture using Infrastructure-as-Code (IaC) principles to manage scalable, distributed
environments. Played a key role in onboarding several enterprise clients to Azure, streamlining their operations and supporting their
transition to cloud-based services. Dived into the world of Generative AI, where I helped create and deploy multiple serverless applications on Azure Function Apps, enhancing
our ability to deliver innovative AI solutions. As the project gained traction, I helped transform it into a centralized hub for generative AI applications on Kubernetes, enabling efficient
communication between apps through Service Bus.
Implemented Helm for centralized Kubernetes management and KEDA for intelligent pod scaling based on message queue size, optimizing
resource usage and processing speed. Designed a robust DevOps framework that included CI/CD pipelines and automated database operations, which significantly improved our
deployment processes and overall project reliability, using Datadog for effective monitoring. Gained valuable experience with tools like Azure AI Search, Document Intelligence, Helm, and OpenAI, which enriched our offerings and kept
us ahead of industry trends.
Leveraged my understanding of generative AI application flow to troubleshoot and resolve issues, tracing requests from custom GPT through
Kubernetes ingress and pods. Used tools like Swagger and Datadog to efficiently identify root causes and implement effective solutions. Collaborated closely with the security team to identify and mitigate potential vulnerabilities, implementing customer-managed keys for
encryption, establishing private endpoints for secure connectivity, and enforcing robust password and key policies, ensuring our architecture
met stringent company security standards.
Implemented an event-driven Retrieval-Augmented Generation (RAG) pipeline from scratch, serving as the backbone of projects. This
solution integrated AI services, including Service Bus, Storage Account, Document Intelligence, embeddings, and AI Search.
Achievements/Tasks
Page 2 of 3
WORK EXPERIENCE
Technical Lead
MindTree Ltd - Project IDN
02/2021 - 05/2023, Bengaluru, India
Developed a scalable Kubernetes infrastructure to develop and deploy Microservices-based platform aimed at bringing multiple partners
together to develop plugins based on existing offerings of client products.
Implemented DevOps practices with GitHub Action CI/CD workflows for Microservices deployment on Azure Kubernetes via Azure Container
Registry. Achieved one-click end-to-end infra deployment automation. Developed & Maintained Azure Bicep templates for deployment of Azure
resources ( Infrastructure as Code ).
Troubleshot and resolved complex production issues related to Kubernetes and Azure. Collaborated with development teams to ensure
smooth deployment and operations of applications in the production environment.
DevOps Engineer
o9 Solutions
05/2020 - 02/2021, Bengaluru''')

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
