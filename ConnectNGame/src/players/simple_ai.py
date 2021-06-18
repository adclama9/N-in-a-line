import random
from typing import Optional, List, Union
from ConnectNGame.src.players.player import Player


class SimpleAI(Player):
    def __init__(self, num: int, board: "Board", win_count: int, seed: Optional[Union[None, int]]) -> None:
        self.board = board
        self.current_position: List = []
        random.seed(seed)
        self.win_count = win_count
        super().__init__(num, self.board.blank_space)

    def get_name_and_piece(self, num: int) -> None:
        self.name = 'SimpleAi ' + str(self.num)
        visible_characters = [chr(i) for i in range(ord('!'), ord('~') + 1)]

        while True:
            piece = random.choice(visible_characters)
            if piece in self.taken_pieces:
                continue
            else:
                self.piece = piece
                self.taken_pieces.append(self.piece)
                break

    def get_move(self, empty_list: List) -> int:
        if self.piece == self.taken_pieces[2]:
            enemy_piece = self.taken_pieces[4]
        else:
            enemy_piece = self.taken_pieces[2]

        for i in empty_list:
            if self.test_if_win(i, self.piece):
                choice = i
                break
            elif self.test_if_win(i, enemy_piece):
                choice = i
                break
            else:
                continue
        else:
            return random.choice(empty_list)

        return choice

    def test_if_win(self, column_play: int, piece: str) -> bool:
        count = -1
        for i in range(0, len(self.board.game_state)):
            if self.board.game_state[i][column_play] == self.board.blank_space:
                count += 1
            else:
                break
        self.board.game_state[count][column_play] = piece
        self.current_position = [column_play, count, piece]
        if self.run_all_win_check():
            self.board.game_state[count][column_play] = self.board.blank_space
            return True
        else:
            self.board.game_state[count][column_play] = self.board.blank_space
            return False

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
