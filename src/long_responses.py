import random


def help():
    response = (
        "Commands that I can process are: "
        + "\n"
        + "name"
        + "\n"
        + "time"
        + "\n"
        + "eur"
        + "\n"
        + "eur history"
    )
    return response


def unknown():
    response = [
        "Could you please re-phrase that? Or type 'help'",
        "I don't understand what you mean, try to type 'help'.",
        "I'm sorry, I don't understand what you mean...",
        "Sorry I don't know, try to type 'help'.",
        "Type 'help' for a list of commands.",
    ]
    return response[random.randrange(len(response))]
