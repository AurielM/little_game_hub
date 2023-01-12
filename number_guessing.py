from random import randint
from main import Hub

class RandomNumberG(Hub):
    """
    In this game you need to guess the number chosen by the computer between 1 and 100
    Depending on the level of difficulty chosen you'll get 5, 10 or 15 guesses
    Guess the number before your chances run out and you win the round!

    You'll have the option of returning back to the main menu after each run
    """

    def __init__(self, player):
        pass