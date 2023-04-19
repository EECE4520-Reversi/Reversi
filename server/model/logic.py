from typing import List

from model.board import Board
from model.enums import GameState, TileState
from model.move import Move
from model.tile import Tile


class Logic:
    """A class to represent a game's logic.

    ...

    Attributes
    ----------
    size : int
        the number of tiles in any row or column of the desired game
    current_player : int
        int indicating current player's turn
    board : Board
        the game board to which logic is applied

    Methods
    -------
    switch_players():
        Switches which player is the current player
    calculate_move(move):
        Updates board with results of passed move
    validate_move(move):
        Checks move to verify it is allowed
    find_valid_moves(update_board_flag):
        Scans board to find valid moves
    game_over():
        Checks if the game can not continue
    matrix:
        Returns current state of game board
    """

    def __init__(self, size: int = 8, board: Board = None, player: int = 1) -> None:
        """Constructs all necessary attributes for a single game

        Args:
            size (int, optional): the length of the board. Defaults to 8.
            player (int, optional): the starting player. Defaults to 1.
        """
        self.size = size
        self.board = board
        self.current_player = GameState(player)
        if not self.board:
            self.board = Board(size)
            self.board.initialize_board()
        self.find_valid_moves(True)

    @property
    def opposite_player(self):
        return 3 - self.current_player

    def switch_players(self) -> None:
        """Switches which player is the current player"""
        self.current_player = 3 - self.current_player

    def calculate_move(self, move: Move):
        """Updates board with results of passed move

        Args:
            move (Move):
                Move to be calculated

        Returns:
            bool: True if move was succesful, False otherwise
        """

        # Call validate_move() on given move
        tiles_to_flip = self.validate_move(move, self.current_player)
        # If no flip tiles found, move was invalid
        if len(tiles_to_flip) == 0:
            return False

        # If any flip tiles found, continue
        # Append given move to list
        tiles_to_flip.append(Tile(TileState.VIABLE, move.col, move.row))

        # Update board by flipping all found tiles to the current player's state
        self.board.update_board(tiles_to_flip, self.current_player)

        # The move was valid, so True is returned
        return True

    def validate_move(self, move: Move, player: int):
        """Checks move to verify it is allowed

        This function checks each cardinal and diagonal path from the given
        tile. If the path consists of tiles belonging to the opposite player
        and ends in a tile belonging to the current player, then all
        intermediate tiles in that path should be flipped.

        If at least one such path exists, the move is valid and all flippable
        tiles are returned.
        Otherwise, the move is invalid and an empty list is returned

        Args:
            move (Move): The move to be verified
            player (int): Player to check

        Returns:
            list:
                The tiles that would be flipped from this move
        """

        # sanity check
        if not (0 <= move.row < self.size) or not (0 <= move.col < self.size):
            return []

        # fmt: off
        border = [[-1, -1], [0, -1], [1, -1],
                  [-1, 0],           [1, 0],
                  [-1, 1],  [0, 1],  [1, 1]]
        # fmt: on
        flipped = []

        # Check each border tile
        for i in range(8):
            x_offset, y_offset = border[i]
            # print("checking path ", i, " along x ", x_offset, " and y ", y_offset)
            # Get the position of border tile with relative offset
            x = move.col + x_offset
            y = move.row + y_offset
            temp = []
            # Check if first path tile is within board limits and belongs to other player
            if (
                (0 <= x < self.size)
                and (0 <= y < self.size)
                and self.board.get_tile(x, y).player == 3 - player
            ):
                x += x_offset
                y += y_offset

                # Skip path if tile is out of board limits
                if self.size <= x or x < 0 or self.size <= y or y < 0:
                    continue

                # track tiles along each potential path
                # temp.append(self.board.get_tile(x, y))

                # loop through path tiles until your end tile is found
                while self.board.get_tile(x, y).player == 3 - player:
                    x += x_offset
                    y += y_offset

                    # break if out of bounds
                    if self.size <= x or x < 0 or self.size <= y or y < 0:
                        break
                    # print("Temp tile found at ", x, ", ", y)
                    # temp.append(self.board.get_tile(x, y))

                # At this point the path has ended either out of bounds
                #  or at a tile that is empty or belongs to current player

                # Skip if path terminates out of bounds
                if self.size <= x or x < 0 or self.size <= y or y < 0:
                    continue

                if self.board.get_tile(x, y).player == player:
                    while True:
                        x -= x_offset
                        y -= y_offset

                        if (x, y) == (move.col, move.row):
                            break
                        flipped.append(self.board.get_tile(x, y))
        # Once all paths checked, return list of all tiles to be flipped
        return flipped

    def find_valid_moves(
        self, update_board_flag: bool, player: int = None
    ) -> List[Move]:
        """Scans the whole board to find all valid moves for current player

        Args:
            update_board_flag (bool): Selects whether the found tiles should be
                displayed on the game board
            player (int): Player to check for moves

        Returns:
            bool: returns True if any valid moves are found, otherwise False
        """
        # Track number of valid moves to determine return value
        valid_moves = []
        player = player if player is not None else self.current_player

        # check each tile on board
        for row in self.board.matrix:
            for tile in row:
                # If tile was previously updated to be valid, we remove
                # that validation to re-validate for the current player
                state = tile.player
                if state == 3:
                    tile.player = 0
                # skip tile if occupied by player tile
                elif state in [1, 2]:
                    continue

                # Create a temp move for each empty tile and pass
                # it to validate_move
                temp_move = Move(tile.x, tile.y)

                # If move is invalid, continue to next tile
                if len(self.validate_move(temp_move, player)) == 0:
                    continue

                # If move is valid, increment valid moves counter
                # and check if the tile should be updated.
                if update_board_flag:
                    tile.player = 3
                valid_moves.append(temp_move)

        # Return True if valid_moves is nonzero
        return valid_moves

    def game_over(self):
        """Checks board to see if game is over

        There are two conditions to check:
            1. All tiles have been used
            2. Neither player has a valid move available

        Checking for condition 1. is much faster,
        but condition 2 covers condition 1.
        So, we will check for condition 2 after each turn.

        Returns:
            bool: True if the game is over, False otherwise
        """

        # Load current board state
        tiles = self.board.flat_board

        # Check if current player still has valid moves
        for tile in tiles:
            if tile == 3:
                return False

        # If other player cannot move, game is over
        if len(self.find_valid_moves(False, self.opposite_player)) == 0:
            return True

        # If other player can move, game is over
        return False

    def get_board(self) -> List[int]:
        """Getter for current board state as a 1D array of tile states

        Returns:
            list: Array of all current tile states on the game board
        """
        return self.board.flat_board

    def to_dict(self):
        return {
            "size": self.size,
            "board": self.board.to_dict(),
            "current_player": self.current_player,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get("size"),
            Board.from_dict(data.get("board")),
            data.get("current_player"),
        )
