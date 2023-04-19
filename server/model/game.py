import asyncio
import copy
from typing import List

from model.board import Board
from model.enums import TileState, GameType, GameState, Difficulty
from model.logic import Logic
from model.move import Move
from model.user import User


class Game:
    """Interface object between controller and model

    ...

    Attributes
    ----------
    logic : Logic
        the logic instance associated with this game
    running : bool
        indicates whether this game has ended
    winner : int
        the winner determined at the end of the game

    Methods
    -------
    take_turn():
        Calls necessary logic to interpret a player's move
    game_over(move):
        Checks if the game is still running
    make_move(move):
        Passes move to logic to be verified and placed
    get_board_data(update_board_flag):
        Gets list of current tile states from board
    get_score():
        Gets current score of game
    end_game():
        Returns winner of game and saves final game data
    """

    def __init__(
        self,
        board_id: str = None,
        size: int = 8,
        search_depth: int = 1,
        game_type: int = GameType.AI,
        logic: Logic = None,
        running: bool = True,
        winner: int = 0,
        players: List[str] = [],
    ) -> None:
        """Initialize logic, board, and players

        Args:
            size (int, optional): Size of the game board. Defaults to 8.
        """
        # initialize logic, board, and players
        self.logic = logic or Logic(size)
        self.running = running
        self.winner = winner
        self.size = size
        self.difficulty = Difficulty(search_depth)
        self.board_id = board_id
        # game_type = 1: Local Game
        # game_type = 2: AI Game
        # game_type = 3: Online Game
        self.game_type = GameType(game_type)
        self.players = players

    def reset(self):
        self.logic = Logic(self.size)
        self.running = True
        self.winner = 0

    def take_turn(self, x: int, y: int) -> bool:
        """Calls necessary logic to interpret a player's move

        Args:
            x (int): x-position of given move
            y (int): y-position of given move

        Returns:
            bool: True if game is not over after the move
        """
        # print(f"Making move at [{x}, {y}]")
        # pass Move to logic for calculating and updating
        nextMove = Move(x, y)
        self.make_move(nextMove)
        self.logic.switch_players()

        # Update valid moves for next player
        self.logic.find_valid_moves(True)

        # check if game is over
        if self.game_over():
            # get winner and end turn
            self.winner = self.end_game()
            return False

        # end turn
        return True

    def game_over(self) -> bool:
        """Checks if the game is still running

        Returns:
            bool: True if the game is over, otherwise False
        """
        return self.logic.game_over()

    def make_move(self, move: Move) -> bool:
        """Passes move to logic to be verified and placed

        Args:
            move (Move): The move received from controller

        Returns:
            bool: True if move was successful. False on error.
        """
        # pass Move to board for updating
        success = self.logic.calculate_move(move)
        return success

    def get_board_data(self) -> list[int]:
        """Gets list of current state tiles from board

        Returns:
            list[int]: List of current state tiles
        """
        # Returns flat array of size*size length containing tile states
        return self.logic.get_board()

    def get_score(self) -> list[int]:
        """Gets current score of game

        Returns:
            list: contains each player's score on the current board
        """
        return self.logic.board.get_score()

    def end_game(self) -> int:
        """Returns winner of game and saves final game data

        Returns:
            int: player who won
                0 if tie
                1 if white
                2 if black
        """
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

    def calculate_elos(self, winner: User, loser: User, score_diff):
        default_elo_change = 30
        elo_diff_factor = (loser.get_elo() - winner.get_elo()) // 50
        score_diff_factor = score_diff // 20
        scaled_elo_change = default_elo_change + elo_diff_factor + score_diff_factor
        winner.gain_elo(scaled_elo_change)
        loser.lose_elo(scaled_elo_change)

    @property
    def current_turn(self) -> GameState:
        """Returns the current player

        Returns:
            int: Player's turn
        """
        return GameState(self.logic.current_player)

    def to_dict(self):
        return {
            "_id": self.board_id,
            "logic": self.logic.to_dict(),
            "running": self.running,
            "winner": self.winner,
            "size": self.size,
            "difficulty": self.difficulty,
            "game_type": self.game_type,
            "players": self.players,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Game":
        game = cls(
            data.get("_id"),
            data.get("size"),
            data.get("difficulty"),
            data.get("game_type"),
            Logic.from_dict(data.get("logic")),
            data.get("running"),
            data.get("winner"),
            data.get("players"),
        )
        return game
