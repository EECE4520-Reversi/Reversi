import asyncio
import copy

from model.board import Board
from model.enums import TileState, GameType, GameState
from model.logic import Logic
from model.move import Move


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
        self.difficulty = search_depth
        self.board_id = board_id
        # game_type = 1: Local Game
        # game_type = 2: AI Game
        # game_type = 3: Online Game
        self.game_type = GameType(game_type)
        self.lock = asyncio.Lock()

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
            bool: True if move was successful. False on error.
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

    def take_ai_turn(self) -> bool:
        """Calls necessary logic to interpret an AI's move
        Returns:
            bool: True if move was successful. False on error.
        """

        # pass Move to logic for calculating and updating
        nextMove = self.minimax_decision(self.logic.board, self.difficulty)
        # Make the move to switch players
        if nextMove is not None:
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

    def minimax_decision(self, board: Board, search_depth: int = 3) -> Move:
        """ "Given a board, assuming it is player 2's turn,
        returns the move that is best to take for player 2"""
        for row in board.matrix:
            for tile in row:
                if tile.player == TileState.VIABLE:
                    # create a temporary game to calculate moves made on this tile
                    temp_game = Game(size=board.size)
                    temp_game.logic.current_player = GameState.PLAYER2
                    temp_game.logic.board = self.logic.board.clone()

                    # take the next turn with the current valid tile
                    temp_game.take_turn(tile.x, tile.y)
                    tile.minimax_score = self.minimax(
                        temp_game.logic.board, GameState.PLAYER1, 1, search_depth
                    )

        # sift through board, find minimum score and return the move
        move = None
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
        if board_state != GameState.GAMEOVER and current_depth <= search_depth:
            # for each valid move, calculate its minimax value
            minimax_values = []
            for row in board.matrix:
                for tile in row:
                    if tile.player == TileState.VIABLE:
                        # create a temporary game to calculate moves made on this tile
                        temp_game = Game(size=board.size)
                        temp_game.logic.current_player = board_state
                        temp_game.logic.board = copy.deepcopy(board)

                        # take the next turn with the current valid tile
                        temp_game.take_turn(tile.x, tile.y)

                        # find the state of the new board after the turn
                        """1: Player 1's turn (black)
                           2: Player 2's turn (white)
                           3: Game over"""
                        if temp_game.logic.game_over():
                            next_state = GameState.GAMEOVER
                        else:
                            next_state = temp_game.logic.current_player

                        # call minimax
                        minimax_values.append(
                            self.minimax(
                                temp_game.logic.board,
                                next_state,
                                current_depth + 1,
                                search_depth,
                            )
                        )

            # take the min minimax value if it is AI turn or max value if it is the player
            # TODO: min/max raises if it has an empty sequence
            if not minimax_values:
                return self.heuristic(board)
            elif current_depth % 2 == 0:
                return min(minimax_values)
            else:
                return max(minimax_values)

        # if we have reached the end of the search depth, return the heuristic value
        else:
            return self.heuristic(board)

    def heuristic(self, board: Board):
        """Given a board, calculate the heuristic score assuming the player is white"""
        tile_score = board.get_score()
        # white score - black score
        heuristic_result = tile_score[0] - tile_score[1]

        return heuristic_result

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
        )
        return game
