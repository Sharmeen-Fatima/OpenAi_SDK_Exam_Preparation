from agents import (Agent,
                    Runner, 
                    OpenAIChatCompletionsModel, 
                    AsyncOpenAI, 
                    RunConfig
                   )
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = AsyncOpenAI(
    api_key=api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = client
)
config = RunConfig(
    model = model,
    tracing_disabled = True,
    model_provider = client
)
async def main():
    agent = Agent(
        name= "Agentic AI SDK Task Agent",
        instructions= "you are an expert in Agentic Ai SDK, perform tasks"
    )
    result = await Runner.run(
        agent,
        "Tell me about prompt engineering in AI.",
        run_config=config
    )
    print(result.final_output)
# print("API Key: ", api_key)
if __name__ == "__main__":
    asyncio.run(main())