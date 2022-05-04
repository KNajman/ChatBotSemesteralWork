from datetime import datetime
import os
from exchange_rate import *
import pytest

def test_exchange_rate_with_02_05_2022_rate_EUR():
    """
    test exchange rate
    """
    assert exchange_rate("02.05.2022", 'EUR') == '24,670'


def test_exchange_rate_with_no_date():
    with pytest.raises(ValueError):
        exchange_rate("", "EUR")


def test_exchange_rate_with_no_currency():
    with pytest.raises(ValueError):
        exchange_rate("25.02.2022", "")


def test_exchange_rate_with_uncorrect_date():
    with pytest.raises(ValueError):
        exchange_rate("EUR", "USD")


def test_exchange_rate_with_uncorrect_currency():
    with pytest.raises(ValueError):
        exchange_rate("25.02.2022", "RRRR")


def test_exchange_rate_with_switcher_values():
    with pytest.raises(ValueError):
        exchange_rate("EUR", "25.02.2022")


def test_exchange_rate_with_wront_date_type():
    with pytest.raises(TypeError):
        exchange_rate(2022, "EUR")


def test_exchange_rate_with_wront_date_format():
    with pytest.raises(ValueError):
        exchange_rate("02.31.2022", "EUR")


def test_exchange_rate_with_wront_currency_type():
    with pytest.raises(TypeError):
        exchange_rate("02.05.2022", 1234)


def test_save_exchange_rate_in_file():
    if os.path.exists("test_file.txt"):
        os.remove("test_file.txt")

    save_exchange_rate_in_file("24,670", "test_file.txt")
    d = datetime.now().strftime("%d.%m.%Y")
    with open("test_file.txt", "r") as file:
        assert file.read() == d + " 24,670\n"


def test_save_exchange_rate_in_file_2():
    if os.path.exists("test_file.txt"):
        os.remove("test_file.txt")

    save_exchange_rate_in_file(24.670, "test_file.txt")
    d = datetime.now().strftime("%d.%m.%Y")
    with open("test_file.txt", "r") as file:
        assert file.read() == d + " " + str(24.670) + "\n"


def test_save_exchange_rate_in_file_3():
    if os.path.exists("test_file.txt"):
        os.remove("test_file.txt")

    save_exchange_rate_in_file("24.670", "test_file.txt")
    d = datetime.now().strftime("%d.%m.%Y")
    with open("test_file.txt", "r") as file:
        assert file.read() == d + " 24.670\n"


def test_save_exchange_rate_in_file_no_rate():
    with pytest.raises(ValueError):
        save_exchange_rate_in_file("", "test_file.txt")


def test_save_exchange_rate_in_file_no_file():
    with pytest.raises(FileNotFoundError):
        save_exchange_rate_in_file("24.670", "")

    if os.path.exists("test_file.txt"):
        os.remove("test_file.txt")
