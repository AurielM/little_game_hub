
import inquirer

class GameBase:
    """
    This will provide the menu of games available to be played.
    """

    player_score = 0
    player_name = None


    def __init__(self):
        self.location = 'The little_game_hub' 
        self.difficulty_levels = ['Easy', 'Normal', 'Hard']
        self.difficulty_level_chosen = None


    def score_board(self):
        print(f'\nPlayer name: {self.player_name}\nCurrent score: {self.player_score}')


    def continue_playing(self):
        stay_or_nay = [
                    inquirer.Confirm("Continue", message="Play another round?", default=False
                    ),]
        dcit_player_choice = inquirer.prompt(stay_or_nay)
        if dcit_player_choice['Continue']:
            return True
        else:
            return False
        

    def introduce_location(self):
        print(f'\nWelcome to the {self.location}!')


    def game_difficulty(self):
        self.choose_difficulty = [
            inquirer.List('Level of difficulty',
                message="What difficulty level would you like to play?",
                choices=self.difficulty_levels,
                carousel=True
            ),]
        answers = inquirer.prompt(self.choose_difficulty)
        self.difficulty_level_chosen = answers['Level of difficulty']


    def run_game(self):
        self.score_board()

