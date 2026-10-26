import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] /'agent')
)

from deepeval import evaluate
from deepeval.metrics import GEval
from deepeval.integrations.langchain import CallbackHandler
from deepeval.test_case import ToolCall, LLMTestCase, SingleTurnParams

from dataset import dataset
from agent import agent
from model import eval_model

from uuid import uuid4

for golden in dataset.goldens:
    response = agent.invoke(
        {"messages":[{"role":"user","content":golden.input}]},
        config = {"configurable":{"thread_id":str(uuid4())},
                 "callbacks":[CallbackHandler()]
                 }
    )
    
    actual_output = response["structured_response"].answer
    
    tool_call = []
    test_case = []
    
    for message in response["messages"]:
        for tool_called in getattr(message,"tool_calls",[]) or []:
            tool_call.append(
                ToolCall(name = tool_called["name"],
                         input_parameters = tool_called["args"])
            )        
        
    test_case = LLMTestCase(
        input = golden.input,
        actual_output = actual_output,
        tool_called = tool_call,
        expected_output= golden.expected_output
    )
    
    dataset.add_test_case(test_case)

metrics = [GEval(
    name = "answercorrectness",
    evaluation_params = [
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT
    ],
    evaluation_steps=["make sure that the actual output and the expected output have the same logical conclusion"],
    model = eval_model,
    threshold = 0.8,
    verbose_mode = True
    
)]

evaluate(test_cases = dataset.test_cases, metrics = metrics)