from crewai import Agent, Task, Crew
from utils import get_openai_api_key
import warnings
import os

warnings.filterwarnings('ignore')

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4'

def create_crew():
    researcher = Agent(
        role="Researcher",
        goal="",
        backstory="",
        allow_delegation=False,
        verbose=True
    )

    analyst = Agent(
        role="Data Analyst",
        goal="",
        backstory="",
        allow_delegation=False,
        verbose=True
    )

    reviewer = Agent(
        role="Reviewer",
        goal="",
        backstory="",
        allow_delegation=False,
        verbose=True
    )

    research = Task(
        description="Conduct the research",
        expected_output="",
        agent=researcher
    )

    analyze = Task(
        description="Analyze the research data",
        expected_output="",
        agent=analyst
    )

    review = Task(
        description="Review and assess the research findings",
        expected_output="",
        agent=reviewer
    )

    crew = Crew(
        agents=[researcher, analyst, reviewer],
        tasks=[research, analyze, review],
        verbose=True
    )

    return crew