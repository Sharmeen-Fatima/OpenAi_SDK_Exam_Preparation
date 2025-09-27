import asyncio
from dataclasses import dataclass
from agents import (Agent,
                    Runner,
                    OpenAIChatCompletionsModel,
                    RunContextWrapper,
                    function_tool,
                    AsyncOpenAI,
                    RunConfig,
                    handoff)
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    tracing_disabled=True,
    model=model,
    model_provider=client
)

@dataclass
class UserInfo:
    name: str
    father: str
    roll: int

@function_tool
async def fetch_use_roll(wrapper: RunContextWrapper[UserInfo]) -> str:
    """Fetch the user name and roll number. Call this function to get user's name and roll"""
    return f"The user {wrapper.context.name} have a {wrapper.context.roll}"

async def main():
    user_info = UserInfo(
        name="Ali-Haider",
        father="Shujauddin",
        roll=241063
    )

    agent = Agent[UserInfo](
        name="User Info",
        tools=[fetch_use_roll]
)
if __name__ == "__main__":
    asyncio.run(main())

@dataclass
class NewUserInfo:
    name: str
    father: str
    CNIC: int
    Email: str
    RegistrationID: int

@function_tool
async def fetch_user_RegistrationID(wrapper: RunContextWrapper[NewUserInfo]) -> int:
    """Fetch the new user name and registrationid and CNIC. Call this function to get user's name, RegistrationID and CNIC"""
    return f"The Student name is {wrapper.context.name} father name {wrapper.context.father} CNIC NO: {wrapper.context.CNIC} and {wrapper.context.name} has a Registration ID {wrapper.context.RegistrationID}"

async def newuser():
    new_user = NewUserInfo(
        name:="Sharmeen Fatima",
        father:= "Shuja uddin",
        CNIC:= 42401-5555555-8,
        Email:= "Creative.coder@hotmail.com",
        RegistrationID= 103018
)
    agent = Agent[NewUserInfo](
        name="New Registration Agent",
        tools=[fetch_user_RegistrationID]
    )
if __name__ == "__main__":
    asyncio.run(newuser())

async def triageagent():
    user_agent = Agent[UserInfo](
        name="User Info",
        tools=[fetch_use_roll]
    )
    new_agent = Agent[NewUserInfo](
        name="New Registration Agent",
        tools=[fetch_user_RegistrationID]
    )

    TriageAgent = Agent(
        name="Triage Agent",
        handoffs=[user_agent, handoff(new_agent)],
        handoff_description="If User provide RegistrationID you should handoff NewUserInfo else UserInfo"
    )
    return TriageAgent

async def run_runner():
    triage_agent = await triageagent()
    while True:
        user_input = input("Write anything you want (type 'exit' to quit): ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        if "would you like me to do that" in user_input.lower():
            user_input = "yes" 
        result = await Runner.run(
            triage_agent,
            input=user_input,
            run_config=config
        )
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(run_runner())