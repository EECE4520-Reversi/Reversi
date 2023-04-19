from model.logic import Logic
from model.move import Move
from model.game import Game
import unittest


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game(None, 3)
        self.game2 = Game(None, 4)

    def test_take_turn(self):
        ans = [1, 1, 1, 2, 1, 3, 0, 0, 0]
        self.assertEqual(self.game.take_turn(2, 0), True)
        self.assertEqual(self.game.logic.get_board(), ans)

        ans = [0, 3, 0, 3]
