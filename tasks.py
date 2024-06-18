from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

# Define the research task
research_task = Task(
    description=(
        "Discover the upcoming major trend in {topic}. Focus on outlining"
        "the pros and cons and the overarching narrative. Your final report"
        "should clearly present the key points, market opportunities, and"
        "potential risks."
    ),
    expected_output='A comprehensive 3-paragraph report on the latest AI trends.',
    tools=[tool],
    agent=news_researcher,
)

# Define the writing task with specific language model configuration
write_task = Task(
    description=(
        "Create an insightful article on {topic}. Emphasize the latest"
        "trends and their impact on the industry. Ensure the article is"
        "easy to understand, engaging, and positive."
    ),
    expected_output='A 4-paragraph article on {topic} advancements formatted in markdown.',
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='blog_post.md'  # Specify the output file
)
