from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    function_tool,
    set_tracing_disabled,
    set_default_openai_client,
    RunConfig
)
from dotenv import load_dotenv
import os 

load_dotenv()
set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

set_default_openai_client(external_client)

model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
@function_tool
def fetch_weather(city: str) -> str:
     """Fetch the current weather for a given city."""
     return f"The current weather in {city} is sunny with a temperature of 25°C."

@function_tool
def fetch_news(topic: str) -> str:
     """Fetch the latest news headlines for a given topic."""
     return f"The latest news on {topic} includes major developments in the field."

agent: Agent = Agent(
    name="Fetcher_Data",
    instructions=(
        "You are a helpful assistant. "
        "Use tools to fetch weather and news information. "
        "Always use simple and easy words to explain for beginners. "
        "Explain answers clearly and briefly."
    ),
    tools=[fetch_weather, fetch_news],  
    model=model,                        
)

config = RunConfig(tracing_disabled=True)

prompt = "What is the current weather in New York."
result = Runner.run_sync(agent, 
                         prompt, 
                         run_config=config)

print(result.final_output)
