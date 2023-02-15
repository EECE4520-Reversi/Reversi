from Logic import logic
from Move import move

class game():

    def __init__(self, size=8) -> None:
        # initialize logic, board, and players
        self.myLogic = logic(8)

    def game_over(self):
        # makes call to logic game_over
        pass

    def get_move(self, x, y, p):
        # controller generates move from user input
        pass

    def make_move(self, move):
        # pass move to board for updating
        pass

    def end_game(self):
        pass
        
    
