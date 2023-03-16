from typing import List

from model.board import Board
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
    get_board():
        Returns current state of game board
    """

    def __init__(self, size: int = 8, player: int = 1) -> None:
        """Constructs all necessary attributes for a single game

        Args:
            size (int, optional): the length of the board. Defaults to 8.
            player (int, optional): the starting player. Defaults to 1.
        """
        self.size = size
        self.board = Board(size)
        self.current_player = player
        self.find_valid_moves(True)

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
        tiles_to_flip = self.validate_move(move)
        # If no flip tiles found, move was invalid
        if len(tiles_to_flip) == 0:
            return False

        # If any flip tiles found, continue
        # Append given move to list
        tiles_to_flip.append(Tile(3, move.get_col(), move.get_row()))

        # Update board by flipping all found tiles to the current player's state
        self.board.update_board(tiles_to_flip, self.current_player)

        # Switch players now that a valid move has been made
        self.switch_players()

        # The move was valid, so True is returned
        return True

    def validate_move(self, move: Move):
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

        Returns:
            list:
                The tiles that would be flipped from this move
        """
        border = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
        flipped = []

        # Check each border tile
        for i in range(8):
            tile = border[i]

            # Get the position of border tile with relative offset
            x = move.get_col() + tile[0]
            y = move.get_row() + tile[1]

            # Continue if border tile is within board limits
            if (x < 0 or x >= self.size) or (y < 0 or y >= self.size):
                continue

            # Begin tracking path starting at border tile
            currentTile = self.board.get_tile(x, y)
            temp = []

            # Stop if board edge reached OR tile belongs to opposing player
            while (
                0 <= currentTile.getX() < self.size - 1
                and 0 <= currentTile.getY() < self.size - 1
            ) and 3 - currentTile.get_player() == self.current_player:
                # If path tile is potentially flippable, save it in temp list
                temp.append(currentTile)

                # Step along path using relative offset of border tile
                currentTile = self.board.get_tile(
                    currentTile.getX() + tile[0], currentTile.getY() + tile[1]
                )

            # If stopped by tile belonging to opposing player, save path
            if (
                0 <= x < self.size and 0 <= y < self.size
            ) and currentTile.get_player() == self.current_player:
                flipped += temp
                continue
            # If stopped by tile being outside of board, discard path
            else:
                continue
            # Continue to check next path direction

        # Once all paths checked, return list of all tiles to be flipped
        return flipped

    def find_valid_moves(self, update_board_flag: bool):
        """Scans the whole board to find all valid moves for current player

        Args:
            update_board_flag (bool): Selects whether the found tiles should be
                displayed on the game board

        Returns:
            bool: returns True if any valid moves are found, otherwise False
        """
        # Track number of valid moves to determine return value
        valid_moves = 0

        # check each tile on board
        for row in self.board.get_board():
            for tile in row:
                # If tile was previously updated to be valid, we remove
                # that validation to re-validate for the current player
                state = tile.get_player()
                if state == 3:
                    tile.set_player(0)

                # skip tile if occupied by player tile
                if state == 1 or state == 2:
                    continue
                else:
                    # Create a temp move for each empty tile and pass
                    # it to validate_move
                    tempMove = Move(tile.getX(), tile.getY())

                    # If move is invalid, continue to next tile
                    if len(self.validate_move(tempMove)) == 0:
                        continue

                    # If move is valid, increment valid moves counter
                    # and check if the tile should be updated.
                    else:
                        if update_board_flag:
                            tile.set_player(3)
                        valid_moves += 1

        # Return True if valid_moves is nonzero
        return valid_moves != 0

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
        tiles = self.board.get_board(True)

        # Check if current player still has valid moves
        for tile in tiles:
            if tile == 3:
                return False

        # If current player cannot move, switch players
        self.switch_players()

        # If other player cannot move, game is over
        if not self.find_valid_moves(True):
            return True

        # If other player can move, game is over
        return False

    def get_board(self) -> list[int]:
        """Getter for current board state as a 1D array of tile states

        Returns:
            list: Array of all current tile states on the game board
        """
        return self.board.get_board(True)
