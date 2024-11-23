from crewai import Agent, Task, Crew
from utils import get_openai_api_key
import warnings
import os

warnings.filterwarnings('ignore')

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4'

def create_crew(transcript_response=None, reference_content=None):
    researcher = Agent(
        role="Researcher",
        goal="To conduct comprehensive research on the given topic",
        backstory="An AI agent trained to perform deep and thorough research on a wide range of topics",
        allow_delegation=False,
        verbose=True
    )

    analyst = Agent(
        role="Data Analyst",
        goal="To analyze the data obtained from the research",
        backstory="An AI agent skilled in data analysis and interpretation",
        allow_delegation=False,
        verbose=True
    )

    reviewer = Agent(
        role="Reviewer",
        goal="To review the research findings and provide a summary",
        backstory="An AI agent with expertise in reviewing and summarizing complex research findings",
        allow_delegation=False,
        verbose=True
    )

    research = Task(
        description=f"Research the topic: {transcript_response or 'No topic provided'}\nReference content: {reference_content or 'No reference content provided'}",
        expected_output="A detailed report of the research conducted on the given topic",
        agent=researcher
    )

    analyze = Task(
        description="Analyze the research data",
        expected_output="A comprehensive analysis of the research data",
        agent=analyst
    )

    review = Task(
        description="Review and assess the research findings",
        expected_output="A concise and clear summary of the research findings",
        agent=reviewer
    )

    crew = Crew(
        agents=[researcher, analyst, reviewer],
        tasks=[research, analyze, review],
        verbose=True
    )

    return crew