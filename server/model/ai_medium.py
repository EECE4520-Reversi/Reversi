from model.ai import AI
from model.board import Board
from model.enums import Difficulty


class AI_Medium(AI):
    """A class to represent AI agents operating with a medium difficulty"""

    difficulty = Difficulty.MEDIUM

    def heuristic(self, board: Board):
        """Given a board, calculate the heuristic score assuming the player is white (player 1)"""
        tile_score = board.get_score()
        # white score - black score
        heuristic_result = tile_score[0] - tile_score[1]

        return heuristic_result
