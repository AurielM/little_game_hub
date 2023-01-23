from random import randint

from gamebase import GameBase

class RandomNumberG(GameBase):
    """
    In this game you need to guess the number chosen by the computer between 1 and 100
    Depending on the level of difficulty chosen you'll get 5, 10 or 15 guesses
    Guess the number before your chances run out and you win the round!

    You'll have the option of returning back to the main menu after each run
    """



    def __init__(self):
        super().__init__()
        self.location = 'The Number Guessing Game'
        self.new_player = False
        

    def game_simulation(self):
        self.player_score += 3
        print('game_simulation: Player score: ', self.player_score)


    def run_game(self):
        self.introduce_location()
        
        print('Game body here... \n\n{self.location} \n\n...is the game.')
        
        print('Round over!\n')
        super().run_game()


class ExampleGame2():

    def __init__(self):
        self.location = 'The Example game 2'

    def commence_game(self):
        print('game commencing' + self.location)
        pass

    