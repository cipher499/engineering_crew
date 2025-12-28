from code_crew.crew import CodeCrew
from crewai import Crew, Process

code_crew = CodeCrew()

# get agent + task objects
frontend_agent = code_crew.frontend_engg()
frontend_task = code_crew.frontend_task()

# build a minimal crew
frontend_crew = Crew(
    agents=[frontend_agent],
    tasks=[frontend_task],
    process=Process.sequential,
    verbose=True,
)

frontend_crew.kickoff()
