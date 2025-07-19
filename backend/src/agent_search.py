from google.adk.agents import Agent
from google.adk.tools import google_search
from google.genai import types

agent_search = Agent(
    name="AgentSearch",
    model="gemini-2.0-flash",
    instruction="Answer any general query using the google_search tool.",
    tools=[google_search],
    description="Agent that answers using Google search only.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.0,
    ),
)
