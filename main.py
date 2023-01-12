

class Hub:
    """
    
    """

    def __init__(self, location, player_score, player_name):
        Hub.location = location 
        Hub.player_score = player_score
        Hub.player_name = player_name

    def introduce_player():
        
        player_name = input('\nWelcome player! \n\n To avoid being called \'player\' for the remainder of the game input name here: ')
        
        if player_name == '':
            player_name = 'player'

        print(f'ok! Your name is {player_name}')


Hub.introduce_player()