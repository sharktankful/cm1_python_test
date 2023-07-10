from langchain.chat_models import ChatOpenAI
# TEMP
from langchain.memory import ChatMessageHistory
from langchain.schema import HumanMessage, SystemMessage

history = ChatMessageHistory()

# Function to send message and get a response from chatbot
def send_message(message):
    chat = ChatOpenAI(openai_api_key="",
                    model='gpt-3.5-turbo', client='my_applicaiton')

    messages = [
        SystemMessage(content="Your a helpful AI Assistant"),
        HumanMessage(content=message)
    ]
    response = chat(messages)

    # TEMP
    history.add_user_message(message)

    return response.content


# User-Message Variables
user_message = ""

# Chatbot will stay activated until user enters 'quit' into the terminal/command-prompt
while user_message.lower() != "quit":

    # Sends message to ChatBot
    response = send_message(user_message)

    # Extract the bot's reply from the response variable and prints it
    bot_reply = response 
    print("ChatBot:", bot_reply, end='\n')

    # User message to send to ChatBot
    user_message = input("You: ")

# TEMP
print(history.messages)

print("ChatBot Turned Off.")
