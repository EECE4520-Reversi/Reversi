from model.logic import Logic
from model.move import Move


class Game:
    """Interface object between controller and model

    ...

    Attributes
    ----------
    logic : Logic
        the logic instance associated with this game
    running : bool
        indicates whether this game has ended
    winner : int
        the winner determined at the end of the game


    Methods
    -------
    take_turn():
        Calls necessary logic to interpret a player's move
    game_over(move):
        Checks if the game is still running
    make_move(move):
        Passes move to logic to be verified and placed
    get_board_data(update_board_flag):
        Gets list of current tile states from board
    get_score():
        Gets current score of game
    end_game():
        Returns winner of game and saves final game data
    """

    def __init__(self, size: int = 8) -> None:
        """Initialize logic, board, and players

        Args:
            size (int, optional): Size of the game board. Defaults to 8.
        """
        # initialize logic, board, and players
        self.logic = Logic(size)
        self.running = True
        self.winner = 0
        self.size = size

    def take_turn(self, x: int, y: int) -> bool:
        """Calls necessary logic to interpret a player's move

        Args:
            x (int): x-position of given move
            y (int): y-position of given move

        Returns:
            bool: True if move was successful. False on error.
        """

        # display most current board (with valid moves highlighted)
        currentBoard = self.get_board_data()

        # get most recent score
        score = self.get_score()

        # pass Move to logic for calculating and updating
        nextMove = Move(x, y)
        self.make_move(nextMove)

        # Update valid moves for next player
        self.logic.find_valid_moves(True)

        # check if game is over
        if self.game_over():
            # get winner and end turn
            self.winner = self.end_game
            return False

        # end turn
        return True

    def game_over(self) -> bool:
        """Checks if the game is still running

        Returns:
            bool: True if the game is over, otherwise False
        """
        if self.logic.game_over():
            return True
        else:
            return False

    def make_move(self, move: Move) -> bool:
        """Passes move to logic to be verified and placed

        Args:
            move (Move): The move received from controller

        Returns:
            bool: True if move was successful. False on error.
        """
        # pass Move to board for updating
        return self.logic.calculate_move(move)

    def get_board_data(self) -> list[int]:
        """Gets list of current state tiles from board

        Returns:
            list[int]: List of current state tiles
        """
        # Returns flat array of size*size length containing tile states
        return self.logic.get_board()

    def get_score(self) -> list[int]:
        """Gets current score of game

        Returns:
            list: contains each player's score on the current board
        """
        return self.logic.board.get_score()

    def end_game(self) -> int:
        """Returns winner of game and saves final game data

        Returns:
            int: player who won
                0 if tie
                1 if white
                2 if black
        """
        # return winner
        #   # 1 if White
        #   # 2 if Black
        #   # 0 if tie
        score = self.get_score()
        if score[0] > score[1]:
            return 1
        elif score[0] < score[1]:
            return 2
        else:
            return 0
