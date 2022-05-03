from datetime import datetime
import re
import long_responses as long
import exchange_rate as ex


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
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


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words
        )

    # REPONSES---------------------------------------------------------------------------------------------------------
    response("Hello!", ["hello", "hi", "hey"], single_response=False)
    response("Time is: " + str(datetime.now().strftime("%H:%M:%S")),
             ["what is the", "time"], single_response=True, required_words=["time"])
    response("Commands that I can process are: help, name, time, eur, eur history", [
             "Can you help me", "I need help", "help"], required_words=["help"])
    response("My name is Bob", ["what is", "your", "name",
             "tell me"], single_response=True, required_words=["name"])
    response(ex.exchange_rate(datetime.now().strftime("%d.%m.%Y"), 'EUR') + " Kč/1EUR",
             ["exchange rate", "eur"], single_response=True, required_words=["eur"])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input: str):
    split_message = re.split(r"\s+|[,;?!.-]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response


if __name__ == "__main__":
    while True:
        print('Bot: ' + get_response(input('You: ')))