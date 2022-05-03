import random
from urllib import response


def unknown():
    response['Could you please re-phrase that?',
             'What does than mean?',
             'Sorry I don\'t know.'][random.randrange(3)]
    return response
