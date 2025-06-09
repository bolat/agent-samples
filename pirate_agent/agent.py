from google.adk.agents import Agent
from google.adk.events import Event, EventActions
from google.genai import types
#from google.adk.models.lite_llm import LiteLlm
import datetime
import os
from dotenv import load_dotenv, dotenv_values

# Load environment variables from .env file
load_dotenv()
# config = dotenv_values(".env")


# # Print the loaded environment variables for debugging
# for key, value in config.items():
#     print(f"{key}={value}")
# Set the environment variable for the Google GenAI API key
# os.environ["GOOGLE_API_KEY"] = config.get("GOOGLE_GENAI_API_KEY", "")

AGENT_MODEL = "gemini-2.0-flash"

# Root agent using auto-discovered tools
root_agent = Agent(
    name="pirate_agent",
    model=AGENT_MODEL,
    description="Acts like a pirate",
    instruction="You are a pirate called Jolly Roger. You will act as a pirate including personality traits and respond to user queries in a pirate-like manner. Use your tools to assist with tasks.",
)