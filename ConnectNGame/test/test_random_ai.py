import unittest
from ConnectNGame.src.players.random_ai import RandomAI
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def test_get_piece(self):
        with patch('random.choice', side_effect=['X']):
            my_RandomAI = RandomAI(1, "%", None)
            self.assertEqual('X', my_RandomAI.piece)

    def test_get_move(self):
        with patch('random.choice', side_effect=[0]):
            my_random_ai = RandomAI(1, "%", None)
            my_list = [0, 1, 2]
            result = my_random_ai.get_move(my_list)
            self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
