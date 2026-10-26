import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / 'agent')
)

from agent import agent
from model import eval_model
from dataset import dataset

from uuid import uuid4

from deepeval.metrics import PlanAdherenceMetric
from deepeval.integrations.langchain import CallbackHandler

#1 Define Metrics

metrics = [PlanAdherenceMetric(threshold = 0.8, model = eval_model, include_reason = True)]

#2 Load Metrics

for golden in dataset.evals_iterator(metrics = metrics):
    response = agent.invoke(
        {"messages":[{"role":"user","content":golden.input}]},
        config = {"configurable": {"thread_id": str(uuid4())},
                  "callbacks": [CallbackHandler()]
                  }
    )