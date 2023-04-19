from model.board import Board
from model.tile import Tile
import unittest


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board4x4 = Board(4)
        self.board4x4.initialize_board()

    def test_flat_board(self):
        x = self.board4x4.flat_board
        ans = [0, 0, 0, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0]
        self.assertEqual(x, ans)

    def test_get_score(self):
        self.assertEqual(self.board4x4.get_score(), [2, 2])

        flip_list = [Tile(1, 1, 2)]
        self.board4x4.update_board(flip_list, 1)
        self.assertEqual(self.board4x4.get_score(), [3, 1])

        flip_list = [Tile(1, 1, 2), Tile(1, 2, 2)]
        self.board4x4.update_board(flip_list, 2)
        self.assertEqual(self.board4x4.get_score(), [1, 3])

    def test_update_board(self):
        ans = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        flip_list = [Tile(1, 1, 2), Tile(1, 2, 1)]
        self.board4x4.update_board(flip_list, 1)
        self.assertEqual(self.board4x4.flat_board, ans)

    def test_get_winner(self):
        self.assertEqual(self.board4x4.get_winner(), 0)

        flip_list = [Tile(1, 1, 2)]
        self.board4x4.update_board(flip_list, 1)
        self.assertEqual(self.board4x4.get_winner(), 1)

        flip_list = [Tile(1, 1, 2), Tile(1, 2, 2)]
        self.board4x4.update_board(flip_list, 2)
        self.assertEqual(self.board4x4.get_winner(), 2)

    def test_get_tile(self):
        self.assertEqual(self.board4x4.get_tile(1, 1), self.board4x4.matrix[1][1])
        self.assertEqual(self.board4x4.get_tile(1, 2), self.board4x4.matrix[2][1])
        self.assertEqual(self.board4x4.get_tile(1, 3), self.board4x4.matrix[3][1])
