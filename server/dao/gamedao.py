from dao.basedao import BaseDao
from model.game import Game


class GameDao:
    def __init__(self):
        self.collection = "game"

    def save_game(self, game: Game):
        BaseDao().db[self.collection].replace_one(
            {"_id": game.board_id}, game.to_dict(), upsert=True
        )

    def fetch_games(self):
        return BaseDao().db[self.collection].find()
