from google.adk.agents import BaseAgent
from src.agent_search import agent_search
from src.agent import custom_tools_agent


class SmartOrchestrator(BaseAgent):
    def __init__(self):
        super().__init__(
            name="SmartOrchestrator",
            description="Routes queries to search-agent or custom-tools agent.",
        )
        self._search = agent_search
        self._custom = custom_tools_agent

    async def _run_async_impl(self, context):
        if hasattr(context, "parts"):
            user_text = context.parts[0].text
        elif hasattr(context, "content"):
            user_text = context.content
        else:
            user_text = str(context)
        user_text = user_text.lower()

        if "horse" in user_text or "dice" in user_text:
            target = self._custom
        else:
            target = self._search

        async for event in target.run_async(context):
            yield event


root_agent = SmartOrchestrator()
