import random


def get_random_letter():
    """Get a random letter from the alphabet"""
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    random_index = random.randint(0, len(letters)-1)
    return letters[random_index]


def get_random_symbol():
    """Get a random symbol from this list[@, $, #, *, -]"""
    symbols = ["@", "$", "#", "*", "-"]


def generate_password():
    """Generate a random password for the user"""
    pass