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
#### 2. Runner 🏃🏻‍♂️

- Used to run the <code>agent.</code> ⭐
- It manages the interaction between the <code>agent</code> and the model. 💻
- Here, <code>Runner.run_sync(...)</code> is used — which means it is running in <code>**synchronous (non-async)**</code> mode. 💡

---
#### 3. <code>OpenAIChatCompletionsModel</code> 💡

- This class defines a model that follows the <code>**OpenAI-style chat completion API**</code>. ✍🏻
- In this example, <code>**Gemini**</code> has also been wrapped to behave like this API. ✒

---
#### 4. AsyncOpenAI 🤖

- An <code>async</code>-compatible client for <code>OpenAI-style</code> APIs (including <code>Gemini,</code> if it follows the same API format). ⭐
- It handles API <code>requests</code> to Gemini. 💎

---
#### 5. RunConfig 🏃🏻‍♂️

- This object defines the **global configuration** for running the agent: ⭐
    - Which model will be used
    - Whether tracing is enabled or disabled
    - Which provider will run the model
- Think of it as a **global behavior controller** for the agent's execution. ✨

---
#### 6. <code>from dotenv import load_dotenv</code> 💻

- Loads environment variables from a `.env` file.👍
- It's a **secure way to store sensitive information** like API keys, tokens, and other configuration values. 😏

---
#### 7. os 💻

- A built-in Python module used to **interact with the operating system**, especially for accessing **environment variables** (e.g., `os.getenv()` to read values). ✒

---
#### 8. `load_dotenv()`🔐

- Loads the `.env` file so that you can access its values using `os.getenv(...)`. 📚
- It ensures environment variables are available in your Python code. 🎯

---
#### 9. Connect_API_KEY. 💡

- `api_key = os.getenv("GEMINI_API_KEY")` 👍
- Securely fetches the **Gemini API key** from the `.env` file using `os.getenv(...)`. 🔐
- This keeps the key private and out of your source code. 💻

-----
### **Client, Model, and Config Setup**

🔹 **AsyncOpenAI(...)**

```python
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
```
This creates an **asynchronous client** to connect with the **Gemini API**.

* `base_url` is the **endpoint** for the Gemini API.
* This client will handle **all model-related calls and requests**.

---

### **Model Setup**

🔹 **`OpenAIChatCompletionsModel(...)`**

```python
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)
```
In this line, the **Gemini model** is wrapped using an **OpenAI-style interface**.

* This allows the **OpenAI Agents SDK** to interact with the Gemini model **as if it were a standard OpenAI model**.
* It ensures compatibility and smooth integration with tools designed for the OpenAI ecosystem.
---
