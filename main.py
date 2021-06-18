import sys
import ConnectNGame.src.game


def main() -> None:
    filename = sys.argv[1]
    mapped = {}
    with open(filename) as fil:
        for line in fil:
            if line == "":
                continue
            else:
                line = str(line)
                key, value = line.split(":")
                key = key.strip()
                value = value.strip()
                mapped[key] = [value]
    num_rows = mapped["num_rows"]
    num_cols = mapped["num_cols"]
    num_pieces_to_win = mapped["num_pieces_to_win"]
    blank_char = mapped["blank_char"]
    try:
        seed = int(sys.argv[2])
    except:
        seed = None

    new_game = ConnectNGame.src.game.Game(int(num_cols[0]), int(num_rows[0]), blank_char[0], int(num_pieces_to_win[0]), seed)
    new_game.start_game()


if __name__ == '__main__':
    main()
