# IT'S A SIMPLE AGENT

## THE THING WE HAVE LEARN IN THIS SIMPLE AGENT

#### Highlights ✨

- Agent
- Runner
- OpenAIChatCompletionsModel
- AsyncOpenAI
- RunConfig
- from dotenv import load_dotenv
- os
- Connect API Key

---
#### 1. <code>Agent</code> 🤖

- Represents the LLM (Large Language Model) <code>agent.</code>😏
- You can give it instructions (for example, "act like a helpful assistant").✨
- This <code>agent</code> will later take input and send a query to the model. ⭐

---
#### 2. Runner

- Used to run the <code>agent.</code>
- It manages the interaction between the <code>agent</code> and the model.
- Here, <code>Runner.run_sync(...)</code> is used — which means it is running in <code>**synchronous (non-async)**</code> mode.

---
#### 3. <code>OpenAIChatCompletionsModel</code>

- This class defines a model that follows the <code>**OpenAI-style chat completion API**</code>.
- In this example, <code>**Gemini**</code> has also been wrapped to behave like this API.

---
#### 4. AsyncOpenAI

- An <code>async</code>-compatible client for <code>OpenAI-style</code> APIs (including <code>Gemini,</code> if it follows the same API format).
- It handles API <code>requests</code> to Gemini.

---
#### 5. RunConfig

- This object defines the **global configuration** for running the agent:
    - Which model will be used
    - Whether tracing is enabled or disabled
    - Which provider will run the model
- Think of it as a **global behavior controller** for the agent's execution.

---
#### 6. <code>from dotenv import load_dotenv</code>

- Loads environment variables from a `.env` file.
- It's a **secure way to store sensitive information** like API keys, tokens, and other configuration values.

---
#### 7. os

- A built-in Python module used to **interact with the operating system**, especially for accessing **environment variables** (e.g., `os.getenv()` to read values).

---
#### 8. `load_dotenv()`

- Loads the `.env` file so that you can access its values using `os.getenv(...)`.
- It ensures environment variables are available in your Python code.

