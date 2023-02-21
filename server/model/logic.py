from typing import List

from model.board import Board
from model.move import Move
from model.tile import Tile


class Logic:
    def __init__(self, size: int = 8, player: int = 1) -> None:
        self.size = size
        self.board = Board(size)
        self.current_player = player
        self.find_valid_moves(True)

    def switch_players(self):
        self.current_player = 3 - self.current_player

    def calculate_move(self, move: Move):
        # returns true if Move was successful
        # retursn false if not
        border = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
        flipped: List[Tile] = []

        # if Move is invalid, return an empty list
        tiles_to_flip, checked = self.validate_move(move)
        if len(tiles_to_flip) == 0:
            return flipped

        flipped += tiles_to_flip
        flipped.append(Tile(3, move.get_col(), move.get_row()))

        # continue where validate_move() left off
        for i in range(checked, 7):
            tile = border[i]
            x = move.get_col() + tile[0]
            y = move.get_row() + tile[1]
            currentTile = self.board.get_tile(x, y)
            temp = []
            checked += 1

            while (
                0 <= x < self.size and 0 <= y <= self.size
            ) and currentTile.get_player() != self.current_player:
                temp.append(currentTile)
                currentTile = self.board.get_tile(
                    currentTile.getX() + tile[0], currentTile.getY() + tile[1]
                )

            # if path is valid, save flippable tiles
            if (
                0 <= x < self.size and 0 <= y < self.size
            ) and currentTile.get_player() == self.current_player:
                if len(temp) > 0:
                    for t in temp:
                        flipped.append(t)
            else:
                continue

        if len(flipped) != 0:
            self.board.update_board(flipped, self.current_player)
            self.switch_players()
            return True
        else:
            return False

    def validate_move(self, move: Move):
        # returns a list that contains the tiles that should be flipped
        # for this Move, and how many border tiles have been checked
        border = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
        checked = 0
        flipped = []

        # check each border tile for opposite state
        for i in range(7):
            checked += 1
            tile = border[i]
            x = move.get_col() + tile[0]
            y = move.get_row() + tile[1]
            currentTile = self.board.get_tile(x, y)
            temp = []

            while (
                0 <= x < self.size and 0 <= y < self.size
            ) and 3 - currentTile.get_player() == self.current_player:
                temp.append(currentTile)
                currentTile = self.board.get_tile(
                    currentTile.getX() + tile[0], currentTile.getY() + tile[1]
                )

            if (
                0 <= x < self.size and 0 <= y < self.size
            ) and currentTile.get_player() == self.current_player:
                flipped += temp
                continue
            else:
                continue
        return flipped, checked

    def find_valid_moves(self, update_board_flag: bool):
        # updates self.board with valid Move tiles
        # returns false if no valid moves are found
        valid_moves = 0
        # check each tile
        for row in self.board.get_board():
            for tile in row:
                # mark tile as empty to correct for last run
                state = tile.get_player()
                if state == 3:
                    tile.set_player(0)
                # skip tile if occupied
                if state == 1 or state == 2:
                    continue
                else:
                    tempMove = Move(tile.getX(), tile.getY())
                    if len(self.validate_move(tempMove)[0]) == 0:
                        continue
                    else:
                        if update_board_flag:
                            tile.set_player(3)
                        valid_moves += 1

        return valid_moves != 0

    def game_over(self):
        return False
        # TODO: Fix
        if not self.find_valid_moves(1, False) and not self.find_valid_moves(2, False):
            return True
        else:
            return False

    def get_board(self):
        return self.board.get_board(True)
