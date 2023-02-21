class Move:
    def __init__(self, posx: int, posy: int) -> None:
        self.data = (posx, posy)

    def get_col(self):
        return self.data[0]

    def get_row(self):
        return self.data[1]
