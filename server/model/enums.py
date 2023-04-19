from enum import IntEnum


class GameState(IntEnum):
    PLAYER1 = 1
    PLAYER2 = 2
    GAMEOVER = 3


class TileState(IntEnum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2
    VIABLE = 3


class GameType(IntEnum):
    LOCAL = 1
    AI = 2
    ONLINE = 3


class Difficulty(IntEnum):
    EASY = 0
    MEDIUM = 1
    HARD = 2
