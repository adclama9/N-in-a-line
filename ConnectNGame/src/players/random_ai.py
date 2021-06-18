import random
from ConnectNGame.src.players.player import Player
from typing import Optional, List, Union


class RandomAI(Player):
    def __init__(self, num: int, blank_space: str, seed: Optional[Union[None, int]]):
        random.seed(seed)
        super().__init__(num, blank_space)

    def get_name_and_piece(self, num: int) -> None:
        self.name = 'RandomAi ' + str(self.num)
        VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
        while True:
            piece = random.choice(VISIBLE_CHARACTERS)
            if piece in self.taken_pieces:
                continue
            else:
                self.piece = piece
                self.taken_pieces.append(self.piece)
                break

    def get_move(self, empty_list: List) -> int:
        return random.choice(empty_list)
