from datetime import datetime
from posixpath import split
import re
from selectors import BaseSelector
from time import time
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty+=1

    percantage = float(message_certainty / float(len(recognised_words)))      

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int (percantage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    #REPONSES---------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey'], single_response=True)
    response('Time is: '+str(datetime.now().strftime("%H:%M:%S")), ['what is the', 'time'], required_words=['time'])
    response('Zobraz mozne prikazy', ['help', '-h', '--help'])
    response('My name is John', ['what\'s', 'your', 'name?', 'what is', 'tell me'], required_words=['name'])        

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

