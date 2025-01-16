from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
#from crewai_tools import Tool
from crewai.tools import BaseTool
#from crewai_tools import Tool

#from docgenbuddy.src.docgenbuddy.tools.xxd import github_downloader

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# Tool for cloning GitHub repositories
class GitCloneTool(BaseTool):
    def __init__(self):
        super().__init__()

    name: str = "git_clone"
    description: str = (
        "A tool to clone a Git repository. Provide the 'repo_url' and optionally an 'output_dir'."
        " Example: { 'repo_url': 'https://github.com/example/repo.git', 'output_dir': 'my_repo' }"
    )
    def _run(self, input):
        	print("hello")
    # def _run(self, inputs):
    #     import subprocess
    #     repo_url = inputs.get("repo_url")
    #     output_dir = inputs.get("output_dir", "cloned_repo")
    #     if not repo_url:
    #         return "Error: 'repo_url' is required."
    #     try:
    #         subprocess.run(["git", "clone", repo_url, output_dir], check=True)
    #         return f"Repository cloned into {output_dir}"
    #     except subprocess.CalledProcessError as e:
    #         return f"Error cloning repository: {str(e)}"

import os
import requests
#from crewai_tools import tool
from crewai.tools import BaseTool,tool

# @tool
# def github_downloader(repo_url: str, save_directory: str) -> str:
#     """
#     Downloads a GitHub repository as a zip file from the given URL.

#     Args:
#         repo_url (str): The URL of the GitHub repository.
#         save_directory (str): The directory where the repository will be saved.

#     Returns:
#         str: The path to the downloaded zip file.
#     """
#     try:
#         # Validate and construct the download URL
#         if not repo_url.endswith("/"):
#             repo_url += "/"
#         zip_url = f"{repo_url}archive/refs/heads/main.zip"
        
#         # Prepare download path
#         response = requests.get(zip_url, stream=True)
#         response.raise_for_status()  # Raise an error for bad HTTP status
        
#         # Ensure save directory exists
#         os.makedirs(save_directory, exist_ok=True)
#         file_path = os.path.join(save_directory, f"{repo_url.split('/')[-1]}-main.zip")
        
#         # Save the file
#         with open(file_path, "wb") as f:
#             for chunk in response.iter_content(chunk_size=8192):
#                 f.write(chunk)
        
#         return f"Repository downloaded successfully to {file_path}"
    
#     except Exception as e:
#         return f"Failed to download repository: {str(e)}"




@CrewBase
class Docgenbuddy():
	"""Docgenbuddy crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def repository_downloader(self) -> Agent:
		return Agent(
			config=self.agents_config['repository_downloader'],
			tools=[GitCloneTool()],
			verbose=True
		)

	@agent
	def script_analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['script_analyzer'],
			verbose=True
		)
	
	@agent
	def documentation_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['documentation_writer'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def clone_repository_task(self) -> Task:
		return Task(
			config=self.tasks_config['clone_repository_task'],
			#tools=[GitCloneTool()],
		)

	@task
	def analyze_script_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_script_task'],
			output_file='report.md',
            
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Docgenbuddy crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
