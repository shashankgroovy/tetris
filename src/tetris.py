import sys

from src import grid, tetromino


def process_input(input_line: str):
    """Constructs a TetrisGrid and processes a line of tetromino pieces"""
    pieces = input_line.split(",")
    game = grid.TetrisGrid()

    for piece in pieces:
        shape, column = tetromino.Tetromino(piece[0]), int(piece[1:])
        game.place_piece(shape, column)
        game.clear_full_rows()

    # Let's print the max height amongst all columns in the game.
    game.print_ceiling_height()


def main():
    for line in sys.stdin:
        process_input(line.strip())


if __name__ == "__main__":
    main()
