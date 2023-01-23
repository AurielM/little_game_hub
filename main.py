import inquirer

from gamebase import GameBase
from number_guessing import RandomNumberG, ExampleGame2

game_ongoing = True


def player_choice():
        choose_game = [
            inquirer.List('Choice of Game',
                message="What game would you like to play?",
                choices=[
                    ('Number Guessing Game', RandomNumberG), 
                ('Hangman', ExampleGame2), 
                ('Exit game', exit)
                ],
                carousel=True
            ),]
        answers = inquirer.prompt(choose_game)
        return answers['Choice of Game']().run_game()

GameBase.player_name = input('\nType your name here:')

if GameBase.player_name == '':
    GameBase.player_name = 'player'


while game_ongoing == True:

    game = player_choice()
