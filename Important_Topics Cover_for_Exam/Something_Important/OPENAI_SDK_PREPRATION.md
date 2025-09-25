### 🔧 FUNCTION CALLING, AGENTS & RUNNERS

#### 1. **LLM responses in different scenarios**

* **Depends on prompt, tools, system instructions, and streaming.**
* LLM responses may be:

  * Pure text (chat completion)
  * Tool calls (functions, retrieval, code interpreter, etc.)
  * Partial (in streaming)
  * Final (after tool completion and follow-up)

#### 2. **Function Tool**

* Allows the LLM to call specific, structured functions you define.
* You define:

  * `name`
  * `description`
  * `parameters` (as a schema)

#### 3. **Agent class required parameter**

* Required parameters include:

  * `tools` (list of tools/functions)
  * `model` (model name or object)
  * `system_message` (optional)
  * `max_turns`, `stream`, `instructions` (optional, but useful)

#### 4. **Difference between `Runner.run()` and `Runner.run_sync()`**

* `run()` → **async**, used in `async` context.
* `run_sync()` → **sync** version, blocks the main thread.
* Use based on your app structure (e.g., FastAPI supports async).

#### 5. **`Runner.run_streamed()`**

* Streams output in chunks (token-by-token).
* Useful for real-time UX (like typing animation).
* You can use `.print_response_stream()` to render it nicely.

#### 6. **Jab run hota hai to konsa loop chalta hai?**

* Event loop in **asyncio** is used.
* Especially with `await` calls, like `await runner.run()`

#### 7. **Tripwire triggered hota hai to kya output ata hai?**

* **Tripwire** is used to **detect excessive iterations, loops, or invalid outputs.**
* If triggered, an error is raised (like `TooManyToolCalls` or similar).
* Output will typically be an exception or a fallback.

---

### 🧠 AGENTS

#### 8. **How are dynamic instructions given?**

* Passed via the `instructions` parameter in the Agent class or Runner.
* Can change behavior on the fly.
* Example: `"You're an expert travel planner. Respond concisely."`

#### 9. **From which class is the Agent inherited?**

* Depends on the library.
* In **OpenAI's python agent framework** (e.g., experimental agents), Agent typically inherits from a **base class** like `OpenAIAgent` or `RunnableAgent`.

#### 10. **By default, the Agent model is ready**

* Yes, usually defaults to `gpt-4-turbo` or `gpt-3.5-turbo` unless specified.
* Model is "ready" once tools and system instructions are given.

#### 11. **`max_turns=1` aur tool call ho raha ho to kya hota hai?**

* If `max_turns=1`:

  * Agent gets only **one interaction turn**.
  * If a **tool call is needed**, it may not complete in time.
  * May lead to **incomplete task** or error like `ToolCallLimitExceeded`.

---

### 🌐 UI & MARKDOWN

#### 12. **Clickable image with tooltip**

* In HTML inside Markdown (on platforms that support it):

```html
<a href="https://example.com" title="Click to visit">
  <img src="image_url.jpg" alt="Alt text" width="100">
</a>
```

#### 13. **Top p, temperature, etc.**

* **top\_p**: nucleus sampling – chooses from top tokens until cumulative probability hits `p`.
* **temperature**: randomness – higher value = more creative, lower = more deterministic.
* Example: `temperature=0.2`, `top_p=0.9` for safer outputs.

#### 14. **Ordered list in Markdown**

```markdown
1. First item
2. Second item
3. Third item
```

---

### 🪝 ADVANCED: HOOKS, MODELS, VALIDATION

#### 15. **Hooks**

* Custom functions that run **before or after** model/tool calls.
* Used to:

  * Pre-process input
  * Log events
  * Filter outputs
* Not available in all LLM frameworks yet.

#### 16. **Model behavior error**

* Could refer to:

  * Unexpected output
  * Token limit errors
  * Tool calling failures
  * Hallucination
  * Use logs to debug

#### 17. **Schemas and Validation**

* Functions/tools use JSON Schema (`type`, `properties`, `required`)
* Ensures structured input/output.
* LLM validates before calling a function.

#### 18. **Pydantic data class**

* Used to define structured data for tools/functions:

```python
from pydantic import BaseModel

class WeatherInput(BaseModel):
    city: str
    date: Optional[str] = None

```
