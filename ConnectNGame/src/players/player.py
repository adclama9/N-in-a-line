import abc
from typing import List


class Player(abc.ABC):
    taken_pieces = ['darktillwefeltlikehome']
    taken_names = ['verytemporarynameplsdonttakethis']

    def __init__(self, num: int, blank_char: str) -> None:
        """
        Gets the player number and takes blank char to add it to taken pieces
        then gets each player to get their name and piece
        :param num:
        :type num:
        :param blank_char:
        :type blank_char:
        """
        self.num = num
        self.taken_pieces.append(blank_char)
        self.get_name_and_piece(num)
        ...

    @abc.abstractmethod
    def get_name_and_piece(self, num: int) -> None:
        """
        Gets the name and piece from the player or AI
        :return: none
        :rtype: none
        """
        ...

    @abc.abstractmethod
    def get_move(self, empty_list: List) -> int:
        """
        Gets the move from the player or AI
        :return: the eligible column that the player or AI picks
        :rtype: int
        """
        ...
