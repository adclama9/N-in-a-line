import unittest
from unittest.mock import patch

from ConnectNGame.src.game import Game
from ConnectNGame.test.print_capturer import PrintCapturer


class Test_Game(unittest.TestCase):
    def test_human_names(self):
        user_input = ['h', 'human']
        player_input = ['Raze', '&', 'Cypher', 'T']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            with patch('ConnectNGame.src.players.human_player.input', side_effect=player_input):
                test_game = Game(7, 6, '#', 4, None)
                self.assertEqual(test_game.player_1.name, 'Raze')
                self.assertEqual(test_game.player_1.piece, '&')
                self.assertEqual(test_game.player_1.num, 1)
                self.assertEqual(test_game.player_2.name, 'Cypher')
                self.assertEqual(test_game.player_2.piece, 'T')
                self.assertEqual(test_game.player_2.num, 2)
                self.assertEqual(test_game.seed, None)

    def test_simple_ai(self):
        user_input = ['s', 's']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            test_game = Game(3, 3, '#', 3, 1337)
            test_game.start_game()
            self.assertEqual(test_game.player_1.name,'SimpleAi 1')
            self.assertEqual(test_game.player_1.piece, 'p')
            self.assertEqual(test_game.player_1.num, 1)
            self.assertEqual(test_game.player_2.name, 'SimpleAi 2')
            self.assertEqual(test_game.player_2.piece, 'e')
            self.assertEqual(test_game.player_2.num, 2)

    def test_random_ai(self):
        user_input = ['r', 'r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            test_game = Game(3, 3, '#', 3, 1337)
            test_game.start_game()
            self.assertEqual(test_game.player_1.name,'RandomAi 1')
            self.assertEqual(test_game.player_1.piece, 'p')
            self.assertEqual(test_game.player_1.num, 1)
            self.assertEqual(test_game.player_2.name, 'RandomAi 2')
            self.assertEqual(test_game.player_2.piece, 'e')
            self.assertEqual(test_game.player_2.num, 2)

    def test_type_inputs(self):
        user_input = ['r', 'r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            test_game = Game(3, 3, '#', 3, 1337)
            self.assertEqual(test_game.see_if_simple('imp'),False)
            self.assertEqual(test_game.see_if_simple('smple'), False)
            self.assertEqual(test_game.see_if_simple('si'), True)
            self.assertEqual(test_game.see_if_simple('simp'), True)
            self.assertEqual((test_game.see_if_random('r')),True)
            self.assertEqual((test_game.see_if_random('andom')),False)
            self.assertEqual((test_game.see_if_human('uman')), False)
            self.assertEqual((test_game.see_if_human('man')), False)
            self.assertEqual((test_game.see_if_human('h')), True)

    def test_check_col_full(self):
        user_input = ['r','r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            viper = Game(3, 3, '%', 2, 1337)
            self.assertEqual(viper.check_col_full(0), False)
            self.assertEqual(viper.check_col_full(1), False)
            self.assertEqual(viper.check_col_full(2), False)
            viper.board.game_state = [['1', '1', '1'],
                                      ['1', '1', '1'],
                                      ['1', '1', '1']]
            self.assertEqual(viper.check_col_full(0), True)
            self.assertEqual(viper.check_col_full(1), True)
            self.assertEqual(viper.check_col_full(2), True)

    def test_get_empty_list(self):
        user_input = ['r', 'r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            viper = Game(3, 3, '1', 2, 1337)
            self.assertEqual(viper.get_empty_cols(), [0,1,2])
            viper.board.game_state = [['#', '1', '1'],
                                      ['#', '1', '1'],
                                      ['#', '1', '1']]
            self.assertEqual(viper.get_empty_cols(), [1,2])
            viper.board.game_state = [['#', '#', '1'],
                                      ['#', '#', '1'],
                                      ['#', '#', '1']]
            self.assertEqual(viper.get_empty_cols(), [2])
            viper.board.game_state = [['#', '#', '#'],
                                      ['#', '#', '#'],
                                      ['#', '#', '#']]
            self.assertEqual(viper.get_empty_cols(), [])

    def test_enter_piece_to_board(self):
        user_input = ['h', 'human']
        player_input = ['Raze', 'j', 'Cypher', 'f']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            with patch('ConnectNGame.src.players.human_player.input', side_effect=player_input):
                brimstone = Game(3, 3, '1', 2, 1337)
                brimstone.enter_piece_to_board(0, brimstone.player_1)
                self.assertEqual(brimstone.board.game_state, [['1', '1', '1'],
                                                              ['1', '1', '1'],
                                                              ['j', '1', '1']])
                brimstone.enter_piece_to_board(0, brimstone.player_2)
                self.assertEqual(brimstone.board.game_state, [['1', '1', '1'],
                                                              ['f', '1', '1'],
                                                              ['j', '1', '1']])
                brimstone.enter_piece_to_board(0, brimstone.player_2)
                brimstone.enter_piece_to_board(1, brimstone.player_2)
                self.assertEqual(brimstone.board.game_state, [['f', '1', '1'],
                                                              ['f', '1', '1'],
                                                              ['j', 'f', '1']])
                brimstone.enter_piece_to_board(1, brimstone.player_1)
                brimstone.enter_piece_to_board(1, brimstone.player_1)
                brimstone.enter_piece_to_board(2, brimstone.player_1)
                self.assertEqual(brimstone.board.game_state, [['f', 'j', '1'],
                                                              ['f', 'j', '1'],
                                                              ['j', 'f', 'j']])

    def test_horizontal_count(self):
        user_input = ['r', 'r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            valorant = Game(3, 3, 'V', 3, 1337)
            valorant.board.game_state = [['s', 's', 's'],
                                         ['s', 'b', 'b'],
                                         ['b', 's', 'V']]
            self.assertEqual(valorant.check_horizontal(1, 2, 's'), 1)
            self.assertEqual(valorant.check_horizontal(0, 2, 'b'), 1)
            self.assertEqual(valorant.check_horizontal(1, 1, 'b'), 2)
            self.assertEqual(valorant.check_horizontal(0, 2, 'b'), 1)
            self.assertEqual(valorant.check_horizontal(0, 0, 's'), 3)
            self.assertEqual(valorant.check_horizontal(1, 0, 's'), 3)
            self.assertEqual(valorant.check_horizontal(2, 0, 's'), 3)

    def test_vertical_count(self):
        user_input = ['r', 'r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            valorant = Game(3, 3, 'V', 3, 1337)
            valorant.board.game_state = [['s', 's', 'b'],
                                         ['s', 'b', 'b'],
                                         ['b', 's', 'b']]
            self.assertEqual(valorant.check_vertical(0, 0, 's'), 2)
            self.assertEqual(valorant.check_vertical(0, 2, 'b'), 1)
            self.assertEqual(valorant.check_vertical(2, 0, 'b'), 3)
            self.assertEqual(valorant.check_vertical(2, 1, 'b'), 3)
            self.assertEqual(valorant.check_vertical(2, 2, 'b'), 3)

    def test_positive_diagonal(self):
        user_input = ['r', 'r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            valorant = Game(3, 3, 'V', 3, 1337)
            valorant.board.game_state = [['b', 'b', 's'],
                                         ['b', 'b', 's'],
                                         ['s', 's', 's']]
            self.assertEqual(valorant.check_positive_diagonal(0, 2, 's'), 1)
            self.assertEqual(valorant.check_positive_diagonal(0, 1, 'b'), 2)
            self.assertEqual(valorant.check_positive_diagonal(1, 0, 'b'), 2)
            self.assertEqual(valorant.check_positive_diagonal(1, 2, 's'), 2)

    def test_negative_diagonal(self):
        user_input = ['r', 'r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            valorant = Game(3, 3, 'V', 3, 1337)
            valorant.board.game_state = [['b', 's', 's'],
                                         ['b', 'b', 's'],
                                         ['s', 's', 'b']]
            self.assertEqual(valorant.check_negative_diagonal(0, 0, 'b'), 3)
            self.assertEqual(valorant.check_negative_diagonal(1, 1, 'b'), 3)
            self.assertEqual(valorant.check_negative_diagonal(1, 0, 's'), 2)
            self.assertEqual(valorant.check_negative_diagonal(1, 2, 's'), 1)

    def test_tie_check(self):
        user_input = ['r', 'r']
        with patch('ConnectNGame.src.game.input', side_effect=user_input):
            valorant = Game(3, 3, 'V', 3, 1337)
            valorant.board.game_state = [['b', 's', 'V'],
                                         ['b', 'b', 's'],
                                         ['s', 's', 'b']]
            self.assertEqual(valorant.tie_check(), False)
            valorant.board.game_state = [['b', 's', 'b'],
                                         ['b', 'b', 's'],
                                         ['s', 's', 'b']]
            self.assertEqual(valorant.tie_check(), True)
if __name__ == '__main__':
    unittest.main()