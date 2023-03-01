from typing import List

from model.tile import Tile


class Board:
    def __init__(self, size: int = 8) -> None:
        self.tileScore = [0, 0]
        self.size = size
        self.matrix = [[Tile() for _ in range(self.size)] for _ in range(self.size)]
        self.initialize_board()

    def get_board(self, flattened: bool = False):
        # Return 1D array of all tile states
        if not flattened:
            return self.matrix
        flat_board = []
        for row in self.matrix:
            for tile in row:
                flat_board.append(tile.get_player())
        return flat_board

    def initialize_board(self):
        # create all tile objects with correct positions
        for a in range(self.size):
            for b in range(self.size):
                self.matrix[a][b].set_posx(b)
                self.matrix[a][b].set_posy(a)

        # fill middle 4 tiles with starting configuration
        midLow = self.size // 2 - 1  # default 3
        midHigh = self.size // 2  # default 4

        self.matrix[midLow][midLow].set_player(2)
        self.matrix[midLow][midHigh].set_player(1)
        self.matrix[midHigh][midLow].set_player(1)
        self.matrix[midHigh][midHigh].set_player(2)

    def get_score(self):
        black_score = 0
        white_score = 0

        for row in self.matrix:
            for tile in row:
                if tile.get_player == 1:
                    white_score += 1
                elif tile.get_player == 2:
                    black_score += 1

        self.tileScore = [white_score, black_score]
        return self.tileScore

    def update_board(self, flip_list: List[Tile], player: int):
        # updates tile
        for pos in flip_list:
            self.matrix[pos.getY()][pos.getX()].set_player(player)
        self.get_score()

    def get_winner(self):
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
        return self.matrix[pos_y][pos_x]
