from ConnectNGame.src.board import Board
from typing import List, Optional, Union
from ConnectNGame.src.players.human_player import HumanPlayer  # type: ignore
from ConnectNGame.src.players.random_ai import RandomAI  # type: ignore
from ConnectNGame.src.players.simple_ai import SimpleAI  # type: ignore
from ConnectNGame.src.players.player import Player  # type: ignore


class Game(object):

    def __init__(self, board_col: int, board_row: int, blank_char: str, win_count: int,
                 seed: Optional[Union[None, int]]) -> None:
        self.win_count = win_count
        self.board = Board(board_row, board_col, blank_char, "defaultinput")
        self.current_position: List = []
        self.empty_cols_list: List = []
        self.seed = seed

        self.create_players()

    def create_players(self) -> None:
        while True:
            player_1_type = self.generate_player_from_type(1)
            if player_1_type == 1:
                self.player_1 = SimpleAI(1, self.board, self.win_count, self.seed)
                break
            elif player_1_type == 2:
                self.player_1 = RandomAI(1, self.board.blank_space, self.seed)
                break
            elif player_1_type == 3:
                self.player_1 = HumanPlayer(1, self.board.blank_space)
                self.player_1.taken_names[0] = self.player_1.taken_names[1]
                self.player_1.taken_pieces[0] = self.player_1.taken_pieces[2]
                break
            else:
                print(f'{player_1_type.lower()} is not one of Human or Random or Simple. Please try again.')
                continue

        while True:
            player_2_type = self.generate_player_from_type(2)
            if player_2_type == 1:
                self.player_2 = SimpleAI(2, self.board, self.win_count, self.seed)
                break
            elif player_2_type == 2:
                self.player_2 = RandomAI(2, self.board.blank_space, self.seed)
                break
            elif player_2_type == 3:
                self.player_2 = HumanPlayer(2, self.board.blank_space)
                break
            else:
                print(f'{player_2_type} is not one of Human or Random or Simple. Please try again.')
                continue

    def generate_player_from_type(self, num: int) -> int:
        type = input(f'Choose the type for Player {num}\nEnter Human or Random or Simple: ')
        if self.see_if_simple(type):
            return 1
        elif self.see_if_random(type):
            return 2
        elif self.see_if_human(type):
            return 3
        else:
            return type

    @staticmethod
    def see_if_simple(type_input: str) -> bool:
        simple_list = ['s', 'si', 'sim', 'simp', 'simpl', 'simple']
        for letter in simple_list:
            if letter == type_input.lower().strip():
                return True
        return False

    @staticmethod
    def see_if_random(type_input: str) -> bool:
        random_list = ['r', 'ra', 'ran', 'rand', 'rando', 'random']
        for letter in random_list:
            if letter == type_input.lower().strip():
                return True
        return False

    @staticmethod
    def see_if_human(type_input: str) -> bool:
        human_list = ['h', 'hu', 'hum', 'huma', 'human']
        for letter in human_list:
            if letter == type_input.lower().strip():
                return True
        return False

    def start_game(self) -> None:
        print(self.board)
        while True:
            self.enter_piece_to_board(self.player_1.get_move(self.get_empty_cols()), self.player_1)
            print(self.board)
            if self.run_all_win_check():
                self.player_win(self.player_1)
                break
            if self.tie_check():
                print('Tie Game.')
                break

            self.enter_piece_to_board(self.player_2.get_move(self.get_empty_cols()), self.player_2)
            print(self.board)
            if self.run_all_win_check():
                self.player_win(self.player_2)
                break
            if self.tie_check():
                print('Tie Game.')
                break

    def check_col_full(self, column: int) -> bool:
        count = 0
        for i in range(0, len(self.board.game_state)):
            if self.board.game_state[i][column] == self.board.blank_space:
                count += 1
            else:
                continue
        if count > 0:
            return False
        else:
            return True

    def get_empty_cols(self) -> List:
        self.empty_cols_list = []
        for i in range(self.board.num_cols):
            is_full = self.check_col_full(i)
            if not is_full:
                self.empty_cols_list.append(i)
        return self.empty_cols_list

    def enter_piece_to_board(self, column_play: int, player: "Player") -> None:
        count = -1
        for i in range(0, len(self.board.game_state)):
            if self.board.game_state[i][column_play] == self.board.blank_space:
                count += 1
            else:
                break
        self.board.game_state[count][column_play] = player.piece
        self.current_position = [column_play, count, player.piece]

    def run_all_win_check(self) -> bool:
        x = int(self.current_position[0])
        y = int(self.current_position[1])
        player_char = self.current_position[2]
        if self.check_horizontal(
                x, y, player_char) >= self.win_count or self.check_vertical(
            x, y, player_char) >= self.win_count or self.check_negative_diagonal(
            x, y, player_char) >= self.win_count or self.check_positive_diagonal(
            x, y, player_char) >= self.win_count:
            return True
        else:
            return False

    def check_horizontal(self, x: int, y: int, player_char: str) -> int:
        """
        :return: count
        :rtype: int
        """
        count = 0
        check_left = x
        check_right = x + 1
        while check_left >= 0:
            if self.board.game_state[y][check_left] == player_char:
                count += 1
                check_left -= 1
            else:
                break

        while check_right < len(self.board.game_state[0]):
            if self.board.game_state[y][check_right] == player_char:
                count += 1
                check_right += 1
            else:
                break

        return count

    def check_vertical(self, x: int, y: int, player_char: str) -> int:
        count = 0
        check_up = y
        check_down = y + 1
        while check_up >= 0:
            if self.board.game_state[check_up][x] == player_char:
                count += 1
                check_up -= 1
            else:
                break

        while check_down < len(self.board.game_state):
            if self.board.game_state[check_down][x] == player_char:
                count += 1
                check_down += 1
            else:
                break
        return count

    def check_positive_diagonal(self, x: int, y: int, player_char: str) -> int:
        """
        Checks if there are diagonal win conditions in the positive direction /
        from the newly inserted position
        consists of adding up+right and down+left
        :return: count
        :rtype: int
        """
        count = 0
        check_up = y
        check_right = x
        check_down = y + 1
        check_left = x - 1

        while check_up >= 0 and check_right < len(self.board.game_state[0]):
            if self.board.game_state[check_up][check_right] == player_char:
                count += 1
                check_up -= 1
                check_right += 1
            else:
                break

        while check_down < len(self.board.game_state) and check_left >= 0:
            if self.board.game_state[check_down][check_left] == player_char:
                count += 1
                check_down += 1
                check_left -= 1
            else:
                break
        return count

    def check_negative_diagonal(self, x: int, y: int, player_char: str) -> int:
        """
        Checks if there are diagonal win conditions in the negative direction \
        so adding up+left and down+right
        :return:
        :rtype:
        """
        count = 0
        check_down = y
        check_right = x
        check_up = y - 1
        check_left = x - 1

        while check_down < len(self.board.game_state) and check_right < len(self.board.game_state[0]):
            if self.board.game_state[check_down][check_right] == player_char:
                count += 1
                check_down += 1
                check_right += 1
            else:
                break
        while check_up >= 0 and check_left >= 0:
            if self.board.game_state[check_up][check_left] == player_char:
                count += 1
                check_up -= 1
                check_left -= 1
            else:
                break
        return count

    def tie_check(self) -> bool:
        count = 0
        for i in range(len(self.board.game_state)):
            for j in range(len(self.board.game_state[0])):
                if self.board.game_state[i][j] == self.board.blank_space:
                    count += 1

        if count > 0:
            return False
        else:
            return True

    @staticmethod
    def player_win(player: Player) -> None:
        return print(f'{player.name} won the game!')
