from Move import move
from Board import board
from Tile import tile

class logic():

    def __init__(self, size=8) -> None:
        self.mySize = size
        self.myBoard = board(size)

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

            while (0 <= x < self.size and 0 <= y < self.size) and currentTile.getPlayer != move.getPlayer:
                temp.append(currentTile)
                currentTile = self.board(currentTile.getX + tile[0], currentTile.getY + tile[1])

            if (0 <= x < self.size and 0 <= y < self.size) and currentTile.getPlayer == move.getPlayer:
                for t in temp:
                    flipped.append(t)
                continue
            else:
                continue
        return flipped, checked


    def calculate_move(self, move):
        # returns list of tiles to be flipped
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

            while ( 0 <= x < self.size and 0 <= y <= self.size ) and currentTile.getPlayer != move.getPlayer:
                temp.append(currentTile)
                currentTile = self.board(currentTile.getX + tile(0), currentTile.getY + tile(1))
            
            # if path is valid, save flippable tiles
            if (0 <= x < self.size and 0 <= y < self.size) and currentTile.getPlayer == move.getPlayer:
                if len(temp) > 0:
                    for t in temp:
                        flipped.append(t)
            else:
                continue

        
        self.myBoard.update_board(flipped, move.get_player())
    
    def game_over(self, forfeit=False):
        # returns true if game is over
        # returns false if game is not over
        
        # first checks for a forfeit
        if forfeit == True:
            return True

        # If no forfeit, we check all spaces on the board.
        # If no valid moves exist, return true and end game.
        # If valid moves exist, save the tiles to show user and return false.
        # If one player cannot make a move, the play passes to the other player.
                
        flipped_discs = []

        for row in range(self.board.size):
            for column in range(self.board.size):
                self.board


        return 0
    
    


        
