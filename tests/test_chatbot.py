from datetime import datetime
import pytest
from src.chatbot import *
from src.exchange_rate import exchange_rate


def test_chatbot_response_greeting():
    assert get_response("Hello!") == "Hello!"


def test_chatbot_response_name():
    assert get_response("What is your name?") == "My name is Bob"


def test_chatbot_response_eur():
    assert get_response("What is the exchange rate for eur today?") == str(
        exchange_rate(datetime.now().strftime("%d.%m.%Y"), "eur"))+" Kč/1EUR"


def test_chatbot_response_wrong_input():
    assert get_response("cd /src") != ""


def test_chatbot_response_wrong_input_2():
    assert get_response("Non-sence") != ""


def test_chatbot_response_wrong_input_3():
    assert get_response(42) != ""


def test_chatbot_response_empty_input():
    assert get_response("") != ""


def test_chatbot_response_no_input():
    with pytest.raises(TypeError):
        get_response() != ""


# tests for message_probability

def test_message_probability():
    assert message_probability(
        "Hello!", ["hello", "hi", "hey"], single_response=True) == 0


def test_message_probability_2():
    assert message_probability("hello", ["hello", "hi", "hey"]) == 0


def test_message_probability_no_inputs():
    with pytest.raises(TypeError):
        message_probability()


def test_message_probability_only_wrong_inputs():
    with pytest.raises(TypeError):
        message_probability(0, 0, 0, 0)


def test_message_probability_only_wrong_inputs_2():
    with pytest.raises(TypeError):
        message_probability([''], 0, True, [''])

def test_message_probability_only_wrong_inputs_3():
    assert message_probability(['gsgs'], ['a'], "blbost", ['']) == 0

def test_message_probability_only_wrong_inputs_4():
    with pytest.raises(TypeError):
        message_probability([''], ['a'], False, 0)

def test_message_probability_zero_div_error():
    with pytest.raises(ZeroDivisionError):
        message_probability(['Okurka'], [], True, ['jahoda'])


def test_message_probability_zero_div_error_2():
    with pytest.raises(ZeroDivisionError):
        message_probability(['Okurka'], [], False, ['jahoda'])


def test_message_probability_zero_0_percent():
    assert message_probability([], ['Okurka'], True, ['Okurka']) == 0


def test_message_probability_zero_0_percent_2():
    assert message_probability([], ['Okurka'], False, ['Okurka']) == 0


def test_message_probability_zero_100_percent():
    assert message_probability(['Okurka'], ['Okurka'], True, ['Okurka']) == 100


def test_message_probability_zero_100_percent_2():
    assert message_probability(['Okurka'], ['Okurka'], True, ['Okurka']) == 100
       
        
# tests for check_all_messages


def test_check_all_messages():
    assert check_all_messages(["hello", "hi", "hey"]) == "Hello!"


def test_check_all_messages_non_sence():
    assert check_all_messages("non-sence") != ""


def test_check_all_messages_no_input():
    with pytest.raises(TypeError):
        check_all_messages()


def test_check_all_messages_empty_list():
    assert check_all_messages([]) != ""


def test_check_all_messages_wrong_input():
    with pytest.raises(TypeError):
        check_all_messages(123)
