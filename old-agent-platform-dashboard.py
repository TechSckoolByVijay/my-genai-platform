import streamlit as st
from streamlit_chat import message
import sys
import os
import io
from datetime import datetime 
from dotenv import load_dotenv

st.set_page_config(layout="wide")

sys.path.append(os.path.join(os.getcwd(), 'crews/interview_researcher/src'))
# Import the CrewAI agent modules
from interview_researcher import main

# Load environment variables from the .env file
load_dotenv(os.path.join(os.getcwd(), 'interview_researcher', '.env'))
# Function to capture and display verbose logs
def run_and_capture_agent():
    # Create a StringIO buffer to capture stdout
    captured_output = io.StringIO()
    
    # Redirect stdout to capture the print statements from the agent
    sys.stdout = captured_output

    try:
        # Call the main function that runs your agent
        result = main.run_my_agent(jd_text,candidate_resume_text,temperature,special_instruction)
    except Exception as e:
        result = f"Error occurred: {e}"
    
    # Restore the original stdout (terminal)
    sys.stdout = sys.__stdout__
    
    # Return the final result and the captured verbose logs
    verbose_logs = captured_output.getvalue()  # Get everything that was printed
    return result, verbose_logs



if 'verbose_logs' not in st.session_state:
    st.session_state.verbose_logs = []


# Apply custom CSS for terminal-like appearance
st.markdown("""
    <style>
    .log-box {
        background-color: #1e1e1e; /* Dark background */
        color: #f0f0f0; /* Light text color */
        padding: 10px;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        white-space: pre-wrap;
    }
    .log-info { color: #00ff00; } /* Green for info logs */
    .log-warning { color: #ffcc00; } /* Yellow for warnings */
    .log-error { color: #ff0000; } /* Red for errors */
    </style>
""", unsafe_allow_html=True)


st.sidebar.title("Feature Selection")

features = ["SmartHire", "DocGenBuddy", "InterQCoach", "Resume Categorization","None"]
#selected_feature = st.sidebar.radio("Select a feature", features)
selected_feature = st.sidebar.selectbox("Select a feature",features)

st.sidebar.button("Next Gen Features")
st.sidebar.button("Hiring Made Easy")

# Initialize session state for chat history per feature
if "feature_chats" not in st.session_state:
    st.session_state.feature_chats = {feature: [] for feature in features}

# Display default main content or feature-specific content
if selected_feature == "None":
    st.title("Welcome to Vijay's GenAI experiments")
elif selected_feature == "SmartHire":
    st.title("SmartHire Agent")
        
        # First row with file uploaders
    col1, col2 = st.columns(2)
    with col1:
        jd_file = st.file_uploader("Upload Job Description", type=["txt", "pdf" ], key="jd_file")
    with col2:
        candidate_resume_file = st.file_uploader("Upload Candidate Resume", type=["txt", "pdf"], key="candidate_resume_file")
    
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        jd_text = st.text_area("Your Job Description", key="jd_text", value='''JOB DESCRIPTION – SENIOR AI ARCHITECT
High Level Summary
Chevron invites applications for the role of AI Architect within our Enterprise AI team in
India. This position is integral to designing and developing AI/ML models that significantly
accelerate the delivery of business value. We are looking for an AI architect with the
ability to bring their expertise, innovative attitude and oversee the implementation of AI
solutions. We are looking for an individual with a passion for exploring, innovating, and
delivering cutting edge AI/ML solutions that provide immense value to our business.
Key Responsibilities
• Create the overall architecture for AI systems and solutions, ensuring that they meet
business requirements and are scalable.
• Collaborate with the AI Technical Manager and GCC Petro-technical professionals
and data engineers to integrate models into the business framework.
• Oversee the data collection, storage, and preprocessing to ensure data quality and
availability by working with the data engineering teams across various partner
organizations.
• Consult and provide architectural guidance associated with data, technology,
architectural design patterns, algorithm, and model selection for specific tasks or
solutions.
• Provide oversight for the training of AI models, including tuning and optimizing
performance and cost, building low latency, scalable, and resilient ML and
optimization workloads into AI products.
• Implement AI models into production environments, ensuring they run efficiently
and reliably.
• Continuously monitoring AI systems for performance, accuracy, and reliability, and
making necessary adjustments.
• Ensure that AI solutions and larger AI systems are secure and comply with data
privacy regulations and Responsible AI guardrails.
• Work with cross-functional teams, including data scientists, data engineers, and
business stakeholders, to align AI initiatives and business goals leveraging standard
compliant Chevron IT foundational services.
• Stay abreast of the latest AI trends and technologies and provide technical thought
leadership to the AI team to continuously improve and consider incorporating new
tools and service offerings into the AI ecosystem at Chevron.
Required Qualifications
• Minimum 5 years of experience in in practical AI/ML solution development in industry
or academia; strong preference for additional architectural design and implementation
experience. 5 - 10 years of experience.
• Solid foundation in software development principles and practices, software design
patterns, integration standards and patterns.
• Understanding of AI/ML model life cycle management and DevOps/MLOps.
• Strong programming skills in Python, Spark, C++, Javascript etc.
• Experience designing custom APIs for machine learning models for training and
inference processes and designing, implementing, and delivering frameworks for MLOps.
• Experience in building data pipelines and ML pipelines utilizing Azure services, such as
Azure Data Factory and Azure Machine Learning, as well as CI/CD (e.g. Ansible).
• Experience in data storage (e.g. Azure Data Lake & Blob Storage), data processing, data
engineering (e.g. Databricks, ADF, Azure Synapse), and data governance.
• Proficient at orchestrating large-scale ML/DL jobs, leveraging big data tooling and
modern container orchestration infrastructure, to tackle distributed training and massive
parallel model executions on cloud infrastructure.
• Working knowledge of cognitive services, computer vision, and generative AI
technology and services, e.g. Azure OpenAI.
• Experience in integrating AI solutions with existing systems and workflows.
• Understanding of ethical considerations and compliance requirements of AI.
• Ability to engage business and technical experts at all organizational levels and assess
opportunities to apply machine learning and analytics to improve their workflows and
deliver information and insight to support business decisions.
• Ability to communicate in a clear, concise, and understandable manner both orally and
in writing.''')
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
05/2020 - 02/2021, Bengaluru
Industry leaders transforming its customer's Sales, Supply Chain and Integrated Business Planning with AI solutions .
Troubleshooting of production issues and updated infrastructure with software patches. Production Support, Upgrades, and monthly
maintenance. Developed End-to-End Application validation Automation deployed on Jenkins for validating multiple servers parallelly and generate a formal
html validation report. Internal Process Automation. Recommended & implemented enhancements for improving availability, reliability & performance of our application. o9 platform release &
deployment cycle and Product maintenance. Excellent planning and Implementation skill.
Technical Consultant - DevOps
Blue Yonder (Previously JDA)
01/2015 - 05/2020, For over 30 years, Blue Yonder has been the leading provider of end-to-end, integrated retail and supply chain planning and execution solutions.
Technology Used: Azure DevOps Azure PowerShell, DSC, Azure Repos, Azure Pipelines, ARM Templates, Azure WebApps, Logic Apps. Part of the team for planning to migrate our enterprise application from traditional infrastructure to cloud-based infrastructure with minimal
disruption in our customer service. End to End Environment provisioning of JDA Products in Microsoft Azure Cloud. Developed PowerShell scripts and automated 1000+ hours of manual work/year. This also leads to lesser downtime in our services. Was
awarded the second-highest prestigious award(Individual Pillar Award) for this work.
Troubleshooting of production issues and updated infrastructure with software patches. Production Support, Upgrades, and monthly
maintenance.
TECHNICAL SKILLS
Azure Services Kubernetes Service, Containers, FrontDoor, Application Gateway, App Service, Azure
Automation, AppConfig
Generative AI Prompt Engineering, AIOps, GenAI Agents, LangChain, LangSmith, Custom GPTs, Swagger, FastAPI
Cloud Serverless Computing, Function App, App
Service, Virtual Machine, Monitoring, On- premise to Azure Cloud Migration
DevOps GitHub Action, Designing Build and Release
Pipelines, Secret Management, Azure
Boards, Agile
Automation PowerShell, Python, Azure CLI, Azure
PowerShell
Database Microsoft SQL Server, Oracle, Microsoft
Azure SQL Database
Achievements/Tasks
DevOps Engineer
Azure DevOps Engineer
Page 3 of 3
PROJECTS
Lead Architect, GenAI Factory Initiative
Led the design and development of the GenAI Factory platform, creating a unified architecture that supports multiple business use cases, streamlining
hosting, operations, and maintenance through a common platform pattern. Architected a multi-agent, multi-Generative AI model platform utilizing LangChain, GenAI Agents, LangSmith, and AI Search Index, enabling seamless
integration of various generative AI models.
Implemented a robust Retrieval-Augmented Generation (RAG) pipeline to enhance AI-driven data retrieval and contextual responses, improving model
performance across use cases. Leveraged Azure Service Bus for decoupled communication, and utilized Helm for Kubernetes management and KEDA for pod scaling, optimizing resource usage and processing speed. Led the DevOps strategy, optimizing CI/CD pipelines, automation processes, and infrastructure-as-code deployments to accelerate development and
deployment cycles. Multi-Region Hub & Spoke Platform Automation for a Healthcare Client's Cloud Transformation
Spearheaded the development of a fully automated multi-region Hub & Spoke platform for a leading U.S. healthcare client, ensuring scalability and resilience
in their cloud infrastructure. Utilized Terraform for Infrastructure as Code (IaC) and Azure DevOps pipelines to streamline deployment and management processes, enhancing operational efficiency. Enabled the client’s data transformation journey by delivering a highly available, fault-tolerant platform deployed on Azure Cloud, supporting their transition
to a modern cloud-based architecture. Microservices Based Enterprise Development Platform - IDN
Developed a scalable and standardized Microservices-based platform aimed at bringing multiple partners together to develop extensions based on existing offerings of client products. Achieved one-click end-to-end infra deployment automation. Developed & Maintained Azure Bicep templates for deployment of Azure resources (
Infrastructure as Code ). Developed GitHub Action CI/CD workflows for Microservices deployment on Azure Kubernetes.
CERTIFICATES
Certified Kubernetes Application Developer ( CKAD )
(04/2024 - Present)
The Certified Kubernetes Application Developer (CKAD) exam certifies
that candidates can design, build and deploy cloud-native applications for Kubernetes. The CKAD was created by the Linux Foundation.
Hashicorp Certified Terraform Associate (07/2023 - Present)
The Terraform Associate certification is for Cloud Engineers specializing in operations, IT, or development who know the basic concepts and skills associated with Terraform.
Microsoft Certified: DevOps Engineer Expert
(01/2022 - Present) subject matter expertise in working with people, processes, and products
to enable the continuous delivery of value in organizations.
Kubernetes and Cloud Native Associate (KCNA)
(12/2022 - Present)
Demonstrates a user’s foundational knowledge and skills in Kubernetes and the wider cloud native ecosystem. Microsoft Certified: Azure Data Fundamentals
(11/2023 - Present)
This certification is an opportunity to demonstrate your knowledge of core data concepts and related Microsoft Azure data services.
AZ-104: Microsoft Certified: Azure Administrator Associate
certification (10/2019 - Present)
Expertise in implementing, managing, and monitoring an organization’s Microsoft Azure environment. AZ-900 : Microsoft Certified Azure Fundamentals
certification (08/2019 - Present)
This certificate demonstrates to have a foundational knowledge of cloud
services and how those services are provided with Microsoft Azure.
Microsoft Certified: Azure AI Fundamentals
(01/2024 - Present)
Demonstrate fundamental AI concepts related to the development of software and services of Microsoft Azure to create AI solutions.
HONOR AWARDS
Individual Pillar Award (2018)
Blue Yonder An annual award to recognize the exceptional performance & individual efforts that have made a significant contribution to enhancing customer satisfaction and timely delivery.
Team Pillar Award (2019)
JDA Software An annual award to recognize the contribution of an individual in
helping the team to achieve its targets.
Spot Award (2017)
JDA Software Awarded SPOT award for efficiently handling a data center outrage potentially causing business disruption of multiple clients.
EDUCATION
Master Of Science(hons.)
BITS Pilani, Pilani campus
07/2010 - 06/2014, Pilani, Rajasthan''')


    temperature = st.slider("Set Temperature", min_value=0.0, max_value=1.0, value=0.5, key="hire_smart_temperature")
    special_instruction = st.text_input("Special Instruction for Agent", placeholder="pecial Instruction for Agent", value="nothing for now")
    trigger_button = st.button("Trigger CrewAI Agent")
    
    if trigger_button:
        # Capture the agent's output and verbose logs
        final_message, verbose_logs = run_and_capture_agent()

        # Show the verbose logs in a collapsible expander with a terminal-like appearance
        # with st.expander("Agent is running"):
        #     st.markdown(f'<div class="log-box">{verbose_logs}</div>', unsafe_allow_html=True)

        # Show verbose logs in a collapsible expander
        with st.expander("Agent at your service"):
            #for log in st.session_state.verbose_logs:
            # for log in verbose_logs:
            #     # For simplicity, you can add logic to categorize messages (info, warning, error) based on their content
            #     if "error" in log.lower():
            #         log_class = "log-error"
            #     elif "warning" in log.lower():
            #         log_class = "log-warning"
            #     else:
            #         log_class = "log-info"

            # Display each log with appropriate CSS class
            st.markdown(f'<div class="log-box"><span class="log-info">{verbose_logs}</span></div>', unsafe_allow_html=True)

        # Display the final result from the agent
        st.markdown('<br><h3 style="color: #00FFCC; font-family: Arial, sans-serif;">Your interview Q&A report</h3>', unsafe_allow_html=True)
        st.success(final_message)
        message_data = str(final_message)
        # #formatted_message = message_data.replace("\n", "<br>")
        
        # st.markdown(
        #     f"""
        #     <div style="
        #         background: linear-gradient(145deg, #1E1E1E, #252525); 
        #         color: #D3D3D3; 
        #         padding: 20px; 
        #         border-radius: 10px; 
        #         box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5); 
        #         font-family: 'Roboto', sans-serif; 
        #         font-size: 14px; 
        #         line-height: 1.6;">
                
        #         {message_data}
        #         <br><br>
        #         </div>
        #     """,
        #     unsafe_allow_html=True
        # )
        
    
# else:
#     st.title(f"{selected_feature}")

#     # File uploader
#     uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "jpg", "png"])

#     # Temperature input
#     temperature = st.slider("Set Temperature", min_value=0.0, max_value=1.0, value=0.5)

#     # System message input
#     system_message = st.text_input("System Message", placeholder="Enter system message")

#     # Chat with AI, specific to each feature
#     st.subheader("Chat with AI")
#     feature_chat_key = f"{selected_feature}_chat_history"
#     if feature_chat_key not in st.session_state:
#         st.session_state[feature_chat_key] = []

#     # Display past conversation for selected feature
#     for msg in st.session_state[feature_chat_key]:
#         message(msg["content"], is_user=msg["is_user"])

#     # New user input
#     user_input = st.text_input("Your message:", placeholder="Type your message here...")
#     import time

#     # After capturing user input
#     if user_input:
#         # Display the user's message immediately
#         st.session_state[feature_chat_key].append({"content": user_input, "is_user": True})
        
#         # Mimic AI processing time
#         time.sleep(1)  # Add delay here to simulate response time

#         # Generate AI response (in a real app, you’d call an API here)
#         ai_response = f"AI Response to '{user_input}'"
#         ai_response = get_openai_response(user_input, temperature)
#         st.session_state[feature_chat_key].append({"content": ai_response, "is_user": False})

#         # Display the AI response
#         message(ai_response, is_user=False)
