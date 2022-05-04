import pylint
import chatbot

def test_chatbot_response():
    chatbot.get_response("Hello!")
    chatbot.get_response("What is the time?")
    chatbot.get_response("Can you help me?")
    chatbot.get_response("What is your name?")
    chatbot.get_response("What is the exchange rate for eur today?")