class tile:
    # A simple object containing the position
    # and state of itself
    # The state is:
    #   0 if empty
    #   1 if white
    #   2 if black
    def __init__(self, player, posX = 0, posY = 0):
        self.x = posX
        self.y = posY
        self.player = player

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def get_player(self):
        return self.player
    
    def set_posx(self, posX):
        self.x = posX
    
    def set_posy(self, posY):
        self.y = posY
    
    def set_player(self, playerNum):
        self.player = playerNum
