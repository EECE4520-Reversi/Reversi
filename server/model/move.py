class Move:
    """Object to hold and return move data

    ...

    Attributes
    ----------
        data: tuple
            holds the position data of the move

    Methods
    ----------
        get_col():
            Gets x position of given move
        get_row():
            Gets y position of given move
    """

    def __init__(self, posx: int, posy: int) -> None:
        """Initializes attributes from provided data

        Args:
            posx (int): x position of provided move
            posy (int): y position of provided move
        """
        self.data = (posx, posy)

    @property
    def col(self) -> int:
        """Gets x position of this move

        Returns:
            int: x position of this move
        """
        return self.data[0]

    @property
    def row(self) -> int:
        """Gets y position of this move

        Returns:
            int: y position of this move
        """
        return self.data[1]

    def __eq__(self, other: "Move"):
        return self.data == other.data
