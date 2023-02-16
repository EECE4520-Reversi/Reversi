class move():

    def __init__(self, posx, posy, player) -> None:
        self.data = (posx, posy, player)

    def get_col(self):
        return self.data(0)
    
    def get_row(self):
        return self.data(1)
