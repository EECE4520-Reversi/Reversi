from typing import List, Dict

from model.game import Game


class GameController:
    """Interface object for Model, View, and Database

    ...

    Methods
    --------
    send_move(board_id: str, x:int, y:int):
        Sends move to Game with board_id
    get_board(board_id: str):
        Gets list of tile states from target game board
    get_state(board_id: str):
        Returns whose turn it is on the target game
    get_winner(board_id: str):
        Returns the winner of the target game
    get_score(board_id: str):
        Returns the current score of the target game
    reset_game(board_id: str):
        Resets the target game state
    get_data(board_id: str):
        Return all getter results in dictionary
    """

    def __init__(self) -> None:
        self.games: Dict[str, Game] = {}

    def new_game(self, size: int, difficult: int):
        """Creates a new game using the given settings

        Args:
            size (int): Size of the board
            difficult (int): Match difficulty
        """
        board_id = str(len(self.games.keys()))
        self.games[board_id] = Game(size=size, search_depth=difficult)
        print(
            f"Created New Game (id: {board_id}, size: {size}, difficulty: {difficult})"
        )
        return self.get_data(board_id)

    # checks if the given game exists
    def game_exists(self, board_id: str):
        return board_id in self.games

    # sends a Move to the board
    def send_move(self, board_id: str, x: int, y: int) -> None:
        """Sends move to Game with board_id

        Args:
            board_id (str): id of target game
            x (int): x position of move
            y (int): y position of move
        """
        self.games[board_id].take_turn(x, y)

        # if the game is a player vs AI game
        if self.games[board_id].game_type == 2 and self.games[board_id].logic.current_player == 2:
            self.games[board_id].take_ai_turn()


    def change_difficulty(self, board_id: str, difficulty: int) -> None:
        self.games[board_id].difficulty = difficulty

    def get_board(self, board_id: str) -> list[int]:
        """Gets list of tile states from target game board

        Args:
            board_id (str): id of target game

        Returns:
            list[int]: List of target game's tile states
        """
        return self.games[board_id].get_board_data()

    def get_state(self, board_id: str) -> int:
        """Returns whose turn it is on the target game

        Args:
            board_id (str): id of target game

        Returns:
            int: Playder value of target game
                1: Player 1's turn (black)
                2: Player 2's turn (white)
                3: Game over
        """
        print("Getting game state")
        if self.games[board_id].logic.game_over():
            return 3
        else:
            return self.games[board_id].logic.current_player

    def get_winner(self, board_id: str) -> int:
        """Returns the winner of the target game

        Args:
            board_id (str): id of target game

        Returns:
            int: Player with higher score
                0: tie
                1: white
                2: black
        """
        return self.games[board_id].end_game()

    # returns an array of the game score in the form of [whiteScore, blackScore]
    def get_score(self, board_id: str) -> List[int]:
        """Returns the current score of the target game

        Args:
            board_id (str): id of target game

        Returns:
            list[int]: [whitescore, blackscore]
        """
        print(self.games[board_id].get_score())
        return self.games[board_id].get_score()

    def reset_game(self, board_id: str) -> None:
        """Resets the target game state

        Args:
            board_id (str): id of target game
        """
        self.games[board_id] = Game(self.games[board_id].size)

    def get_data(self, board_id: str):
        """Return all getter results in dictionary

        Args:
            board_id (str): id of the target game

        Returns:
            dict: key:value holding all critical game information
        """
        return {
            "id": board_id,
            "board": self.get_board(board_id),
            "score": self.get_score(board_id),
            "state": self.get_state(board_id),
            "winner": self.get_winner(board_id),
            "size": self.games[board_id].size,
        }
