import sys

from src import grid, tetromino


def process_input(input_line: str):
    """Constructs a TetrisGrid and processes a line of tetromino pieces"""
    try:
        pieces = input_line.split(",")
        game = grid.TetrisGrid()

        for piece in pieces:
            shape, column = tetromino.Tetromino(piece[0]), int(piece[1:])
            game.place_piece(shape, column)
            game.clear_full_rows()

        # Let's print the max height amongst all columns in the game.
        print(game.get_ceiling_height())
    except KeyError:
        print("Invalid input")


def main():
    try:
        for line in sys.stdin:
            process_input(line.strip())
    except KeyboardInterrupt:
        pass
