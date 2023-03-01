from typing import List

from model.tile import Tile


class Board:
    """A class to represent a game's board state

    ...

    Attributes
    ----------
    size : int
        the number of tiles in any row or column of the desired game
    tile_score : list
        list of curren tile counts for both players
    matrix : list[list]
        2D array of tiles to represent current board state

    Methods
    -------
    get_board(flattened:bool):
        Returns current state of game board
    initialize_board():
        Fills the board during initialization with default state
    get_score():
        Calculates score from current state
    update_board(flip_list: list[tile], player: int):
        Updates given tiles with given player state
    get_winner():
        Returns player with higher score
    get_tile(pos_x: int, pos_y: int):
        returns Tile object at given position
    """

    def __init__(self, size: int = 8) -> None:
        """Constructs all necessary objects for a single board

        Args:
            size (int, optional): Size of the board. Defaults to 8.
        """
        self.tileScore = [0, 0]
        self.size = size
        self.matrix = [[Tile() for _ in range(self.size)] for _ in range(self.size)]
        self.initialize_board()

    def get_board(self, flattened: bool = False):
        """Gets the state of each tile on the board

        Args:
            flattened (bool, optional): Board states returned as a 1D array
            if True. Defaults to False.

        Returns:
            list[list[Tile]]: matrix of Tiles
                OR
            list[int]: list of tile states
        """
        # If flag is False, return the 2D matrix as is
        if not flattened:
            return self.matrix

        # If flag is True, grab each tile state and store in a list to return
        flat_board = []
        for row in self.matrix:
            for tile in row:
                flat_board.append(tile.get_player())
        return flat_board

    def initialize_board(self) -> None:
        """Fills the board during initialization with default state"""

        # Assign all tiles correct position data
        for a in range(self.size):
            for b in range(self.size):
                self.matrix[a][b].set_posx(b)
                self.matrix[a][b].set_posy(a)

        # fill middle 4 tiles with starting configuration
        midLow = self.size // 2 - 1
        midHigh = self.size // 2

        self.matrix[midLow][midLow].set_player(2)
        self.matrix[midLow][midHigh].set_player(1)
        self.matrix[midHigh][midLow].set_player(1)
        self.matrix[midHigh][midHigh].set_player(2)

        # No return data
        return

    def get_score(self) -> list[int]:
        """Calculates score from current state

        Returns:
            list: list of each players most recent score
        """

        # Initialize score counters
        black_score = 0
        white_score = 0

        # Iterate over each tile to check player state
        for row in self.matrix:
            for tile in row:
                # If black tile, increment black score, else increment white
                if tile.get_player == 1:
                    white_score += 1
                elif tile.get_player == 2:
                    black_score += 1

        # Pack two scores into list for return
        self.tileScore = [white_score, black_score]
        return self.tileScore

    def update_board(self, flip_list: List[Tile], player: int) -> None:
        """Updates given tiles with given player state

        Args:
            flip_list (List[Tile]): list of tiles to be updated
            player (int): new player state for flipped tiles
        """
        # Set player of each tile by using position values
        for tile in flip_list:
            self.matrix[tile.getY()][tile.getX()].set_player(player)

        # Update score to reflect changes
        self.get_score()

        # No return value
        return

    def get_winner(self):
        """Returns player with higher score

        Returns:
            int: player who won
                returns integer:
                0 = no winner
                1 = White wins
                2 = Black wins
        """
        # returns integer:
        # 0 = no winner
        # 1 = White wins
        # 2 = Black wins

        if self.tileScore[0] > self.tileScore[1]:
            return 1
        elif self.tileScore[0] < self.tileScore[1]:
            return 2
        else:
            return 0

    def get_tile(self, pos_x: int, pos_y: int) -> Tile:
        """returns Tile object at given position

        Args:
            pos_x (int): which row to check for tile in
            pos_y (int): which col to check for tile in

        Returns:
            Tile: pointer to tile object at provided position
        """
        return self.matrix[pos_y][pos_x]
