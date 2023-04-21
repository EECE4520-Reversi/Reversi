from model.board import Board
from model.enums import TileState, GameState
from model.game import Game
from model.move import Move
from abc import abstractmethod
import copy


class AI:
    """A class to represent AI agents to play against the user

    ...

    Attributes
    ----------
    difficulty : int
        the difficulty level of the AI
        0 = easy (search depth = 1)
        1 = medium (search depth = 2)
        2 = hard (search_depth = 3)

    search_depth : int
        the depth of the search for the minimax algorithm

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

    def minimax_decision(self, board: Board, search_depth: int = 1) -> Move:
        """ "Given a board, returns the move that is best to take for the AI"""
        for row in board.matrix:
            for tile in row:
                if tile.player == TileState.VIABLE:
                    # create a temporary game to calculate moves made on this tile
                    temp_game = Game(size=board.size)
                    temp_game.logic.current_player = GameState.PLAYER2
                    temp_game.logic.board = board

                    # take the next turn with the current valid tile
                    temp_game.take_turn(tile.x, tile.y)
                    tile.minimax_score = self.minimax(
                        temp_game.logic.board, GameState.PLAYER1, 1, search_depth
                    )

        # sift through board, find minimum score and return the move
        min_score = 9999
        for row in board.matrix:
            for tile in row:
                if tile.player == TileState.VIABLE:
                    if tile.minimax_score < min_score:
                        min_score = tile.minimax_score
                        move = Move(tile.x, tile.y)

        return move

    def minimax(
        self, board: Board, board_state: int, current_depth: int, search_depth: int
    ) -> int:
        """Given a board, board state, the current depth of the algorithm
        Returns the best minimax score of the valid moves"""
        if board_state != 3 and current_depth != search_depth:
            # for each valid move, calculate its minimax value
            minimax_values = []
            for row in board.matrix:
                for tile in row:
                    if tile.player == TileState.VIABLE:
                        # create a temporary game to calculate moves made on this tile
                        temp_game = Game(size=board.size)
                        temp_game.logic.current_player = board_state
                        temp_game.logic.board = board

                        # take the next turn with the current valid tile
                        temp_game.take_turn(tile.x, tile.y)

                        # find the state of the new board after the turn
                        """1: Player 1's turn (black)
                           2: Player 2's turn (white)
                           3: Game over"""
                        if temp_game.logic.game_over():
                            next_state = 3
                        else:
                            next_state = temp_game.logic.current_player

                        # call minimax
                        minimax_values.append(
                            self.minimax(
                                temp_game.logic.board,
                                next_state,
                                current_depth + 1,
                                search_depth=search_depth,
                            )
                        )

            # find the current player based on search depth
            # take the min minimax value if it is AI turn or max value if it is the player
            # TODO: min/max raises if it has an empty sequence
            if current_depth % 2 == 0:
                return min(minimax_values)
            else:
                return max(minimax_values)

        return self.heuristic(board)

    @abstractmethod
    def heuristic(self):
        """Given a board, calculate the heuristic score assuming the player is white (player 1)"""
        pass
