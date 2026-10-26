import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] /'agent')
)

from deepeval import evaluate
from deepeval.metrics import ArgumentCorrectnessMetric
from deepeval.integrations.langchain import CallbackHandler
from deepeval.test_case import LLMTestCase, ToolCall

from uuid import uuid4

from agent import agent
from model import eval_model
from dataset import dataset

for golden in dataset.goldens:
    response = agent.invoke(
        {"messages":[{"role":"user","content":golden.input}]},
        config = {"configurable":{"thread_id":str(uuid4())},
                 "callbacks":[CallbackHandler()] 
                }
    )

    tool_caller = []
    test_cases = []
    
    actual_output = response["structured_response"].answer
    for message in response["messages"]:
        for tool_called in getattr(message,"tool_calls",[]) or []:
            tool_caller.append(
                ToolCall(name = tool_called["name"],
                         input_parameters = tool_called["args"])
            )
    test_cases = LLMTestCase(
        input = golden.input,
        actual_output = actual_output,
        tools_called=tool_caller
    )
    dataset.add_test_case(test_cases)
    
metrics = [ArgumentCorrectnessMetric(threshold= 0.8, model = eval_model, include_reason = True)]
    
evaluate(test_cases=dataset.test_cases,metrics=metrics)