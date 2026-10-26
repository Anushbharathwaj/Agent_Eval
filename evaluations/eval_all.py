import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] /'agent')
)

from deepeval import evaluate
from deepeval.metrics import( ToolCorrectnessMetric,
                              TaskCompletionMetric,
                              PlanAdherenceMetric,
                              PlanQualityMetric,
                              StepEfficiencyMetric,
                              ArgumentCorrectnessMetric,
                              GEval
                            )
from deepeval.integrations.langchain import CallbackHandler
from deepeval.test_case import LLMTestCase, ToolCall, SingleTurnParams
from deepeval.evaluate import CacheConfig, DisplayConfig

from uuid import uuid4

from agent import agent

if __package__:
    from .model import eval_model
    from .dataset import dataset
else:
    from model import eval_model
    from dataset import dataset


SUCCESSFUL_TASK_DESCRIPTION = """
If the username is missing, ask the user to provide it.
For a refund request, identify the customer and the requested purchases, and
check that each purchase is no more than 30 days old and is not in the future.
Refund only the items requested by the user. If the customer or requested item
cannot be found, do not issue a refund ticket and explain why.
Once the necessary information is available, tell the user whether a refund
ticket was issued and its amount, or explain why no refund was issued.
For an information-only request, answer the question without issuing a ticket.
"""

def build_metrics():
    """Keep the thresholds and evaluator model used by the individual scripts."""
    trace_metrics = [
        TaskCompletionMetric(threshold = 0.8, model =eval_model, include_reason= True, task = SUCCESSFUL_TASK_DESCRIPTION),
        StepEfficiencyMetric(threshold = 0.8,model = eval_model, include_reason =True),
        PlanQualityMetric(threshold = 0.8, model = eval_model, include_reason = True),
        PlanAdherenceMetric(threshold = 0.8, model =eval_model,include_reason =True)
    ]
    
    single_turn_metrics =[
        ArgumentCorrectnessMetric(threshold = 0.5, model = eval_model, include_reason =True),
        ToolCorrectnessMetric(threshold= 0.8, model =eval_model, include_reason =True),
        GEval(name = "Answer Correctness",
              evaluation_params = [
                  SingleTurnParams.INPUT,
                  SingleTurnParams.ACTUAL_OUTPUT,
                  SingleTurnParams.EXPECTED_OUTPUT
                ],
              evaluation_steps = [
                  "Check that the actual output and expected output have the same "
                  "logical conclusion about the user's request.",
              ],
              model =eval_model,
              verbose_mode = True,
              threshold = 0.8
              )
    ]
    
    return trace_metrics, single_turn_metrics


def main():
    trace_metrics, single_turn_metrics = build_metrics()
    cache_config = CacheConfig(write_cache = False, use_cache = False)
    display_config = DisplayConfig(inspect_after_run =False)
    test_case = []
    
    for golden in dataset.evals_iterator(
        metrics = trace_metrics,
        cache_config=cache_config,
        display_config=display_config
    ):
        response = agent.invoke(
            {"messages":[{'role':'user','content':golden.input}]},
            config = {'configurable':{'thread_id': str(uuid4())},
                      'callbacks': [CallbackHandler()]
                     }
        )
        
        tool_call = []
    
        
        for message in response['messages']:
            for tool_called in getattr(message,'tool_calls',[]) or []:
                tool_call.append(
                    ToolCall(name = tool_called['name'],
                             input_parameters = tool_called['args'])
                )
        test_case.append(
            LLMTestCase(input = golden.input,
                    actual_output = response['structured_response'].answer,
                    expected_output = golden.expected_output,
                    tools_called= tool_call,
                    expected_tools= golden.expected_tools
                    )
        )
        
    evaluate(test_cases=test_case, metrics= single_turn_metrics, cache_config=cache_config,display_config=display_config)
    print(f"All Testcases completed : {len(test_case)}")
if __name__ == "__main__":
    main()