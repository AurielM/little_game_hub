
import inquirer

class GameBase:
    """
    This will provide the menu of games available to be played.
    """

    player_score = 0
    player_name = None


    def __init__(self):
        self.location = 'The little_game_hub' 


    def score_update(self):
        print(f'\nPlayer name: {self.player_name}\nCurrent score: {self.player_score}')


    def continue_playing(self):
        stay_or_nay = [
                    inquirer.Confirm("Continue", message="Play another round?", default=False
                    ),]
        inquirer.prompt(stay_or_nay)
        

    def introduce_location(self):
        print(f'\n Welcome to the {self.location}!')


    def run_game(self):
        self.score_update()
        self.continue_playing()
