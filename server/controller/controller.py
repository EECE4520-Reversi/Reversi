from typing import Dict, List, Set

from dao.gamedao import GameDao
from dao.userdao import UserDao
from model.enums import GameType, GameState, TileState, Difficulty
from model.user import User
from model.game import Game
from model.ai_model.ai import AI
from model.ai_model.ai_easy import AI_Easy
from model.ai_model.ai_medium import AI_Medium
from model.ai_model.ai_hard import AI_Hard
import hashlib


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
        self.online_players: Dict[str, str] = {}  # TODO: Change from just names?
        for db_game in GameDao().fetch_games():
            game = Game.from_dict(db_game)
            self.games[game.board_id] = game
        
        self.easy_ai = AI_Easy()
        self.medium_ai = AI_Medium()
        self.hard_ai = AI_Hard()

    def new_game(self, size: int, difficult: int, game_type: int, players: List[str]):
        """Creates a new game using the given settings

        Args:
            size (int): Size of the board
            difficult (int): Match difficulty
            game_type (int): Game type
        """
        board_id = str(len(self.games.keys()) + 1)
        self.games[board_id] = Game(
            board_id=board_id,
            size=size,
            search_depth=difficult,
            game_type=game_type,
            players=players,
        )
        GameDao().save_game(self.games[board_id])
        return board_id

    # checks if the given game exists
    def game_exists(self, board_id: str):
        return board_id in self.games

    def players_turn(self, board_id: str, username: str):
        """Verify its player one's turn

        Returns:
            bool: If its player one's turn
        """

        # Its the players turn if its local play, or actually their turn
        game = self.games[board_id]
        return (
            game.game_type == GameType.LOCAL
            or (
                game.game_type == GameType.AI and game.current_turn == GameState.PLAYER1
            )
            or (
                game.game_type == GameType.ONLINE
                and game.players[game.current_turn - 1] == username
            )
        )

    def is_move_valid(self, board_id: str, x: int, y: int):
        game = self.games[board_id]
        return game.logic.board.get_tile(x, y).player == TileState.VIABLE

    def convert_index_to_xy(self, board_id, idx):
        game = self.games[board_id]
        return idx % game.size, idx // game.size

    # sends a Move to the board
    def send_move(self, board_id: str, x: int, y: int) -> List[dict]:
        """Sends move to Game with board_id

        Args:
            board_id (str): id of target game
            x (int): x position of move
            y (int): y position of move
        """
        game = self.games[board_id]
        game.take_turn(x, y)

        # Array of game data. There is a slight delay in between showing each state on the front end
        datas = [self.get_data(board_id)]

        # if the game is a player vs AI game
        if game.game_type == GameType.AI:
            if game.difficulty == Difficulty.EASY:
                self.take_ai_turn(game, self.easy_ai)
            if game.difficulty == Difficulty.MEDIUM:
                self.take_ai_turn(game, self.medium_ai)
            if game.difficulty == Difficulty.HARD:
                self.take_ai_turn(game, self.hard_ai)

            datas.append(self.get_data(board_id))

        GameDao().save_game(game)
        return datas
    
    def take_ai_turn(self, game: Game, ai: AI) -> bool:
        """Calls necessary logic to interpret an AI's move
        Returns:
            bool: True if move was successful. False on error.
        """

        # pass Move to logic for calculating and updating
        nextMove = ai.minimax_decision(game.logic.board)
        # Make the move to switch players
        if nextMove is not None:
            game.make_move(nextMove)

        game.logic.switch_players()

        # Update valid moves for next player
        game.logic.find_valid_moves(True)

        # check if game is over
        if game.game_over():
            # get winner and end turn
            game.winner = game.end_game()
            return False

        # end turn
        return True

    def change_difficulty(self, board_id: str, difficulty: int) -> None:
        self.games[board_id].difficulty = difficulty
        GameDao().save_game(self.games[board_id])

    def get_board(self, board_id: str) -> list[int]:
        """Gets list of tile states from target game board

        Args:
            board_id (str): id of target game

        Returns:
            list[int]: List of target game's tile states
        """
        return self.games[board_id].get_board_data()

    def add_player(self, board_id: str, username: str):
        self.games[board_id].players.append(username)
        GameDao().save_game(self.games[board_id])

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
        # print("Getting game state")
        if self.games[board_id].logic.game_over():
            return GameState.GAMEOVER.value
        else:
            return self.games[board_id].current_turn.value

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
        wint = self.games[board_id].end_game()
        player1 = User.from_dict(UserDao().fetch_specific_user(self.games[board_id].players[0]))
        player2 = User.from_dict(UserDao().fetch_specific_user(self.games[board_id].players[1]))
        score = self.games[board_id].get_score()
        if wint == 1:
            self.games[board_id].calculate_elos(player1, player2, score[0] - score[1])
        elif wint == 2:
            self.games[board_id].calculate_elos(player2, player1, score[1] - score[0])
        return wint


    def get_leaderboard(self):
        return UserDao().fetch_users().sort({ "elo" : -1, "username" : 1})


    # returns an array of the game score in the form of [whiteScore, blackScore]
    def get_score(self, board_id: str) -> List[int]:
        """Returns the current score of the target game

        Args:
            board_id (str): id of target game

        Returns:
            list[int]: [whitescore, blackscore]
        """
        # print(self.games[board_id].get_score())
        return self.games[board_id].get_score()

    def reset_game(self, board_id: str) -> None:
        """Resets the target game state

        Args:
            board_id (str): id of target game
        """
        self.games[board_id].reset()
        GameDao().save_game(self.games[board_id])

    def get_data(self, board_id: str):
        """Return all getter results in dictionary

        Args:
            board_id (str): id of the target game

        Returns:
            dict: key:value holding all critical game information
        """

        game = self.games[board_id]

        return {
            "id": board_id,
            "board": self.get_board(board_id),
            "score": self.get_score(board_id),
            "state": self.get_state(board_id),
            "winner": self.get_winner(board_id),
            "size": game.size,
            "difficulty": game.difficulty,
            "type": game.game_type,
            "players": game.players,
            "currentTurn": game.players[game.current_turn - 1] if len(game.players) > game.current_turn - 1 else None
        }

    def register_user(self, sid: str, username: str, password: str):
        self.online_players[sid] = username
        return (
            UserDao()
            .save_user(User(username, hashlib.sha256(password.encode()).hexdigest()))
            .to_dict()
        )

    def login_user(self, sid: str, username: str, password: str):
        existingUser = User.from_dict(UserDao().fetch_specific_user(username))
        if existingUser.password == hashlib.sha256(password.encode()).hexdigest():
            self.online_players[sid] = username
            return existingUser.to_dict()

    def user_exists(self, username):
        return UserDao().fetch_specific_user(username)

    def joinable_games(self):
        return [
            {"id": board_id, "player": game.players[0], "size": game.size}
            for board_id, game in self.games.items()
            if len(game.players) == 1 and game.game_type == GameType.ONLINE
        ]
