from typing import List
class Board:

    def __init__(self, num_rows: int, num_cols: int, blank_space: str, name: str):
        """parameters for dimensions of grid,
         blank space character,
         board name, and initiate 2D list for
          grid: game_state"""
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.blank_space = blank_space
        self.name = name
        self.game_state = [[str(blank_space) for col in range(num_cols)] for row in range(num_rows)]

    def __str__(self) -> str:
        display_grid = ''
        first_char = "  "
        first_line: List[str] = []
        for i in range(0, self.num_cols):
            first_line.append(str(i))
        first_line = first_char + ' '.join(first_line)# type : ignore
        display_grid += f'{first_line}\n'
        for item, row in enumerate(self.game_state):
            join_row = ' '.join(row)
            display_grid += f'{item} {join_row}\n'
        return display_grid

    def __repr__(self) -> str:
        display_grid = ''
        first_char = "  "
        first_line = []

        for i in range(0, self.num_cols):
            first_line.append(str(i))
        first_line = first_char + ' '.join(first_line)  # type : ignore
        display_grid += f'{first_line}\n'
        for item, row in enumerate(self.game_state):
            join_row = ' '.join(row)
            display_grid += f'{item} {join_row}\n'
        return display_grid


