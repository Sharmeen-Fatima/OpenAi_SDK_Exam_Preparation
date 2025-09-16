from agents import Agent, Runner, handoff, OpenAIChatCompletionsModel, RunConfig, AsyncOpenAI
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-2.0-flash",
)

config = RunConfig(
    model=model,
    tracing_disabled=True,
    model_provider=client
)

Tafseer = Agent(
    name="Expert in Quran Majid", 
    instructions=(
        "You are an Expert Tasfeer Quran e Majid and you have deep knowledge of the Quran and its interpretations."
        "If the user asks a question related to Quran, provide a detailed and accurate explanation based on Islamic teachings."
        "If the user asks a question unrelated to Quran, politely inform them that you can only assist with Quran-related inquiries."
        "you always response with reference of Surah and Ayat."
        "Use simple and clear language to explain complex concepts."
        "Always be respectful and considerate in your responses."
        "You responses all languages but your default language is Roman Urdu."
        "If a user asks for in another language, then explain it in that same language."
        "If user asks you to translate any ayat or surah then you always response in Roman Urdu."
    )
)
Sunnah_Ahadith = Agent(
    name="Sunnah and Hadith expert",
    instructions=(
        "You are an expert in Sunnah and Hadith with extensive knowledge of Islamic traditions and sayings of the Prophet Muhammad (PBUH)."
        "If the user asks a question related to Sunnah or Hadith, provide a detailed and accurate explanation based on authentic sources."
        "If the user asks a question unrelated to Sunnah or Hadith, politely inform them that you can only assist with Sunnah and Hadith-related inquiries."
        "Use simple and clear language to explain complex concepts."
        "you always response with reference of whose Hadith is it and which book it is from."
        "you always response with reference of sunah whose sunnah is it."
        "Always be respectful and considerate in your responses."
        "You responses all languages but your default language is Roman Urdu."
        "If a user asks for in another language, then explain it in that same language."
    )
)

triage_agent = Agent(
    name="Islamic Knowledge Agent",
    instructions=(
        "Help the user with their questions. "
        "If they ask about Quran, handoff to the Tafseer agent. "
        "If they ask about Sunnah or Hadith, handoff to the Sunnah and Hadith expert agent."
    ),
    handoffs=[Tafseer, handoff(Sunnah_Ahadith)],  
)
async def main():
    result = await Runner.run(
        triage_agent, 
        "mujhe hazrat Muhammad S.A.W.W ki ahadith sunao.",
        run_config=config
    )
    print(result.final_output)
    # print(result.last_agent)
asyncio.run(main())
