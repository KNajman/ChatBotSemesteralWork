import pytest
import exchange_rate as er
"""
#TEST
print(exchange_rate("25.02.2022", 'EUR'))
"""

er.exchange_rate("25.02.2022", "EUR")

er.exchange_rate("", "EUR")

er.exchange_rate("25.02.2022", "")

er.exchange_rate("EUR", "USD")

er.exchange_rate("EUR", "25.02.2022")