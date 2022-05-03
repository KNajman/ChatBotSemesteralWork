from datetime import datetime
import requests


def exchange_rate(date: str, currency: str):
    """
    INPUT:
    date in format as %d.%m.%Y
    currency as string in format 'EUR', 'USD', 'GBP' etc.

    RETURN:
    exchange rate for the given currency on a specific date
    """
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;?date="
    date_format = "%d.%m.%Y"

    try:
        datetime.strptime(date, date_format)
    except ValueError:
        raise ValueError("Incorrect date format. It should be dd.mm.yyyy")

    url += date
    if len(currency) != 3:
        raise ValueError(
            "Incorrect currency format. It should be 3 letters as 'EUR', 'USD', 'GBP' etc."
        )

    response = requests.get(url)
    data = response.text
    line_split = data.split()
    for line in line_split:
        if currency in line:
            correct_line = line
    rate = correct_line.split("|")

    if rate == "":
        raise ValueError("Unknown currency.")

    return rate[-1]


def save_exchange_rate_in_file(rate: float, file_name):
    """
    saves exchange rate in file
    """
    if rate == "":
        raise ValueError("Rate was not specified.")

    with open(file_name, mode="a", encoding="utf-8") as file:
        d = datetime.now().strftime("%d.%m.%Y")
        file.write(d + " " + str(rate) + "\n")


if __name__ == "__main__":
    datum = datetime.now().strftime("%d.%m.%Y")

    rate = exchange_rate(datum, "EUR")
    print(rate)

    save_exchange_rate_in_file(rate, "exchange_rate.txt")
