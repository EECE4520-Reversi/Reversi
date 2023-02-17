from Move import move
from Board import board

class logic():

    def __init__(self, size=8, player=1) -> None:
        self.mySize = size
        self.myBoard = board(size)
        self.current_player = player

    def switch_players(self):
        self.current_player = 3 - self.current_player

    def calculate_move(self, move: move):
        # returns true if move was successful
        # retursn false if not
        border = [
                  [-1,-1], [0, -1], [1, -1],
                  [-1, 0],          [1,  0],
                  [-1, 1], [0,  1], [1,  1]
                 ]
        checked = 0
        flipped = []

        # if move is invalid, return an empty list
        move_checked = self.validate_move(move)
        if len(move_checked[0]) == 0:
            return flipped
        
        for i in move_checked[0]:
            flipped.append(i)
        checked = move_checked[1]

        # continue where validate_move() left off
        for i in range(checked, 7):
            tile = border[i]
            x = move.x + tile[0]
            y = move.y + tile[1]
            currentTile = self.myBoard.get_tile(x, y)
            temp = []
            checked += 1

            while ( 0 <= x < self.size and 0 <= y <= self.size ) and currentTile.get_player() != self.current_player:
                temp.append(currentTile)
                currentTile = self.board(currentTile.getX + tile(0), currentTile.getY + tile(1))
            
            # if path is valid, save flippable tiles
            if (0 <= x < self.size and 0 <= y < self.size) and currentTile.get_player() == self.current_player:
                if len(temp) > 0:
                    for t in temp:
                        flipped.append(t)
            else:
                continue

        if (len(flipped) != 0):
            self.myBoard.update_board(flipped, self.current_player)
            self.switch_players()
            return True
        else:
            return False 


    def validate_move(self, move: move):
        # returns a list that contains the tiles that should be flipped
        # for this move, and how many border tiles have been checked
        border = [
                  [-1,-1], [0, -1], [1, -1],
                  [-1, 0],          [1,  0],
                  [-1, 1], [0,  1], [1,  1]
                 ]
        checked = 0
        flipped = []

        # check each border tile for opposite state
        for i in range (7):
            checked += 1
            tile = border[i]
            x = move.x + tile[0]
            y = move.y + tile[1]
            currentTile = self.myBoard.get_tile(x, y)
            temp = []

            while (0 <= x < self.size and 0 <= y < self.size) and currentTile.get_player() != self.current_player:
                temp.append(currentTile)
                currentTile = self.board(currentTile.getX + tile[0], currentTile.getY + tile[1])

            if (0 <= x < self.size and 0 <= y < self.size) and currentTile.get_player() == self.current_player:
                for t in temp:
                    flipped.append(t)
                continue
            else:
                continue
        return flipped, checked


    def find_valid_moves(self, updateBoardFlag):
        # updates myBoard with valid move tiles 
        # returns false if no valid moves are found
        valid_moves = 0
        # check each tile
        for row in self.myBoard.get_board():
            for tile in row:
                # mark tile as empty to correct for last run
                state = tile.get_player()
                if (state == 3): tile.set_player(0)
                # skip tile if occupied
                if (state == 1 or state == 2):
                    continue
                else:
                    tempMove = move(tile.getX, tile.getY)
                    if (len(self.validate_move(tempMove)[0]) == 0):
                        continue
                    else:
                        if (updateBoardFlag == True):
                            tile.set_player(3)
                        valid_moves += 1
        if (valid_moves == 0):
            return False
        else: return True

    def game_over(self):
        if (not self.find_valid_moves(1, False) and not self.find_valid_moves(2, False)):
            return True
        else:
            return False            
