class Tile:
    # A simple object containing the position
    # and state of itself
    # The state is:
    #   0 if empty
    #   1 if white
    #   2 if black
    #   3 is a viable Move
    def __init__(self, player: int = 0, pos_x: int = 0, pos_y: int = 0):
        self.x = pos_x
        self.y = pos_y
        self.player = player

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def get_player(self):
        return self.player

    def set_posx(self, pos_x):
        self.x = pos_x

    def set_posy(self, pos_y):
        self.y = pos_y

    def set_player(self, player_num):
        self.player = player_num
