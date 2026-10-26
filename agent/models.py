from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()

model = init_chat_model(model = "gpt-6-luna")

"""Test the model by invoking it with a sample prompt."""

#response = model.invoke("Hello, how are you?")

#print(response.content)

