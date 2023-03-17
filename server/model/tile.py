class Tile:
    """Object to store the position and state of each game piece

    ...

    Attributes
    ----------
        x: int
            x position of the tile
        y: int
            y position of the tile
        player: int
            player state of the tile

    """

    def __init__(self, player: int = 0, pos_x: int = 0, pos_y: int = 0):
        """Initialize the attributes of this tile

        Args:
            player (int, optional): player state. Defaults to 0.
            pos_x (int, optional): x position (row). Defaults to 0.
            pos_y (int, optional): y position (col). Defaults to 0.
        """
        self.x = pos_x
        self.y = pos_y
        self.player = player
        self.minimax_score = None

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict):
        tile = cls(data.get("player"), data.get("x"), data.get("y"))
        return tile
