from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class CodeCrew():
    """CodeCrew crew"""

    agents_config = 'config/agents.yaml' 
    tasks_config = 'config/tasks.yaml'

    @agent
    def team_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['team_lead'], 
            verbose=True
        )

    @agent
    def backend_engg(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engg'], 
            verbose=True,
            allow_code_execution=True,
            code_execution_mode = "safe",
            max_execution_time = 300,
            max_retry_limit=5
        )

    @agent
    def frontend_engg(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engg'], 
            verbose=True,                               # not executing this part
        )

    @agent
    def testing_engg(self) -> Agent:
        return Agent(
            config=self.agents_config['testing_engg'], 
            allow_code_execution=True,
            code_execution_mode = "safe",
            max_execution_time = 300,
            max_retry_limit=3
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task'], 
        )

    @task
    def backend_task(self) -> Task:
        return Task(
            config=self.tasks_config['backend_task']
        )

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_task']
        )

    @task
    def testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['testing_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CodeCrew crew"""
    
        return Crew(
            agents=self.agents,         # all the functions under the agent decorators
            tasks=self.tasks,           # all the functions under the test decorators
            process=Process.sequential,
            verbose=True,
        )
