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
        minimax_score: int
            minimax score of the tile

    Methods
    ----------
        getX():
            Gets x position of this tile
        getY():
            Gets y position of this tile
        get_player():
            Gets player state of this tile
        set_posx(pos_x:int):
            Sets the x position of this tile
        set_posy(pos_y:int):
            Sets the y position of this tile
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

    def getX(self) -> int:
        """Gets x position of this tile

        Returns:
            int: x position of this tile
        """
        return self.x

    def getY(self) -> int:
        """Gets y position of this tile

        Returns:
            int: y position of this tile
        """
        return self.y

    def get_player(self) -> int:
        """Gets player state of this tile

        Returns:
            int: player state
                0 = empty
                1 = white
                2 = black
                3 = viable move
        """
        return self.player

    def set_posx(self, pos_x) -> None:
        """Sets x position of this tile

        Args:
            pos_x (int): x position to assign this tile
        """
        self.x = pos_x

    def set_posy(self, pos_y) -> None:
        """Sets y position of this tile

        Args:
            pos_y (int): y position to assign this tile
        """
        self.y = pos_y

    def set_player(self, player_num) -> None:
        """Sets player state of this tile

        Args:
            player_num (int): State to assign this tile
        """
        self.player = player_num


