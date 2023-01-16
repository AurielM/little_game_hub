import inquirer

class Hub:
    """
    This will provide the menu of games available to be played.
    """

    def __init__(self):
        self.location = 'The little_game_hub' 
        self.player_score = 0
        self.player_name = None

    def introduce_player(self):
        
        self.player_name = input('\nTo avoid being called \'player\' for the remainder of the game input your name here: ')
        
        if self.player_name == '':
            self.player_name = 'player'

        print(f'ok! Your name is {self.player_name}')

    def welcome_message(self):
        print(f'\n Welcome to the {self.location}, {self.player_name}!')

    def main_menu(self):
        questions = [
            inquirer.List('Choice of Game',
                message="What game would you like to play? \n To exit game: 'Ctrl + c'.",
                choices=['Number Guessing: undergoing maintenance', 'Hangman: undergoing maintenance', 'Rock Paper Scissors: undergoing maintenance', 'Other'],
                carousel=True
            ),]
        answers = inquirer.prompt(questions)
        return(answers)


game = Hub()
game.introduce_player()
game.welcome_message()
game.main_menu()