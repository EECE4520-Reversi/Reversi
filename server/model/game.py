from model.logic import Logic
from model.move import Move


class Game:
    def __init__(self, size: int = 8) -> None:
        # initialize logic, board, and players
        self.logic = Logic(size)
        self.running = True
        self.winner = 0
        self.size = size

    def take_turn(self, x: int, y: int):
        # returns true if turn ends
        # return false if game ends
        #
        # # update board to show valid moves for player p
        # if not self.logic.find_valid_moves(False):
        #     # skips turn if no valid moves are found
        #     return True

        # display most current board (with valid moves highlighted)
        currentBoard = self.get_board_data()
        # get most recent score
        score = self.get_score()

        # pass Move to logic for calculating and updating
        nextMove = Move(x, y)
        self.make_move(nextMove)
        self.logic.find_valid_moves(True)

        # check if game is over
        if self.game_over():
            # get winner and end turn
            self.winner = self.end_game
            return False

        # end turn
        return True

    def game_over(self):
        # makes call to logic game_over
        if self.logic.game_over():
            return True
        else:
            return False

    def make_move(self, move: Move):
        # pass Move to board for updating
        return self.logic.calculate_move(move)

    def get_board_data(self):
        # Returns flat array of size*size length containing tile states
        return self.logic.get_board()

    def get_score(self):
        return self.logic.board.get_score()

    def end_game(self):
        # return winner
        #   # 1 if White
        #   # 2 if Black
        #   # 0 if tie
        score = self.get_score()
        if score[0] > score[1]:
            return 1
        elif score[0] < score[1]:
            return 2
        else:
            return 0
