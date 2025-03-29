from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import ScrapeWebsiteTool
from pydantic import BaseModel, Field

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


class City(BaseModel):
    city: str
    duration_in_days: int
    avg_temp: int

@CrewBase
class Webparsepro():
	"""Webparsepro crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def city_selector(self) -> Agent:
		return Agent(
			config=self.agents_config['city_selector'],
			verbose=True
		)

	@agent
	def local_guide(self) -> Agent:
		return Agent(
			config=self.agents_config['local_guide'],
			verbose=True
		)

	@agent
	def itinerarie_maker(self) -> Agent:
		return Agent(
			config=self.agents_config['itinerarie_maker'],
			verbose=True
		)

	# @agent
	# def reporting_analyst(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['reporting_analyst'],
	# 		verbose=True
	# 	)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def city_selector_task(self) -> Task:
		return Task(
			config=self.tasks_config['city_selector_task'],
		)

	@task
	def recommend_local_experiences_task(self) -> Task:
		return Task(
			config=self.tasks_config['recommend_local_experiences_task'],
		)

	@task
	def create_travel_itinerary_task(self) -> Task:
		return Task(
			config=self.tasks_config['create_travel_itinerary_task'],
			output_file="travel_plan.md"
		)
	@task
	def report_city_name(self) -> Task:
		return Task(
			config=self.tasks_config['report_city_name'],
			output_json=City,
		)

	# @task
	# def reporting_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['reporting_task'],
	# 		output_file='report.md'
	# 	)

	@crew
	def crew(self) -> Crew:
		"""Creates the Webparsepro crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
