from .player import Player
from typing import List


class HumanPlayer(Player):

    def get_name_and_piece(self, num: int) -> None:
        while True:
            player_name = input(f'HumanPlayer {num} enter your name: ')
            player_name = player_name.strip()

            if player_name == "":
                print("Your name cannot be the empty string or whitespace.")
                continue
            elif num == 2 and player_name.lower() == self.taken_names[0].lower():
                print(f"You cannot use {player_name} for your name as someone else is already using it.")

            else:
                player_piece = input(f"HumanPlayer {num} enter your piece: ")
                player_piece = player_piece.strip()

                if player_piece == "":
                    print('Your piece cannot be the empty string or whitespace.')
                    continue
                elif len(player_piece) > 1:
                    print(f'{player_piece} is not a single character. Your piece can only be a single character.')
                    continue
                elif player_piece == self.taken_pieces[1]:
                    print('Your piece cannot be the same as the blank character.')
                    continue
                elif num == 2 and player_piece.lower() == self.taken_pieces[0].lower():
                    print(f'You cannot use {player_piece} for your piece as {self.taken_names[1]} is already using it.')
                    continue
                else:
                    self.name = player_name
                    self.piece = player_piece
                    self.taken_names.append(player_name)
                    self.taken_pieces.append(player_piece)
                    break

    def get_move(self, empty_list: List) -> int:
        while True:
            column_play = input(f'{self.name}, please enter the column you want to play in: ')
            try:
                column_play = int(column_play)
                if column_play > empty_list[-1] or column_play < 0:
                    print(
                        f'Your column needs to be between 0 and {empty_list[-1]} but is actually {column_play}.')
                    continue
                elif column_play not in empty_list:
                    print(f'You cannot play in {column_play} because it is full.')
                    continue
                else:
                    break
            except ValueError:
                print(f'{self.name}, column needs to be an integer. {column_play} is not an integer. ')
                continue
        return column_play
