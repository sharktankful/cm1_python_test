from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI(openai_api_key="GRAB API KEY",
                  model='gpt-3.5-turbo', client='my_applicaiton')

messages = [
    SystemMessage(content="Your an expert data scientist"),
    HumanMessage(content="Why is the sky blue?")
]
response = chat(messages)

print(response.content, end='\n')
