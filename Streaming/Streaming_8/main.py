import asyncio
import random
from agents import (
                    Agent,
                    OpenAIChatCompletionsModel,
                    RunConfig,
                    Runner, 
                    function_tool,
                    AsyncOpenAI,
                    ItemHelpers
                    )

from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    base_url="https://generativegoogleapi.com/v1beta/openai/",
    api_key=api_key
)

model = OpenAIChatCompletionsModel(
    model= "gemini-2.5-flash",
    openai_client=client
)

@function_tool
def how_many_jokes(joke: str) -> str:
    """tell the 6 jokes."""
    return f"I wil not tell about this {joke}, Because listen to me I'm also Joke."

async def main():
    agent = Agent(
        instructions="You are a helpful assistant. First, determine how many jokes to tell, then provide jokes.",
        tools=[how_many_jokes],
    )

    config = RunConfig(tracing_disabled=True)

    result = Runner.run_streamed(
        agent, 
        input="Hello",
        run_config=config
        )

    async for event in result.stream_events():
        if event.item.type == "tool_call_output_item":
            print(f"Tool output: {event.item.output}")
        elif event.item.type == "message_output_item":
            print(ItemHelpers.text_message_output(event.item))

asyncio.run(main())