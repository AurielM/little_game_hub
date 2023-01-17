import inquirer
from number_guessing import RandomNumberG
from number_guessing import ExampleGame2

class Hub:
    """
    This will provide the menu of games available to be played.
    """


    def __init__(self):
        self.location = 'The little_game_hub' 
        self.player_score = 0
        self.player_name = None
        self.new_player = True # game_count is true when the player has just entered the game
        self.numer_guessing = RandomNumberG
        self.example_game2 = ExampleGame2

    def introduce_player(self):
        
        self.player_name = input('\nInput your name here: ')
        
        if self.player_name == '':
            self.player_name = 'player'


    def welcome_message(self):
        if self.new_player:
            print(f'\n Welcome to the {self.location}, {self.player_name}! Your score is: {self.player_score}\n\n')
        else:
            print(f'Welcome back {self.player_name}! Your score is: {self.player_score}\n\n')


    def main_menu(self):
        self.welcome_message()
        if self.location == 'The little_game_hub': 
            choose_game = [
                inquirer.List('Choice of Game',
                    message="What game would you like to play? \n To exit game: 'Ctrl + c'.",
                    choices=['Number Guessing Game', 'Hangman', 'Rock Paper Scissors', 'Other'],
                    carousel=True
                ),]
            answers = inquirer.prompt(choose_game)
        else:
            stay_or_nay = [
                inquirer.Confirm("Continue", message="Play another round?", default=False
                ),]
            answers = inquirer.prompt(stay_or_nay)
        return(answers)


    def get_choices(answers): 
        available_games = {RandomNumberG(): "Number guessing game", ExampleGame2: "Hangman"}
        game_choices = list(available_games.values)
        
        return game_choices()

