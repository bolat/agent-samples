from google.adk.agents import Agent
from google.adk.events import Event, EventActions
from google.genai import types
from google.adk.models.lite_llm import LiteLlm
import datetime

from time_agent import tools

AGENT_MODEL = "gemini-2.0-flash"

# Root agent using auto-discovered tools
root_agent = Agent(
    name="time_agent",
    model=AGENT_MODEL,
    description="Acts like a time assistant",
    instruction="You are a helpful time assistant. Your primary goal is to provide the current time for given timezones or cities. "
                "When the user asks for the time in a specific city or time zone "
                "you MUST use the 'get_current_time' tool to find the information. "
                "Analyze the tool's response: if the status is 'error', inform the user politely about the error message. "
                "If the status is 'success', present the information clearly and concisely to the user. "
                "Only use the tools when appropriate for a time-related request.",
    tools=[tools.get_current_time],#discover_adk_tools(time_agent.tools),
)