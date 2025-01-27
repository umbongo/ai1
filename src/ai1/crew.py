from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Ai1():
	"""Ai1 crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True
		)

	@agent
	def profiler(self) -> Agent:
		return Agent(
			config=self.agents_config['profiler'],
			verbose=True
		)
	
	@agent
	def resume_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['resume_strategist'],
			verbose=True
		)
	
	@agent
	def interview_preparer(self) -> Agent:
		return Agent(
			config=self.agents_config['interview_preparer'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def profile_task(self) -> Task:
		return Task(
			config=self.tasks_config['profile_task'],
		)
	
	@task
	def resume_strategy_task(self) -> Task:
		return Task(
			config=self.tasks_config['resume_strategy_task'],
			output_file='tailored_resume.md'
		)
	
	@task
	def interview_preparation_task(self) -> Task:
		return Task(
			config=self.tasks_config['interview_preparation_task'],
			output_file='interview_materials.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Ai1 crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
