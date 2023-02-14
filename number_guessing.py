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
        self.player_chances = { 'Easy': 20, 
                                'Normal': 10, 
                                'Hard': 5
                                }
        self.game_rules = """ Rules:
        - A random number will be chosen between 1 and 100
        - The objective is to guess the number before you're out of guesses.
        - You will be given hints on whether your guess is too high/too low per guess.
        - You have have a limited number of guesses before it's game over!
        """
        self.guess_count = int
        self.round_ongoing = True
        self.hints = ['Too low!\n','Too high!\n', 'You win!\n']


    def run_game(self):
        super().run_game()
        self.guess_count = self.player_chances[self.difficulty_level_chosen]
        self.introduce_difficulty_level_chosen = f'Number of guesses: {self.guess_count}'
        print(self.introduce_difficulty_level_chosen)
        print(self.game_rules)
        self.number_generated = randint(1, 100)
        while self.round_ongoing:
            self.players_guess = input('Player\'s guess: ')
            print(self.number_comparison(self.players_guess))
            self.guess_count -= 1
            if self.guess_count > 0:
                print(f'{self.guess_count} chances to guess the correct number')
            else:
                self.round_ongoing = False
                

        

        print('Round over!\n')
        self.play_again()
        

    def play_again(self):
        if self.continue_playing():
            self.round_ongoing = True
            self.run_game()
        elif not self.continue_playing:
            exit()
      

    def number_comparison(self, players_guess):
        if int(self.players_guess) < self.number_generated:
            return self.hints[0]
        elif int(self.players_guess) > self.number_generated:
            return self.hints[1]
        elif int(self.players_guess) == self.number_generated:
            self.round_ongoing = False
            return self.hints[2]


class ExampleGame2():

    def __init__(self):
        self.location = 'The Example game 2'

    def commence_game(self):
        print('game commencing' + self.location)
        pass

    