import unittest
import sys
#sys.path.insert(0, '/BoardPrinterProject/src)
from ConnectNGame.src.board import Board

class TestBoard(unittest.TestCase):
    def test_initiate_board(self):
        test_board=Board(3,3,'3','3')
        self.assertEqual(test_board.num_rows,3)

    def test_board_filling(self):
        test_board = Board(2, 2, "2", '2')
        self.assertEqual(test_board.game_state,[['2','2'],['2','2']])

    def test_str(self):
        test_board = Board(3, 3, '3', '3')
        self.assertEqual(type(str(test_board)),str)

    def test_repr(self):
        test_board = Board(3, 3, '3', '3')
        self.assertEqual(type(repr(test_board)), str)

if __name__ == '__main__':
    unittest.main()