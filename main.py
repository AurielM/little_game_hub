import inquirer

class Hub:
    """
    This will provide the menu of games available to be played.
    """


    def __init__(self):
        self.location = 'The little_game_hub' 
        self.player_score = 0
        self.player_name = None
        self.game_count = 0


    def introduce_player(self):
        
        self.player_name = input('\nInput your name here: ')
        
        if self.player_name == '':
            self.player_name = 'player'


    def welcome_message(self):
        if self.game_count == 0:
            print(f'\n Welcome to the {self.location}, {self.player_name}! Your score is: {self.player_score}\n\n')
        else:
            print(f'Welcome back {self.player_name}! Your score is: {self.player_score}\n\n')


    def main_menu(self):
        game.welcome_message()
        if self.location == 'The little_game_hub': 
            questions = [
                inquirer.List('Choice of Game',
                    message="What game would you like to play? \n To exit game: 'Ctrl + c'.",
                    choices=['Number Guessing: undergoing maintenance', 'Hangman: undergoing maintenance', 'Rock Paper Scissors: undergoing maintenance', 'Other'],
                    carousel=True
                ),]
            answers = inquirer.prompt(questions)
        else:
            questions = [
                inquirer.Confirm("Continue", message="Play another round?"),
                inquirer.Confirm("Return", message="Return to the little game hub?", default=True
                ),]
            answers = inquirer.prompt(questions)
        return(answers)


game = Hub()
game.introduce_player()
game.main_menu()