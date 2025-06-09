from google.adk.agents import Agent
from google.adk.events import Event, EventActions
from google.genai import types
from google.adk.models.lite_llm import LiteLlm
import datetime

AGENT_MODEL = "gemini/gemini-2.0-flash"

# Root agent using auto-discovered tools
root_agent = Agent(
    name="test_agents",
    model=LiteLlm(model=AGENT_MODEL),
    description="Acts like a time assistant",
    instruction="You are a helpful time assistant. Your primary goal is to provide the current time for given timezones or cities. "
                "When the user asks for the time in a specific city or time zone "
                "you MUST use the 'get_time' tool to find the information. "
                "Analyze the tool's response: if the status is 'error', inform the user politely about the error message. "
                "If the status is 'success', present the information clearly and concisely to the user. "
                "Only use the tools when appropriate for a time-related request.",
    tools=discover_adk_tools(test_agent.tools),
)