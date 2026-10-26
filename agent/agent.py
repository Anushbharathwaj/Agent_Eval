from models import model
from tools import get_user_purchase_history, calculate_right_refund, issue_refund_ticket, get_today_date
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from uuid import uuid4
from objects import Answer 
from prompts import agent_system_prompt
from dotenv import load_dotenv
load_dotenv()

agent = create_agent(
    model = model,
    tools = [get_user_purchase_history, calculate_right_refund, issue_refund_ticket, get_today_date],
    system_prompt = agent_system_prompt,
    response_format = Answer,
    checkpointer = InMemorySaver()
)

def run_conversation():
    config = {"configurable":{"thread_id": str(uuid4())}}
    
    text = "I would like to request a refund"
    print(text)
    
    question = HumanMessage(content = text)
    
    conversation = True
    
    while conversation:
        response = agent.invoke({"messages":question}, config = config)
        structured_response = response["structured_response"]
        print(structured_response.answer)
        conversation = structured_response.conversation
        if conversation:
            userquery = input("Reply: \n")
            question = HumanMessage(content = userquery)

    print("the job is done!")

#run_conversation()
 