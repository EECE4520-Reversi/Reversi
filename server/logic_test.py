from model.logic import Logic
from model.move import Move
import unittest

class TestLogic(unittest.TestCase):
    def setUp(self) -> None:
        self.logic = Logic(4)
        self.logic2 = Logic(2)
        self.logic3 = Logic(3)

    def test_game_over(self):
        self.assertEqual(self.logic.game_over(), False)
        self.assertEqual(self.logic2.game_over(), True)

        self.logic3.board.matrix[0][2].player = 1
        self.logic3.board.matrix[2][0].player = 1
        self.assertEqual(self.logic3.game_over(), False)

    def test_switch_players(self):
        self.assertEqual(self.logic.current_player, 1)
        
        self.logic.switch_players()
        self.assertEqual(self.logic.current_player, 2)

        self.logic.switch_players()
        self.assertEqual(self.logic.current_player, 1)

    def test_validate_move(self):
        x = self.logic.validate_move(Move(0,2), 1)
        self.assertEqual(x, [self.logic.board.get_tile(1,2)])

        x = self.logic.validate_move(Move(0,0), 1)
        self.assertEqual(x, [])

        x = self.logic.validate_move(Move(1,0), 2)
        self.assertEqual(x, [self.logic.board.get_tile(1,1)])

    def test_find_valid_moves(self):
        self.assertEqual(self.logic2.find_valid_moves(True), [])

        self.assertEqual(self.logic.board.matrix[0][2].player, 3)
        self.assertEqual(self.logic.board.matrix[1][3].player, 3)
        self.assertEqual(self.logic.board.matrix[2][0].player, 3)
        self.assertEqual(self.logic.board.matrix[3][1].player, 3)

        self.logic.find_valid_moves(True, 2)
        self.assertEqual(self.logic.board.matrix[0][1].player, 3)
        self.assertEqual(self.logic.board.matrix[1][0].player, 3)
        self.assertEqual(self.logic.board.matrix[2][3].player, 3)
        self.assertEqual(self.logic.board.matrix[3][2].player, 3)

    def test_calculate_move(self):
        self.assertEqual(self.logic.calculate_move(Move(0,0)), False)
        self.assertEqual(self.logic.calculate_move(Move(1,1)), False)
        self.assertEqual(self.logic.calculate_move(Move(1,2)), False)
        self.assertEqual(self.logic.calculate_move(Move(0,2)), True)

    



        


