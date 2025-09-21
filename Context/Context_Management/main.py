import asyncio
from dataclasses import dataclass
from agents import(
    Agent,
    Runner,
    RunContextWrapper,
    function_tool,
    RunConfig,
    OpenAIChatCompletionsModel,
    AsyncOpenAI
)
from dotenv import load_dotenv
import os
load_dotenv()

api_key =os.getenv("GEMINI_API_KEY")
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
@dataclass
class UserInfo:
    name: str
    roll_number: int

@function_tool
async def fetch_user_roll_number(wrapper: RunContextWrapper[UserInfo]) -> str:
    """Fetch the roll number of the user. Call this function to get user's roll number information."""
    return f"The User {wrapper.context.name} has roll number {wrapper.context.roll_number}"
async def main():
    user_info = UserInfo(
        name="Sharmeena",
        roll_number=241063
    )
    agent = Agent[UserInfo](
        name="Assistant",
        tools=[fetch_user_roll_number],
    )
    result = await Runner.run(
        starting_agent=agent,
        input="What is the user roll number?",
        context=user_info,
        run_config=config
    )
    print (result.final_output)
    # print(result.last_agent)
    # print(result.last_response_id)
if __name__ == "__main__":
     asyncio.run(main())