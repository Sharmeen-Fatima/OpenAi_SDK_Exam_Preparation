from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)
config = RunConfig(
    model=model,
    tracing_disabled=True,
    model_provider=client
)
agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant that provides accurate information.",
)

result = Runner.run_sync(
    agent,
    input="What is the capital of France?",
    run_config=config
)

print(result.final_output)