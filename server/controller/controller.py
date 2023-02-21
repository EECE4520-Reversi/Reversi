from collections import defaultdict
from model.game import Game


class GameController:
    def __init__(self) -> None:
        self.games = defaultdict(lambda: Game())

    # sends a Move to the board
    def send_move(self, board_id: str, x: int, y: int) -> None:
        self.games[board_id].take_turn(x, y)

    # returns the 1D board matrix
    def get_board(self, board_id: str):
        return self.games[board_id].get_board_data()

    # returns the game state
    # 1 = player 1's (white) turn
    # 2 = player 2's (black) turn
    # 3 = game over
    def get_state(self, board_id: str):
        if self.games[board_id].logic.game_over():
            return 3
        else:
            return self.games[board_id].logic.current_player

    # returns the winner
    # 0 = tie
    # 1 = white
    # 2 = black
    def get_winner(self, board_id: str):
        self.games[board_id].end_game()

    # returns an array of the game score in the form of [whiteScore, blackScore]
    def get_score(self, board_id: str):
        self.games[board_id].get_score()

    def reset_game(self, board_id: str):
        self.games[board_id] = Game(self.games[board_id].size)

    def get_data(self, board_id: str):
        return {
            "board": self.get_board(board_id),
            "score": self.get_score(board_id),
            "state": self.get_state(board_id),
            "winner": self.get_winner(board_id)
        }
