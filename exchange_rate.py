from datetime import datetime, date
from urllib import response
import requests
import re


def lines_that_contain(string, fp):
    return [line for line in fp if string in line]

def exchange_rate(d, currency:str):
    url="https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=7F4C32D076912ACA29A0C575F86392AB?date="
    full_url = url+str(d)

    response=requests.get(full_url)
    data = response.text
    line_split=data.split()
    for line in line_split:
        if currency in line:
            correct_line=line
    rate=correct_line.split('|')
    return rate[-1]

datum = datetime.now().strftime("%d.%m.%Y")


"""
#TEST
print(exchange_rate("25.02.2022", 'EUR'))
"""