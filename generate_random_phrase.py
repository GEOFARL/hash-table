import random
import string


def generate_random_phrase(max_length):
    phrase = ""
    length = random.randint(1, max_length)
    for i in range(length):
        phrase += random.choice(string.ascii_lowercase)
    return phrase
