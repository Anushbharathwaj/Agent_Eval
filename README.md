Agent_Eval — LangChain AI Agent Evaluation System

Build, test, and evaluate a refund support AI agent using Python, LangChain, OpenAI, and DeepEval.

This project demonstrates how to build a tool-using AI agent and systematically evaluate both its final answers and its execution behavior. It includes a refund support agent, sample customer purchase data, an evaluation dataset, and seven evaluation metrics.

The goal is to go beyond checking whether an AI agent produces a correct answer. We also evaluate whether it selects the right tools, passes the correct arguments, follows an appropriate plan, and completes the user's task efficiently.

Dataset 
![alt text](DatasetJsonView.png)

Table of Contents
Project Overview
Features
Technology Stack
Project Structure
Prerequisites
Installation and Setup
Environment Configuration
Running the Agent
Running Evaluations
Evaluation Metrics
Evaluation Dataset
Understanding Evaluation Results
How the Agent Works
Limitations
Future Improvements
Project Overview

The project implements a customer support agent that handles refund-related requests.

The agent can:

Retrieve customer purchase history.
Check purchase dates and refund eligibility according to its instructions.
Calculate refund amounts for requested items.
Generate simulated refund ticket confirmations.
Return structured responses using Pydantic.
Maintain conversation state using LangChain memory and checkpointing.

The evaluation workflow uses DeepEval to measure the quality of the agent's responses and its tool-using behavior.

The project also contains smaller examples in understanding_metrics/ to help explain individual evaluation metrics independently of the complete refund workflow.

Features
AI Agent Development: Build a tool-using refund support agent with LangChain.
Tool Calling: Retrieve purchase history, obtain the current date, calculate refunds, and simulate ticket creation.
Structured Responses: Use Pydantic models to represent agent responses.
Conversation Memory: Maintain conversation state using a LangGraph checkpointer.
Evaluation Dataset: Test the agent with eight refund-related scenarios.
Seven Evaluation Metrics: Assess task completion, efficiency, planning, tool usage, arguments, and answer correctness.
Execution Tracing: Capture agent execution traces through DeepEval's LangChain integration.
Evaluation Reports: Inspect scores, pass rates, and explanations to identify areas for improvement.
Reproducible Dependencies: Use uv and uv.lock to manage project dependencies.
Technology Stack
Technology	Purpose
Python 3.12+	Primary programming language
uv	Python environment and dependency management
LangChain	Agent creation and tool integration
LangGraph	Conversation state and checkpointing
OpenAI	Language model for the agent and evaluation
DeepEval	LLM evaluation and execution tracing
Pydantic	Structured response schemas
python-dotenv	Environment variable management
Streamlit	Optional interactive chat interface
Project Structure
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
├── evaluations/
│   ├── dataset.py
│   ├── evaluate_all.py
│   ├── model.py
│   ├── task_completion.py
│   ├── step_efficiency.py
│   ├── plan_quality.py
│   ├── plan_adherence.py
│   ├── argument_correctness.py
│   ├── tool_correctness.py
│   └── answer_correctness.py
├── understanding_metrics/
├── src/
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md


The exact files may vary depending on the scripts present in your local repository. The main evaluation entry point is evaluations/evaluate_all.py.

Prerequisites

Before starting, ensure you have:

macOS, Linux, or another supported development environment.
Python 3.12 or later.
uv installed.
An OpenAI API key with access to a compatible model.
Git installed if you want to clone or contribute to the repository.
Installation and Setup
1. Install uv on macOS

Install uv using the official installer:

bash
curl -LsSf https://astral.sh/uv/install.sh | sh


Check the installation:

bash
uv --version


If your terminal cannot find uv, reopen the terminal or follow the PATH instructions printed by the installer.

2. Navigate to the project

If you already have the project locally, open its folder in Visual Studio and use the integrated terminal.

Alternatively, clone the repository:

bash
git clone https://github.com/Anushbharathwaj/Agent_Eval.git
cd Agent_Eval

3. Install Python 3.12
bash
uv python install 3.12

4. Install project dependencies

If pyproject.toml and uv.lock are already present, run:

bash
uv sync --locked


This installs the dependencies specified by the existing project configuration and lockfile.

If you are initializing a completely new project rather than setting up this repository, you can create a package and environment with:

bash
uv init --package --python 3.12
uv venv .venv --python 3.12


Then add the required dependencies as appropriate for that new project:

bash
uv add "deepeval[inspect]>=4.2.8"
uv add "langchain>=1.4.4"
uv add "langchain-openai>=1.7.0"
uv add "portalocker>=4.4.0"


For the existing repository, prefer uv sync --locked instead of reinitializing the project.

5. Activate the virtual environment

On macOS or Linux:

bash
source .venv/bin/activate


To run commands without manually activating the environment, you can use uv run.

Environment Configuration

Create a .env file in the project root, or copy .env.example if it is provided.

Add your OpenAI API key:

dotenv
OPENAI_API_KEY=your_openai_api_key_here


Replace the placeholder with your actual key.

Security: Never commit your real .env file, API keys, access tokens, or other credentials to GitHub. The .gitignore file should exclude .env and .venv/.

Model Configuration

Check the model settings in:

agent/models.py
evaluations/model.py

Ensure the configured model identifiers are supported by your OpenAI account and by the libraries used in the project. Update them if necessary.

Running the Agent

The main agent implementation is located in:

text
agent/agent.py


Its supporting modules include:

agent/tools.py — tools used by the agent.
agent/prompts.py — system instructions and refund policy.
agent/data.py — sample customer purchase records.
agent/objects.py — Pydantic response models.
agent/models.py — model configuration.

The agent uses tools to gather purchase information, calculate refund amounts, and generate simulated ticket confirmations.

Optional Streamlit Interface

If agent/streamlit_ui.py is configured for Streamlit, you can run the interface with:

bash
uv run --env-file .env --with streamlit python -m streamlit run agent/streamlit_ui.py


Follow the local URL printed in the terminal to open the application.

The interface and evaluation runner may use different tool configurations, so consult the relevant source files when comparing their behavior.

Running Evaluations

The primary evaluation entry point is:

text
evaluations/evaluate_all.py


Run the complete evaluation workflow from the project root:

bash
uv run --env-file .env python evaluations/evaluate_all.py


The workflow runs the agent against the evaluation scenarios and measures its behavior using seven metrics.

The process typically involves:

Loading the evaluation dataset.
Executing the refund agent for each scenario.
Capturing execution traces and tool calls.
Constructing test cases with actual outputs and expected behavior.
Evaluating the traces and responses.
Displaying metric scores, pass rates, and explanations.

LLM-based evaluation uses API calls and may incur usage costs.

Running Individual Metrics

The evaluations/ directory also contains scripts for individual metrics. For example:

bash
uv run --env-file .env python evaluations/task_completion.py
uv run --env-file .env python evaluations/tool_correctness.py
uv run --env-file .env python evaluations/answer_correctness.py


Check the filenames in your local repository before running individual scripts.

The understanding_metrics/ directory contains smaller examples intended to demonstrate individual metrics with simpler agent tasks.

Evaluation Metrics

The project evaluates the agent using seven metrics.

Metric	What it evaluates
Task Completion	Whether the agent successfully completes the user's