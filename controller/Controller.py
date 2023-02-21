from model.Game import Game

class GameController:
    def __init__(self, game) -> None:
        self.currentGame = game
  
    # sends a move to the board
    def send_move(self, x, y) -> None:
        self.currentGame.take_turn(x, y)

    # returns the 1D board matrix
    def get_board(self):
        return self.currentGame.get_board_data()

    # returns the game state
    # 1 = player 1's (white) turn
    # 2 = player 2's (black) turn
    # 3 = game over
    def get_state(self):
        if (self.currentGame.myLogic.game_over()):
            return 3
        else:
            return self.currentGame.myLogic.current_player

    # returns the winner
    # 0 = tie
    # 1 = white
    # 2 = black
    def get_winner(self):
        self.currentGame.end_game()

    # returns an array of the game score in the form of [whiteScore, blackScore]
    def get_score(self):
        self.currentGame.get_score()





