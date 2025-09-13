from agents import (
    Agent, 
    Runner, 
    OpenAIChatCompletionsModel,
    RunConfig,
    AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled, 
    set_default_openai_api
)
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

agent: Agent = Agent(
    name="Greeting_Agent",
    instructions="Regardless of the greeting you receive (e.g., 'Hi', 'Hey', 'Hello', or any other language greeting), always respond with: 'Asalam O Alaikum  My creator is Muslim. so I'm Muslim Agent'",
    model="gemini-2.0-flash"
)

result = Runner.run_sync(
    agent, 
    "Hello"
)

print(result.final_output)