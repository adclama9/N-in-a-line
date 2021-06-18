import unittest
from unittest.mock import patch

from ConnectNGame.src.players.simple_ai import SimpleAI
from ConnectNGame.src.game import Game
from ConnectNGame.src.board import Board

class MyTestCase(unittest.TestCase):
    def test_get_move(self):
        MyBoard = Board(3,3,"%","Myboard")
        my_simpleAI = SimpleAI(1, MyBoard, 3, None)
        with patch('random.choice', side_effect=[0]):
            my_simpleAI.piece = "z"
            my_simpleAI.taken_pieces = ["x", "w", "z", "d", "e"]
            empty_list = [0,1,2]
            result = my_simpleAI.get_move(empty_list)
            self.assertEqual(0, result)




if __name__ == '__main__':
    unittest.main()
