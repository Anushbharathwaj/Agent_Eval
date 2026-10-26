<div align="center">

<svg width="100%" height="150" viewBox="0 0 800 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16" />
      <stop offset="100%" stop-color="#1e1b4b" />
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="800" height="150" rx="12" fill="url(#bgGrad)" />
  <circle cx="100" cy="75" r="45" fill="#38bdf8" opacity="0.1" filter="url(#glow)" />
  <text x="50%" y="65" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="42" fill="url(#textGrad)" text-anchor="middle" letter-spacing="2">
    🤖 AGENT_EVAL
  </text>
  <text x="50%" y="102" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="15" fill="#94a3b8" text-anchor="middle" letter-spacing="1">
    Evaluating Tool-Using AI Agents with LangChain, LangGraph &amp; DeepEval
  </text>
</svg>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/LangChain-Agent%20Framework-1C3C3C?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/LangGraph-Workflows-2563EB?style=flat-square&logo=git&logoColor=white" alt="LangGraph">
  <img src="https://img.shields.io/badge/OpenAI-API-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/DeepEval-LLM%20Evaluation-7C3AED?style=flat-square&logo=codeforces&logoColor=white" alt="DeepEval">
  <img src="https://img.shields.io/badge/uv-Dependency%20Management-DE5FE9?style=flat-square&logo=astral&logoColor=white" alt="uv">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
</p>

<p align="center">
  <a href="https://github.com/Anushbharathwaj/Agent_Eval"><b>🌐 Repository</b></a> &nbsp;·&nbsp;
  <a href="https://github.com/Anushbharathwaj/Agent_Eval/issues"><b>🐛 Report an Issue</b></a>
</p>

</div>

---

## 💡 The Strategic "Why"

Building a reliable AI agent requires more than checking whether its final response is correct. An agent can produce a convincing answer while selecting the wrong tool, passing incorrect arguments, following an unsuitable plan, or performing unnecessary actions. Without systematic evaluation, these execution failures can remain hidden.

`Agent_Eval` demonstrates an evaluation-driven approach to AI agent development through a refund support agent built with **Python**, **LangChain**, **LangGraph**, **OpenAI**, and **DeepEval**. It evaluates both the agent's final responses and its execution behavior across eight refund-related scenarios.

---

## ✨ Key Features

- 🎯 **Task Completion Evaluation:** Assess whether the agent successfully achieves the user's requested outcome.
- 🛠️ **Tool Selection Analysis:** Evaluate whether the agent selects the appropriate tools for each scenario.
- 🧩 **Argument Correctness:** Examine whether the agent supplies suitable arguments when invoking tools.
- 🧠 **Planning Evaluation:** Assess the quality of the execution plan and whether the agent follows it.
- ⚡ **Step Efficiency:** Identify unnecessary or redundant actions during agent execution.
- 💬 **Answer Correctness:** Evaluate whether the final response matches the expected conclusion.
- 📊 **Eight Evaluation Scenarios:** Test eligible refunds, expired refund windows, specific items, missing information, unknown customers, and other cases.
- 🔍 **Execution Tracing:** Inspect agent actions and tool calls to investigate evaluation failures.
- 📦 **Structured Responses:** Use Pydantic models to represent agent responses.
- 🔄 **Conversation State:** Demonstrate conversation state management using LangGraph checkpointing.
- 🖥️ **Optional Interactive Interface:** Explore the agent through a Streamlit interface when configured.
- ⚙️ **Reproducible Environment:** Manage Python dependencies using `uv` and `uv.lock`.

---

## 🏗️ Technical Architecture

`Agent_Eval` is organized around three core stages: agent execution, tool interaction, and evaluation.

### Core Technologies

| Technology | Purpose | Key Benefit |
| :--- | :--- | :--- |
| **Python 3.12+** | Programming language | Flexible AI development |
| **LangChain** | Agent development | Tool integration and orchestration |
| **LangGraph** | Workflow management | Stateful execution and checkpointing |
| **OpenAI** | Language model | Agent responses |
| **DeepEval** | Agent evaluation | Response and execution assessment |
| **Pydantic** | Data validation | Structured responses |
| **uv** | Dependency management | Reproducible environments |
| **python-dotenv** | Configuration | Environment variable management |
| **Streamlit** | Optional interface | Interactive chat application |

### Evaluation Workflow

```text
 ┌────────────────────────────────────────┐
 │            Customer Request            │
 └───────────────────┬────────────────────┘
                     │
                     ▼
 ┌────────────────────────────────────────┐
 │             LangChain Agent            │
 └───────────────────┬────────────────────┘
                     │
                     ▼
 ┌────────────────────────────────────────┐
 │           LangGraph Workflow           │
 └───────────────────┬────────────────────┘
                     │
                     ▼
 ┌────────────────────────────────────────┐
 │             Tool Selection             │
 └───────────────────┬────────────────────┘
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
     ┌───────┐   ┌───────┐   ┌──────────┐
     │Purchase│   │Refund │   │Simulated │
     │ Lookup │   │ Calc  │   │  Ticket  │
     └───┬────┘   └───┬───┘   └────┬─────┘
         └───────────┼────────────┘
                     │
                     ▼
 ┌────────────────────────────────────────┐
 │             Agent Response             │
 └───────────────────┬────────────────────┘
                     │
                     ▼
 ┌────────────────────────────────────────┐
 │           Structured Output            │
 └───────────────────┬────────────────────┘
                     │
                     ▼
 ┌────────────────────────────────────────┐
 │          DeepEval Evaluation           │
 └───────────────────┬────────────────────┘
                     │
                     ▼
 ┌────────────────────────────────────────┐
 │        Scores and Explanations         │
 └────────────────────────────────────────┘
```

### Directory Structure

```text
Agent_Eval/
├── 📁 agent/                         # Refund support agent implementation
│   ├── 📄 agent.py                   # Agent initialization and execution
│   ├── 📄 data.py                    # Sample customer purchase records
│   ├── 📄 models.py                  # Language model configuration
│   ├── 📄 objects.py                 # Pydantic response models
│   ├── 📄 prompts.py                 # System instructions and refund policy
│   ├── 📄 tools.py                   # Refund-related tool definitions
│   └── 📄 streamlit_ui.py            # Optional Streamlit interface
├── 📁 evaluations/                   # Agent evaluation workflow
│   ├── 📄 dataset.py                 # Evaluation scenarios and expected results
│   ├── 📄 eval_all.py                # Main evaluation runner
│   ├── 📄 model.py                   # Evaluation model configuration
│   ├── 📄 task_completion.py         # Task completion evaluation
│   ├── 📄 step_efficiency.py         # Execution efficiency evaluation
│   ├── 📄 plan_quality.py            # Planning quality evaluation
│   ├── 📄 plan_adherence.py          # Plan adherence evaluation
│   ├── 📄 argumentcorrectness.py     # Tool argument evaluation
│   ├── 📄 answercorrectness.py       # Final answer evaluation
│   └── 📄 tool_correctness.py        # Tool selection evaluation
├── 📁 understanding_metrics/         # Individual metric examples
├── 📁 src/                           # Additional source code
├── 🖼️ DatasetJsonView.png             # Evaluation dataset illustration
├── 📄 .env.example                   # Example environment configuration
├── 📄 .gitignore                     # Git exclusion rules
├── 📄 pyproject.toml                 # Project metadata and dependencies
├── 📄 uv.lock                        # Locked dependency versions
└── 📄 README.md                      # Project documentation
```

---

## 🚀 Operational Setup

### Prerequisites

- **Python:** Version 3.12 or later.
- **uv:** Python package and environment manager.
- **Git:** For cloning and managing the repository.
- **OpenAI API Key:** With access to the model configured by the project.

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anushbharathwaj/Agent_Eval.git
   cd Agent_Eval
   ```

2. **Install Python 3.12 (via uv):**
   ```bash
   uv python install 3.12
   ```

3. **Install project dependencies:**
   ```bash
   uv sync --locked
   ```

4. **Configure environment variables:**
   Create a `.env` file in the project root using `.env.example` as a template, and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   > 🔒 **Security Notice:** Never commit `.env` files or API keys to GitHub. Ensure `.env` is included in your `.gitignore`.

---

## 🏃 Running the Agent

### Command Line Execution
Verify the entry points inside `agent/agent.py` to run the agent directly:
```bash
uv run --env-file .env python agent/agent.py
```

### Optional Streamlit Interface
Launch the interactive web UI using Streamlit:
```bash
uv run --env-file .env --with streamlit python -m streamlit run agent/streamlit_ui.py
```
Open the local URL printed in your terminal to access the application interface.

---

## 🧪 Running Evaluations

### Run Complete Evaluations
Run the primary evaluation runner (`evaluations/eval_all.py`):
```bash
uv run --env-file .env python evaluations/eval_all.py
```
> ⚠️ **Note:** LLM-based evaluations make API calls and may incur costs.

### Run Individual Metrics
You can execute specific evaluation scripts independently:
```bash
uv run --env-file .env python evaluations/task_completion.py
uv run --env-file .env python evaluations/tool_correctness.py
uv run --env-file .env python evaluations/answercorrectness.py
```

---

## 📊 Evaluation Metrics & Scenarios

### Framework Dimensions

| Metric | Purpose | Evaluation Question |
| :--- | :--- | :--- |
| **Task Completion** | Measures successful task completion | Did the agent achieve the intended outcome? |
| **Step Efficiency** | Evaluates execution efficiency | Did the agent avoid redundant actions? |
| **Plan Quality** | Assesses the quality of the plan | Was the execution plan appropriate? |
| **Plan Adherence** | Examines adherence to the plan | Did the agent follow its plan during execution? |
| **Argument Correctness** | Evaluates tool arguments | Were the arguments appropriate for the request? |
| **Tool Correctness** | Evaluates tool selection | Did the agent select the expected tools? |
| **Answer Correctness** | Assesses the final response | Did the answer reach the expected conclusion? |

### Evaluation Scenarios (`evaluations/dataset.py`)

- **Eligible refund:** Calculate the refund and create a simulated ticket.
- **Expired refund window:** Explain why the purchase is ineligible for a refund.
- **Specific item refund:** Calculate the refund for the requested item only.
- **Multiple-item refund:** Calculate the combined refund amount for the requested items.
- **Information-only request:** Answer the question without creating a refund ticket.
- **Missing username:** Ask the user to provide the missing information.
- **Unknown customer:** Explain that the customer could not be found.
- **Unpurchased item:** Explain that the requested item is absent from purchase history.

![Evaluation dataset JSON structure](DatasetJsonView.png)

---

<div align="center">

Built with Python, LangChain, LangGraph, OpenAI, and DeepEval.

[Explore Agent_Eval on GitHub](https://github.com/Anushbharathwaj/Agent_Eval)

</div>