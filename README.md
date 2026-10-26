Agent_Eval — LangChain AI Agent Evaluation System

Build, test, and evaluate a refund support AI agent using Python, LangChain, OpenAI, and DeepEval.

This project demonstrates how to build a tool-using AI agent and evaluate both its final answers and its execution behavior. It includes a refund support agent, sample customer purchase data, an evaluation dataset, and seven evaluation metrics.

The objective is to go beyond checking whether an AI agent produces a correct answer. We also evaluate whether it selects the right tools, passes the correct arguments, follows an appropriate plan, and completes tasks efficiently.

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
Maintain conversation state using LangGraph checkpointing.

The evaluation workflow uses DeepEval to measure response quality, tool selection, tool arguments, planning, and task completion.

The repository also contains smaller examples in understanding_metrics/ to demonstrate individual evaluation metrics independently of the complete refund workflow.

Features
AI Agent Development: Build a tool-using refund support agent with LangChain.
Tool Calling: Retrieve purchase history, obtain the current date, calculate refunds, and simulate ticket creation.
Structured Responses: Use Pydantic models to represent agent responses.
Conversation Memory: Maintain conversation state using a LangGraph checkpointer.
Evaluation Dataset: Test the agent with eight refund-related scenarios.
Seven Evaluation Metrics: Measure task completion, efficiency, planning, tool usage, argument correctness, and answer correctness.
Execution Tracing: Capture agent execution traces using DeepEval's LangChain integration.
Evaluation Reports: Inspect scores, pass rates, and explanations to identify areas for improvement.
Dependency Management: Use uv and uv.lock to manage Python dependencies.
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
│   ├── eval_all.py
│   ├── model.py
│   ├── task_completion.py
│   ├── step_efficiency.py
│   ├── plan_quality.py
│   ├── plan_adherence.py
│   ├── argumentcorrectness.py
│   ├── answercorrectness.py
│   └── tool_correctness.py
├── understanding_metrics/
├── src/
├── DatasetJsonView.png
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md


The structure above illustrates the main components. Your actual repository may contain additional files or use slightly different filenames. Check the files in evaluations/ before running individual scripts.

Prerequisites

Before getting started, ensure you have:

Python 3.12 or later.
uv installed.
An OpenAI API key with access to a compatible model.
Git installed.
Visual Studio Code or another code editor.
Installation and Setup
1. Install uv

On macOS, run:

bash
curl -LsSf https://astral.sh/uv/install.sh | sh


Verify the installation:

bash
uv --version


If the terminal cannot find uv, reopen the terminal or follow the PATH instructions displayed by the installer.

2. Clone the repository
bash
git clone https://github.com/Anushbharathwaj/Agent_Eval.git
cd Agent_Eval


If you already have the project locally, open that folder in your editor instead.

3. Install Python 3.12
bash
uv python install 3.12

4. Install dependencies

From the project root, run:

bash
uv sync --locked


This installs the dependencies specified by pyproject.toml and uv.lock.

If you are creating a completely new project rather than setting up this repository, you can initialize it separately:

bash
uv init --package --python 3.12
uv venv .venv --python 3.12


Add any required dependencies that are not already declared in the project configuration.

5. Activate the virtual environment

On macOS or Linux:

bash
source .venv/bin/activate


Alternatively, use uv run to execute commands inside the project's environment without manually activating it.

Environment Configuration

Create a .env file in the project root. If .env.example exists, use it as a template.

Add your API key:

dotenv
OPENAI_API_KEY=your_openai_api_key_here


Replace the placeholder with your own key.

Security: Never commit .env, API keys, or other credentials to GitHub. Ensure that .env is excluded by .gitignore. Commit .env.example only with placeholder values.

Model Configuration

Check the model settings in:

agent/models.py
evaluations/model.py

Ensure the configured model identifiers are supported by your OpenAI account and the libraries used in this project.

Running the Agent

The primary agent implementation is:

text
agent/agent.py


Supporting modules include:

File	Responsibility
agent/tools.py	Tools for purchase lookup, date lookup, refund calculation, and simulated tickets
agent/prompts.py	System instructions and refund policy
agent/data.py	Sample customer purchase records
agent/objects.py	Pydantic response models
agent/models.py	Language model configuration

The agent uses these tools to gather purchase information, calculate refund amounts, and generate simulated ticket confirmations.

Optional Streamlit Interface

If agent/streamlit_ui.py is configured for Streamlit, launch it with:

bash
uv run --env-file .env --with streamlit python -m streamlit run agent/streamlit_ui.py


Open the local URL displayed in your terminal.

The Streamlit interface may use a different tool configuration from the evaluation runner. Refer to the relevant source files when comparing their behavior.

Running Evaluations

The main evaluation workflow is implemented in the evaluation runner, which may be named evaluations/eval_all.py in your current repository.

Run the command that matches your actual filename:

bash
uv run --env-file .env python evaluations/eval_all.py


The workflow runs the agent against the evaluation scenarios and measures its behavior using seven metrics.

The process typically involves:

Loading the evaluation dataset.
Executing the agent for each scenario.
Capturing execution traces and tool calls.
Constructing test cases containing actual outputs and expected behavior.
Evaluating execution traces and final responses.
Displaying metric scores, pass rates, and explanations.

LLM-based evaluations make API calls and may incur usage costs.

Running Individual Metrics

The evaluations/ directory contains scripts for evaluating individual metrics. For example, if the corresponding files exist:

bash
uv run --env-file .env python evaluations/task_completion.py
uv run --env-file .env python evaluations/tool_correctness.py
uv run --env-file .env python evaluations/answercorrectness.py


Use the exact filenames present in your local repository. The understanding_metrics/ directory contains smaller examples designed to explain individual evaluation concepts.

Evaluation Metrics

The project evaluates the agent using seven metrics.

Metric	What it measures
Task Completion	Whether the agent achieves the intended task
Step Efficiency	Whether the agent avoids unnecessary or redundant actions
Plan Quality	Whether the agent develops an appropriate plan
Plan Adherence	Whether execution follows the intended plan
Argument Correctness	Whether tool arguments are appropriate for the user's request
Tool Correctness	Whether the expected tools are selected
Answer Correctness	Whether the final answer reaches the expected conclusion
Understanding the Metrics

1. Task Completion

Measures whether the agent successfully achieves the requested outcome.

2. Step Efficiency

Evaluates whether the agent completes the task without unnecessary actions or redundant tool calls.

3. Plan Quality

Assesses whether the agent's plan is suitable for the user's request.

4. Plan Adherence

Measures whether the agent follows its plan during execution.

5. Argument Correctness

Checks whether the agent passes appropriate arguments to its tools.

6. Tool Correctness

Checks whether the agent selects the expected tools for each scenario.

7. Answer Correctness

Uses an LLM-based evaluation rubric to compare the agent's answer against the expected conclusion.

Metric thresholds and scoring configurations are defined in the evaluation scripts. Completing an evaluation does not necessarily mean that every metric passes.

Evaluation Dataset

The dataset is defined in the evaluation dataset module, typically:

text
evaluations/dataset.py


It contains eight refund-related scenarios designed to test different agent behaviors.

Scenario	Expected behavior
Eligible refund	Calculate the amount and issue a simulated refund ticket
Purchase outside the refund window	Explain why the purchase is ineligible
Specific item refund	Refund only the requested item
Multiple-item refund	Calculate the combined amount for requested items
Information-only question	Provide information without issuing a ticket
Missing username	Ask the user to provide the missing information
Unknown customer	Explain that the customer could not be found
Unpurchased item	Explain that the requested item is absent from the purchase history

These scenarios help identify problems that a successful demonstration might miss. An agent may generate a convincing response while selecting an incorrect tool, passing invalid arguments, calculating the wrong amount, or issuing a ticket when the user only requested information.

Dataset Screenshot

The screenshot below illustrates the evaluation dataset structure.

!Evaluation dataset JSON structure

The dataset defines the inputs and expected behavior used to assess the agent. Keep the sample data, refund policy, and expected answers consistent, especially when evaluating purchase dates and refund eligibility.

Understanding Evaluation Results

Evaluation reports provide scores, pass rates, and explanations for each metric.

When investigating a failed test:

Inspect the user's request and expected behavior.
Review the agent's final response.
Examine the selected tools and their arguments.
Inspect the execution trace and evaluation explanation.
Determine whether the problem lies in the agent, the dataset, the tools, or the evaluation rubric.
Make a targeted improvement and rerun the evaluation.

A low score does not always indicate an incorrect agent response. It may also reveal inconsistent reference answers, missing evaluation evidence, or an overly strict scoring rubric.

Average scores and pass rates measure different aspects of performance. An acceptable average score can coexist with many individual cases failing their thresholds.

Limitations
The purchase records are sample data.
Refund ticket creation is simulated.
Eligibility decisions depend on the configured instructions and tool workflow.
The evaluation dataset covers a limited number of scenarios.
LLM-based evaluation scores may vary between runs.
Evaluation quality depends on consistent expected answers, model settings, and scoring rubrics.
This project is an educational prototype, not a production refund-processing system.
Future Improvements

Potential improvements include:

Expand the dataset with additional refund scenarios and edge cases.
Test multi-turn conversations and follow-up questions.
Add stronger validation inside refund tools.
Test purchases at the refund-window boundary.
Add expected tool arguments and stricter tool-call checks.
Export evaluation reports for comparison across runs.
Compare different models and prompts using the same dataset.
Add regression tests to prevent previously fixed failures from returning.
Introduce persistent storage and production-grade access controls.
Repository

GitHub: https://github.com/Anushbharathwaj/Agent_Eval

This project is intended for learning and experimentation with AI agents, tool calling, LLM evaluation, and evaluation-driven development.