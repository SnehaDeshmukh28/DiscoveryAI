from crewai import Agent
from tools import tool
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize the Gemini language model
llm = ChatGoogleGenerativeAI(
    #model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define the senior researcher agent with specific attributes
news_researcher = Agent(
    role="Senior Researcher",
    goal='Discover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Fueled by an insatiable curiosity, you lead the charge in"
        "innovation, eager to uncover and disseminate knowledge that could"
        "transform the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Define the writer agent responsible for creating tech news blogs
news_writer = Agent(
    role='Writer',
    goal='Craft engaging tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a talent for demystifying complex subjects, you write"
        "engaging narratives that both inform and captivate, making new"
        "discoveries accessible to all."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
