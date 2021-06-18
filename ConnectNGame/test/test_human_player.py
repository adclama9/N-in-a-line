import unittest
from ConnectNGame.src.players.human_player import HumanPlayer
import unittest
from unittest.mock import patch


class test_human_player(unittest.TestCase):
    def test_get_human_name_piece(self):
        user_input = ["Bob", "B"]
        with patch('ConnectNGame.src.players.human_player.input', side_effect=user_input):
            new_player = HumanPlayer(1, "%")
            new_player.get_name_and_piece(1)
            self.assertEqual(new_player.name,'Bob')
            self.assertEqual(new_player.piece, "B")
    def test_get_human_move(self):
        user_input = [2]
        empty_list = [0,1,2]
        with patch('ConnectNGame.src.players.human_player.input', side_effect=user_input):
            new_player = HumanPlayer(1,"%")
            column_play = new_player.get_move(empty_list)
            self.assertEqual(2, column_play)



if __name__ == '__main__':
    unittest.main()
