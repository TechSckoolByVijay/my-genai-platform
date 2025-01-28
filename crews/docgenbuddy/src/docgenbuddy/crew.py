from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import BaseTool
from crewai_tools import DirectoryReadTool, FileReadTool

import os
# Tool for cloning GitHub repositories
class GitCloneTool(BaseTool):
    name: str = "git clone tool"
    description: str = "A tool to clone a Git repository. Provide the 'repo_url' and optionally an 'output_dir'."

    def _run(self, repo_url: str,output_dir: str):
        import subprocess
        #repo_url="https://github.com/TechSckoolByVijay/GitHubActions"
        #output_dir="C:\Learning Lab\my-genai-platform\crews\docgenbuddy\out"
        #repo_url = inputs.get("repo_url")
        #output_dir = inputs.get("output_dir", "cloned_repo")
        if not repo_url:
            return "Error: 'repo_url' is required."
        try:
            subprocess.run(["git", "clone", repo_url, output_dir], check=True)
            return f"Repository cloned into {output_dir}"
        except subprocess.CalledProcessError as e:
            return f"Error cloning repository: {str(e)}"

class List_and_Read_Files(BaseTool):
    name: str = "List and Read files"
    description: str = "List the required files at 'output_dir' and read them. "

    def _run(self,directory_path: str):
        file_data = {}
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_data[file] = f.read()
        return file_data

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
			tools=[DirectoryReadTool(),FileReadTool(),List_and_Read_Files()],
			#tools=[List_and_Read_Files()],
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
			config=self.tasks_config['clone_repository_task']
		)

	@task
	def create_list_of_scripts(self) -> Task:
		return Task(
			config=self.tasks_config['create_list_of_scripts']
		)
	
	@task
	def analyze_script_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_script_task']
		)
	@task
	def generate_readme_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_readme_task'],
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
