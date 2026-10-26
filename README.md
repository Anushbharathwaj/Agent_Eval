🤖 Agent_Eval

An AI Agent Evaluation System using LangChain, LangGraph, OpenAI, and DeepEval.

Build, test, and evaluate a refund support AI agent while measuring answer correctness, tool selection, argument accuracy, planning, and task completion.

!Python !LangChain !LangGraph !DeepEval !OpenAI

Repository: Anushbharathwaj/Agent_Eval

Table of Contents
Features
Technology Stack
Project Structure
Prerequisites
Installation
Configuration
Running the Agent
Running Evaluations
Evaluation Metrics
Evaluation Dataset
Understanding Results
Screenshots
Limitations
Roadmap
Contributing
License
Features
AI Agent: Build a refund support agent using LangChain.
Tool Calling: Retrieve purchases, calculate refunds, and simulate ticket creation.
Structured Responses: Use Pydantic models for agent outputs.
Conversation Memory: Maintain conversation state using LangGraph checkpointing.
Agent Evaluation: Evaluate responses and execution behavior using DeepEval.
Execution Tracing: Inspect agent actions, selected tools, and tool arguments.
Evaluation Dataset: Test eight refund-related scenarios.
Seven Evaluation Metrics: Measure task completion, efficiency, planning, tool selection, argument correctness, and answer correctness.
Interactive Interface: Optional Streamlit chat interface.
Dependency Management: Manage Python dependencies using uv.
Technology Stack
Technology	Purpose
Python 3.12+	Core programming language
LangChain	Agent creation and tool integration
LangGraph	Stateful workflows and checkpointing
OpenAI	Language model
DeepEval	LLM evaluation and execution tracing
Pydantic	Structured data validation
uv	Python environment and dependency management
python-dotenv	Environment variable configuration
Streamlit	Optional chat interface
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


The structure represents the expected repository layout. Check your local files for the exact module names before running individual scripts.

Prerequisites

Before installing the project, ensure you have:

Python 3.12 or later
Git
uv
An OpenAI API key with access to the configured model
Installation
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


This installs the dependencies defined in pyproject.toml and uv.lock.

Configuration

Create a .env file in the project root. If .env.example exists, use it as a template.

Add your OpenAI API key:

env
OPENAI_API_KEY=your_openai_api_key_here


Replace the placeholder with your actual API key.

Security: Never commit .env files or API credentials to GitHub. Ensure .env is included in .gitignore.

Model Configuration

Review the model settings in:

text
agent/models.py
evaluations/model.py


Ensure the configured model identifiers are supported by your OpenAI account and installed library versions.

Running the Agent

The primary agent implementation is located at:

text
agent/agent.py


Supporting modules include:

agent/tools.py — purchase lookup, refund calculation, and simulated ticket operations.
agent/prompts.py — system instructions and refund policy.
agent/data.py — sample customer purchase records.
agent/objects.py — Pydantic response models.
agent/models.py — language model configuration.

Run the agent using the entry point defined in agent/agent.py. Check the module for its supported invocation method.

Optional Streamlit Interface

If the Streamlit interface is configured, start it with:

bash
uv run --env-file .env --with streamlit python -m streamlit run agent/streamlit_ui.py


Open the local URL displayed in your terminal.

Running Evaluations

The main evaluation workflow is expected at:

text
evaluations/eval_all.py


Run the complete evaluation workflow:

bash
uv run --env-file .env python evaluations/eval_all.py


The workflow typically:

Loads the evaluation dataset.
Executes the agent against each test scenario.
Captures execution traces and tool calls.
Compares actual behavior with expected outcomes.
Evaluates final answers and execution behavior.
Reports metric scores, pass rates, and explanations.

Note: Verify that evaluations/eval_all.py exists and supports direct execution. LLM-based evaluations make API calls and may incur costs.

Running Individual Metrics

If the following scripts exist in your repository, you can run them individually:

bash
uv run --env-file .env python evaluations/task_completion.py
uv run --env-file .env python evaluations/tool_correctness.py
uv run --env-file .env python evaluations/answercorrectness.py


Check the actual filenames in evaluations/ before running these commands.

Evaluation Metrics

The project evaluates the agent using seven metrics.

Metric	Description
Task Completion	Determines whether the agent achieves the requested outcome.
Step Efficiency	Measures unnecessary or redundant actions.
Plan Quality	Evaluates whether the execution plan is appropriate.
Plan Adherence	Checks whether execution follows the intended plan.
Argument Correctness	Evaluates the arguments passed to tools.
Tool Correctness	Checks whether the agent selects the expected tools.
Answer Correctness	Evaluates whether the final response reaches the expected conclusion.

These metrics help identify problems that may not be visible from the final response alone, such as incorrect tool calls, unnecessary steps, and inappropriate arguments.

Evaluation Dataset

The evaluation dataset is expected at:

text
evaluations/dataset.py


It contains eight refund-related scenarios.

Scenario	Expected Behavior
Eligible refund	Calculate the refund and create a simulated ticket.
Expired refund window	Explain why the purchase is ineligible.
Specific item refund	Refund only the requested item.
Multiple-item refund	Calculate the combined refund amount.
Information-only request	Provide information without creating a ticket.
Missing username	Ask the user for the missing information.
Unknown customer	Explain that the customer could not be found.
Unpurchased item	Explain that the item is absent from purchase history.

The scenarios test successful refund requests, missing information, invalid requests, and situations where the agent should not initiate a refund.

Understanding Results

Evaluation reports can provide metric scores, pass rates, and explanations for individual test cases.

When a test fails:

Review the user request and expected behavior.
Inspect the final agent response.
Examine the selected tools and their arguments.
Review the execution trace.
Check the evaluation rubric.
Improve the agent, tools, dataset, or evaluation criteria.
Rerun the evaluation.

A low score does not always indicate an incorrect final answer. It may also reveal inefficient execution, invalid arguments, inconsistent reference answers, or missing evaluation evidence.

Screenshots

If DatasetJsonView.png exists in the repository root, display the evaluation dataset using:

!Evaluation Dataset JSON Structure

The screenshot illustrates the dataset structure used to define test inputs and expected behavior.

Limitations
Customer purchase records are sample data.
Refund ticket creation is simulated.
Eligibility decisions depend on the configured refund policy.
The evaluation dataset covers a limited number of scenarios.
LLM-based evaluation scores may vary between runs.
Evaluation quality depends on consistent reference answers and scoring criteria.
This project is an educational prototype, not a production refund-processing system.
Roadmap
Implement a refund support agent.
Integrate tool calling.
Define refund-related evaluation scenarios.
Implement seven evaluation metrics.
Capture agent execution traces.
Expand the evaluation dataset.
Add multi-turn conversation tests.
Introduce regression testing.
Compare different models and prompts.
Export evaluation reports for comparison across runs.
Contributing

Contributions, bug reports, and suggestions are welcome.

Fork the repository.
Create a feature branch:
bash
git checkout -b feature/your-feature

Implement and test your changes.
Commit your changes:
bash
git commit -m "Add your feature"

Push your branch:
bash
git push origin feature/your-feature

Open a Pull Request.
License

Check the repository for a LICENSE file before specifying the project's license. If no license exists, usage and redistribution permissions should not be assumed.

Built for learning and experimentation with AI agents, tool calling, LLM evaluation, and evaluation-driven development.

Explore Agent_Eval on GitHub