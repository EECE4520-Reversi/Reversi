from Logic import logic
from Move import move
from Tile import tile

class board():

    def __init__(self, size = 8) -> None:
        self.tileScore = [0, 0]
        self.matrix = [[tile() for i in range(self.size)] for i in range(self.size)]
        self.initialize_board(self)
        self.myTile = tile(0, 0, 1)
        self.mySize = size

    def get_board(self):
        # Return 1D array of all tile states
        flat_board = []
        for row in self.matrix:
            for tile in row:
                flat_board.append(tile.get_player())
        return flat_board

    def initialize_board(self):
        # create all tile objects with correct positions
        for a in range(self.size-1):
            for b in range(self.size-1):
                self.matrix[a][b].set_posx(b)
                self.matrix[a][b].set_posy(a)
        
        # fill middle 4 tiles with starting configuration
        midLow = self.size / 2 - 1 # default 3
        midHigh = self.size / 2    # default 4
        
        self.matrix[midLow][midLow].set_player(1)
        self.matrix[midLow][midHigh].set_player(2)
        self.matrix[midHigh][midLow].set_player(2)
        self.matrix[midHigh][midHigh].set_player(1)
        

    def get_score(self):
        self.blackScore = 0
        self.whiteScore = 0

        for row in self.matrix:
            for tile in row:
                if tile.get_player == 1:
                    self.whiteScore += 1
                elif tile.get_player == 2:
                    self.blackScore += 1
        
        self.tileScore = [self.whiteScore, self.blackScore]
        return self.tileScore


    def update_board(self, flipList, player):
        # updates tile
        for pos in flipList:
            self.matrix[pos[0]][pos[1]].player = player
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


    def get_tile(self, posX, posY) -> tile:
        return self.matrix[posY][posX]
