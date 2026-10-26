🤖 Agent_Eval
Evaluating Tool-Using AI Agents with LangChain and DeepEval

Build, test, and evaluate an AI-powered refund support agent using Python, LangChain, LangGraph, OpenAI, and DeepEval.

Agent_Eval explores how to evaluate an AI agent beyond its final answer by examining tool selection, argument correctness, planning, execution efficiency, and task completion.

<p align="center">
<img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white" alt="Python 3.12+">
<img src="https://img.shields.io/badge/LangChain-Agents-1C3C3C" alt="LangChain">
<img src="https://img.shields.io/badge/LangGraph-Workflows-E67E22" alt="LangGraph">
<img src="https://img.shields.io/badge/DeepEval-LLM%20Evaluation-6C5CE7" alt="DeepEval">
<img src="https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white" alt="OpenAI">
</p>

<p align="center">
<a href="https://github.com/Anushbharathwaj/Agent_Eval">Repository</a> ·
<a href="https://github.com/Anushbharathwaj/Agent_Eval/issues">Issues</a>
</p>

📌 Table of Contents
Overview
Key Features
Technology Stack
Architecture
Project Structure
Getting Started
Running the Agent
Running Evaluations
Evaluation Metrics
Evaluation Dataset
Understanding Results
Limitations
Future Improvements
Contributing
License
🎯 Overview

A reliable AI agent must do more than generate a plausible response. It should select the correct tools, pass valid arguments, follow an appropriate execution plan, and complete the requested task without unnecessary actions.

Agent_Eval provides an evaluation workflow for investigating these behaviors through a refund support agent and a dataset of eight scenarios.

The agent can:

Retrieve customer purchase history.
Check purchase dates and refund eligibility.
Calculate refunds for individual or multiple items.
Generate simulated refund ticket confirmations.
Return structured responses using Pydantic.
Maintain conversation state using LangGraph checkpointing.

DeepEval evaluates the agent's final responses and execution behavior against expected outcomes.

✨ Key Features
Feature	Description
🧠 AI Agent	Refund support workflow powered by LangChain
🛠️ Tool Calling	Purchase lookup, date retrieval, refund calculation, and simulated ticket creation
📦 Structured Output	Pydantic-based response models
🔄 Conversation State	LangGraph checkpointing
🧪 Evaluation Dataset	Eight refund-related test scenarios
📊 Seven Metrics	Evaluate answer quality and execution behavior
🔍 Execution Tracing	Inspect agent actions and tool calls
💬 Interactive UI	Optional Streamlit interface
⚡ Dependency Management	Reproducible environment using uv
🧰 Technology Stack
Technology	Purpose
Python 3.12+	Core programming language
LangChain	Agent orchestration and tool integration
LangGraph	Stateful workflows and checkpointing
OpenAI	Language model for agent execution and evaluation
DeepEval	LLM evaluation and execution tracing
Pydantic	Structured data and response validation
uv	Python environment and dependency management
python-dotenv	Environment variable configuration
Streamlit	Optional interactive chat interface
🏗️ Architecture

The project follows an evaluation-driven workflow.

mermaid
flowchart TD
    A["Customer Request"] --> B["LangChain Agent"]
    B --> C["LangGraph Workflow"]
    C --> D["Tool Selection"]
    D --> E["Purchase Lookup"]
    D --> F["Refund Calculation"]
    D --> G["Simulated Ticket Creation"]
    E --> H["Agent Response"]
    F --> H
    G --> H
    H --> I["Structured Output"]
    I --> J["DeepEval Evaluation"]
    K["Evaluation Dataset"] --> J
    L["Execution Traces"] --> J
    J --> M["Scores and Explanations"]

    classDef agent fill:#DCEAFE,stroke:#2563EB,color:#172554
    classDef evaluation fill:#EDE9FE,stroke:#7C3AED,color:#3B0764
    class B,C,D,H,I agent
    class J,K,L,M evaluation


The evaluation workflow compares actual agent behavior with expected outcomes to identify incorrect answers, inappropriate tool calls, invalid arguments, and inefficient execution.

📂 Project Structure
text
Agent_Eval/
├── agent/
│   ├── agent.py
│   ├── data.py
│   ├── models.py
│   ├── objects.py
│   ├── prompts.py
│   ├── tools.py
│   └── streamlit_ui.py
│
├── evaluations/
│   ├── dataset.py
│   ├── eval_all.py
│   ├── model.py
│   ├── task_completion.py
│   ├── step_efficiency.py
│   ├── plan_quality.py
│   ├── plan_adherence.py
│   ├── argumentcorrectness.py
│   ├── answercorrectness.py
│   └── tool_correctness.py
│
├── understanding_metrics/
├── src/
├── DatasetJsonView.png
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md

Core Modules
Module	Responsibility
agent/agent.py	Agent implementation
agent/tools.py	Tool definitions and refund operations
agent/prompts.py	System instructions and refund policy
agent/data.py	Sample customer purchase records
agent/objects.py	Pydantic response models
agent/models.py	Language model configuration
evaluations/dataset.py	Evaluation scenarios and expected behavior
evaluations/eval_all.py	Main evaluation workflow

The project tree reflects the expected layout. Verify filenames against your actual repository before executing individual modules.

🚀 Getting Started
Prerequisites

Install the following before getting started:

Python 3.12 or later
Git
uv
An OpenAI API key with access to the configured model
1. Clone the Repository
bash
git clone https://github.com/Anushbharathwaj/Agent_Eval.git
cd Agent_Eval

2. Install Python
bash
uv python install 3.12

3. Install Dependencies
bash
uv sync --locked


This installs the dependencies specified in pyproject.toml and uv.lock.

4. Configure Environment Variables

Create a .env file in the project root. If .env.example exists, use it as a template.

Add your OpenAI API key:

dotenv
OPENAI_API_KEY=your_openai_api_key_here


Replace the placeholder with your own API key.

Security: Never commit .env files, API keys, or other credentials to GitHub. Ensure .env is included in .gitignore.
5. Verify Model Configuration

Review the model settings in:

text
agent/models.py
evaluations/model.py


Confirm that the configured model identifiers are supported by your OpenAI account and installed library versions.

💬 Running the Agent

The primary implementation is located in:

text
agent/agent.py


Run the agent using the entry point provided by the module. Check agent/agent.py for the supported invocation method, since it may expose an agent object or function rather than a standalone script.

Optional Streamlit Interface

If the Streamlit interface is configured, launch it using:

bash
uv run --env-file .env --with streamlit \
  python -m streamlit run agent/streamlit_ui.py


Open the local URL printed in your terminal.

🧪 Running Evaluations

The main evaluation runner is expected at:

text
evaluations/eval_all.py


Run the complete evaluation workflow from the repository root:

bash
uv run --env-file .env python evaluations/eval_all.py


The workflow typically:

Loads the evaluation dataset.
Executes the agent against each scenario.
Captures execution traces and tool calls.
Constructs test cases using actual outputs and expected behavior.
Evaluates final answers and execution behavior.
Reports metric scores, pass rates, and explanations.
Note: This command assumes evaluations/eval_all.py exists and is configured as an executable script. Check the actual repository entry point before running it.

LLM-based evaluations make API calls and may incur costs.

Running Individual Metrics

If the corresponding scripts exist in your repository, you can run individual evaluations:

bash
uv run --env-file .env python evaluations/task_completion.py
uv run --env-file .env python evaluations/tool_correctness.py
uv run --env-file .env python evaluations/answercorrectness.py


Check the exact filenames and invocation methods in your local evaluations/ directory.

📊 Evaluation Metrics

The project evaluates agent behavior across seven dimensions.

Metric	Evaluation Objective
Task Completion	Did the agent achieve the requested outcome?
Step Efficiency	Did it avoid unnecessary or redundant actions?
Plan Quality	Was the execution plan appropriate?
Plan Adherence	Did execution follow the intended plan?
Argument Correctness	Were the tool arguments appropriate?
Tool Correctness	Were the expected tools selected?
Answer Correctness	Did the final answer reach the expected conclusion?
Why Evaluate Execution Behavior?

A response can appear correct even when the agent uses an inappropriate tool or performs unnecessary actions.

Evaluating both the final answer and execution trace helps identify failures that response-only testing can miss.

Metric thresholds, scoring rubrics, and pass criteria are defined in the evaluation scripts.

🗃️ Evaluation Dataset

The dataset is expected at:

text
evaluations/dataset.py


It contains eight refund-related scenarios.

Scenario	Expected Behavior
Eligible refund	Calculate the amount and create a simulated ticket
Expired refund window	Explain why the purchase is ineligible
Specific item refund	Refund only the requested item
Multiple-item refund	Calculate the combined refund amount
Information-only request	Answer without creating a ticket
Missing username	Request the missing information
Unknown customer	Explain that the customer could not be found
Unpurchased item	Explain that the item is absent from purchase history

These cases cover successful workflows, missing information, invalid requests, and situations where the agent should not initiate a refund.

Dataset Visualization

![Evaluation dataset JSON structure](DatasetJsonView.png)


Keep sample purchase records, refund policy, and expected answers consistent to ensure meaningful evaluation results.

🔎 Understanding Evaluation Results

Evaluation reports can provide scores, pass rates, and explanations for individual test cases.

When a test fails:

Review the input and expected behavior.
Inspect the final response.
Examine tool selection and arguments.
Review the execution trace.
Check the metric's evaluation criteria.
Improve the agent, tools, dataset, or rubric.
Rerun the evaluation.

A low score does not necessarily mean the final answer is incorrect. It may indicate unnecessary tool calls, invalid arguments, missing execution evidence, inconsistent reference answers, or an overly strict evaluation rubric.

Review average scores and individual pass rates together because an acceptable average can hide specific failures.

⚠️ Limitations
Purchase records are sample data.
Refund ticket creation is simulated.
Refund eligibility depends on the configured policy and implementation.
Eight scenarios provide limited evaluation coverage.
LLM-based evaluation results may vary between runs.
Results depend on the quality of the dataset, reference answers, and evaluation rubrics.
This project is an educational prototype, not a production refund-processing system.
🔮 Future Improvements
Expand the dataset with additional refund scenarios and edge cases.
Evaluate multi-turn conversations and follow-up questions.
Add stronger validation inside refund tools.
Test refund-window boundary conditions.
Add stricter assertions for tool selection and arguments.
Export evaluation reports and compare results across runs.
Benchmark different models and prompts using the same dataset.
Add regression tests for previously identified failures.
Introduce persistent storage, authentication, and production-grade access controls.
🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

Fork the repository.
Create a feature branch.
Implement and test your changes.
Submit a pull request describing the changes.

For bugs or feature requests, use the GitHub Issues page.

📄 License

No license information is specified here. Check the repository for an existing LICENSE file before reusing or distributing the project.

<p align="center">
<strong>Built for experimentation with AI agents, tool calling, LLM evaluation, and evaluation-driven development.</strong>
<br>
<a href="https://github.com/Anushbharathwaj/Agent_Eval">Explore Agent_Eval on GitHub</a>
</p>