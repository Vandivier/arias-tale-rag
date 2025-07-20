from google.adk.agents import Agent
from src.utils import create_horse_fact, roll_a_dice
from google.genai import types

# TODO: RAG instance, or RAG as a tool?
arias_tale_rag = create_horse_fact

root_agent = Agent(
    name="arias_tale_rag_agent",
    model="gemini-2.0-flash",
    instruction=(
        "You are a helpful research assistant that knows Aria's Tale lore. "
        "Roll a six-sided die if the user requests it."
        "For other tasks, use the Aria's Tale RAG to bring in useful information, then think about the user's question and answer it."
    ),
    description="An agent that can answer questions.",
    tools=[arias_tale_rag, roll_a_dice],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.0,
    ),
)
