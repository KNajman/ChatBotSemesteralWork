import random
import datetime as dt
import exchange_rate as er


def help():
    long_response = (
        "Commands that I can proced are:\n" 
        + "'help'\n"
        + "'name'\n" 
        + "'time'\n" 
        + "'exchange rate eur'\n" 
        + "'history eur'\n" 
        + "'purchase recommendation eur'")
    return long_response


def unknown():
    long_response = [
        "Could you please re-phrase that? Or type 'help'",
        "I don't understand what you mean, try to type 'help'.",
        "I'm sorry, I don't understand what you mean...",
        "Sorry I don't know, try to type 'help'.",
        "Type 'help' for a list of commands.",
    ]
    return long_response[random.randrange(len(long_response))]


def past_exchange_rates(currency: str):
    time = dt.datetime.now()
    dates = er.past_5_dates(time)
    long_response = "\n"
    for d in dates:        
        long_response+=str(d + " | "+er.exchange_rate(d, currency)+"Kč/1EUR" + "\n")
    return long_response

if __name__ == "__main__":
    print(past_exchange_rates('EUR'))