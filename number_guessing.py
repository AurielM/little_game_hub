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
        self.hints = ['Too low!\n','Too high!\n', 'You win!\n', 'Out of guesses!\n']


    def run_game(self):
        super().run_game()
        self.guess_count = self.player_chances[self.difficulty_level_chosen]
        self.introduce_difficulty_level_chosen = f'Number of guesses: {self.guess_count}'
        print(f' {self.introduce_difficulty_level_chosen} \n{self.game_rules}')
        self.number_generated = randint(1, 100)
        
        while self.round_ongoing:
            self.players_guess = self.input_check(input_type_test=int, message='Player\'s guess:')
            if self.players_guess == 'invalid':
                pass
            else:
                print(self.number_comparison(self.players_guess))
                self.count_down()
        self.play_again()
        

    def play_again(self):
        print(f'Round over!\n')
        print(self.score_board())
        if self.continue_playing():
            self.round_ongoing = True
            self.run_game()

      
    def count_down(self):
        self.guess_count -= 1
        if self.guess_count > 0:
            if self.round_ongoing == True:
                print(f'{self.guess_count} chance(s) to guess the correct number')
        else:
            self.round_ongoing = False
            return self.hints[2]


    def number_comparison(self, players_guess):
        if self.guess_count == 0:
            self.round_ongoing = False
            return self.hints[3]  
        
        if self.players_guess < self.number_generated:
            return self.hints[0]
        elif self.players_guess > self.number_generated:
            return self.hints[1]
        elif self.players_guess == self.number_generated:
            self.round_ongoing = False
            self.player_score += 1
            return self.hints[2]


class HangManG(GameBase):
    """
    In this game you need to guess the word generated before the hangman is fully drawn
    Depending on the level of difficulty chosen you'll have to guess words of 4, 6 and 8 letters long
    Guess the word before your chances run out (you get 6 chances) and you win the round!

    You'll have the option of returning back to the main menu after each run
    """


    def __init__(self):
        super().__init__()
        self.location = 'Hang Man'
        self.player_chances = { 'Easy': 20, 
                                'Normal': 10, 
                                'Hard': 5
                                }
        self.game_rules = """ Rules:
        - A random word will be chosen
        - The objective is to guess the word's letters before you're out of guesses.
        - With each correct letter chosen, the word will appear.
        - You have have a limited number of wrong guesses before it's game over!
        """
        self.guess_count = int
        self.round_ongoing = True
        self.hints = ['Wrong letter!\n','Right letter!\n', 'You win!\n', 'Hang Man!\n']
    
        
    def commence_game(self):
        print('game commencing' + self.location)
        pass

    