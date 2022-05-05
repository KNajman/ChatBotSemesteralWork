from datetime import datetime
from exchange_rate import exchange_rate
from long_responses import unknown, help, past_exchange_rates
import re

def message_probability(user_message: list, recognised_words: list, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percantage = float(message_certainty / float(len(recognised_words)))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percantage * 100)
    else:
        return 0


def check_all_messages(message: list):
    highest_prob_list = {}

    def response(bot_response: str, list_of_words: list, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words)

    # REPONSES---------------------------------------------------------------------------------------------------------
    response("Hello!", ["hello", "hi", "hey"], single_response=True)
    response("Time is: " + str(datetime.now().strftime("%H:%M:%S")),
             ["what is the", "time"], required_words=["time"])
    response(help(), ["Can you help me", "I need help",
             "help", "what can you do", "h"], single_response=True)
    response("My name is Bob", ["what is", "your",
             "name", "tell me"], required_words=["name"])
    response(exchange_rate(datetime.now().strftime("%d.%m.%Y"), "EUR") +"Kč/1EUR", ["exchange rate eur", "eur", "eur rate"])
    response(past_exchange_rates("EUR"), ["history","exchange rate eur history", "history eur"])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input: str):
    split_message = re.split(r"\s+|[,;?!.-]\s*", str(user_input).lower())
    response = check_all_messages(split_message)
    return response


if __name__ == "__main__":
    while True:
        print("Bot: " + get_response(input("You: ")))