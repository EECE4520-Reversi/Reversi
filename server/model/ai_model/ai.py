from model.board import Board
from abc import abstractmethod

class AI:
    """A class to represent AI agents to play against the user

    Attributes
    ----------

    Methods
    -------
    minimax_decision(board, search depth):
        Given a board and search depth, finds the best move for the AI to make using minimax
    minimax(board, board state, current depth):
        Given a board, the state, and the current depth of the search, finds best minimax value
    heuristic(board):
        Given a board, finds the heuristic value of the board
    """

    def __init__(self) -> None:
        """Constructs all necessary attributes for an AI player"""

    @abstractmethod
    def minimax_decision(self):
        """ "Given a board, assuming it is player 2's turn,
        returns the move that is best to take for player 2"""
        pass

    @abstractmethod
    def minimax(self):
        """Given a board, board state, the current depth of the algorithm
        Returns the best minimax score of the valid moves"""
        pass

    @abstractmethod
    def heuristic(self):
        """Given a board, calculate the heuristic score assuming the player is white (player 1)"""
        pass