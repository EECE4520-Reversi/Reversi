class tile:
    # A simple object containing the position
    # and state of itself
    # The state is:
    #   0 if empty
    #   1 if white
    #   2 if black
    def __init__(self, posX = 0, posY = 0, playerNum = 0):
        self.x = posX
        self.y = posY
        self.player = playerNum

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getPlayer(self):
        return self.player
    
    def set_posx(self, posX):
        self.x = posX
    
    def set_posy(self, posY):
        self.y = posY
    
    def set_player(self, playerNum):
        self.player = playerNum
