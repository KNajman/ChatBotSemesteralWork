import pytest
from long_responses import *


def test_long_responses_help():
    assert help() != ""


def test_long_responses_help_parametr():
    with pytest.raises(TypeError):
        help(0)


def test_long_responses_unknown():
    assert unknown() != ""


def test_long_responses_unknown_parametr():
    with pytest.raises(TypeError):
        unknown(0)


def test_past_exchange_rates():
    assert past_exchange_rates('EUR') != ""


def test_past_exchange_rates_uncorrect_data():
    with pytest.raises(TypeError):
        past_exchange_rates(0)

def test_past_exchange_rates_no_data():
    with pytest.raises(TypeError):
        past_exchange_rates()