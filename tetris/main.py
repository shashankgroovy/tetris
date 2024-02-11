import sys


class TetrisGrid:
    def __init__(self):
        # Declare a default grid with size 20 rows, 10 columns
        self.grid = [[0] * 10 for _ in range(20)]
        # An array to track max height of each column
        self.heights = [0] * 10

        # A dict of available shapes
        self.shapes = {
            'Q': [[1, 1], [1, 1]],
            'Z': [[1, 1, 0], [0, 1, 1]],
            'S': [[0, 1, 1], [1, 1, 0]],
            'T': [[1, 1, 1], [0, 1, 0]],
            'I': [[1, 1, 1, 1]],
            'L': [[1, 0], [1, 0], [1, 1]],
            'J': [[0, 1], [0, 1], [1, 1]]
        }

    def place_piece(self, piece, column):
        method = getattr(self, f'_place_{piece}')
        method(self.shapes[piece], column)

    def _place_Q(self, shape, column):
        """Places the Q shape block on the grid"""

        # Find max height of the concerned column and column+1
        max_height = max(self.heights[column], self.heights[column + 1])

        for row_index, pair in enumerate(shape):
            # Update heights for each column
            self.heights[column + row_index] = max_height + 2
            for col_index, tile in enumerate(pair):
                # Place piece on grid
                self.grid[max_height + row_index][column + col_index] = tile

    def _place_Z(self, shape, column):
        """Places the Z shape block on the grid"""

        # Find max height of the concerned columns
        max_height = max(
            self.heights[column],
            self.heights[column + 1],
            self.heights[column + 2]
        )

        for row_index, pair in enumerate(shape):
            for col_index, tile in enumerate(pair):
                # Place piece on grid
                self.grid[max_height + row_index][column + col_index] = tile
                # Update heights for each column
                self.heights[column + row_index] = max_height + col_index

    def _place_S(self, shape, column):
        ...

    def _place_T(self, shape, column):
        ...

    def _place_I(self, shape, column):
        ...

    def _place_L(self, shape, column):
        ...

    def _place_J(self, shape, column):
        ...

    def clear_full_rows(self):
        new_grid = []
        for row in self.grid:
            if 0 in row:
                new_grid.append(row)
        num_empty_rows = 20 - len(new_grid)
        self.grid = [[0] * 10 for _ in range(num_empty_rows)] + new_grid

    def print_heights(self):
        self.clear_full_rows()
        print(max(self.heights))


def process_input(input_line):
    pieces = input_line.split(',')
    grid = TetrisGrid()
    for piece in pieces:
        letter, column = piece[0], int(piece[1:])
        grid.place_piece(letter, column)
    grid.print_heights()


def main():
    for line in sys.stdin:
        process_input(line.strip())


if __name__ == "__main__":
    main()
