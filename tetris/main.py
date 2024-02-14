import sys


class Tetromino:
    """Tetromino represents a geometric shape composed of four squares,
    connected orthogonally.

    Shapes of each tetromino is associated with the alphabet it closely
    represents. The tetromino list are created to be visually similar to the
    shape they represent i.e. the top of the tetromino is at index = 0, and
    bottom of tetromino is at index = N.
    Thus, a Tetromino's bottom row is not zero indexed to keep the orientation
    intact.

     For example:
     Tetromino shape 'T' has the geometric shape as follows:

     │          │
     │   ###    │
     │    #     │
     └──────────┘

    Tetromino shape 'T' represented in a Python list object with the
    orientation intact as follows using binary digits:
        1 = occupied
        0 = empty space

        [
            [1, 1, 1],
            [0, 1, 0]
        ]

    Example:
    >>> piece = Tetromino('T')
    >>> print(piece.body)
        ((1, 1, 1), (0, 1, 0))

    >>> piece.flip()
    >>> print(piece.body)
        ((0, 1, 0), (1, 1, 1))
    """

    # The body is an tuple that denotes a specific shape of a tetromino
    body: tuple[tuple[int, ...], ...]

    # The peaks of a tetromino piece is a tuple where each element of the
    # tuple represents the "highest" non-empty space that appears in
    # the body for each vertical position in the piece.
    peaks: tuple[int, ...]

    # Available geometric shapes
    SHAPES = {
        'Q': ((1, 1), (1, 1)),
        'Z': ((1, 1, 0), (0, 1, 1)),
        'S': ((0, 1, 1), (1, 1, 0)),
        'T': ((1, 1, 1), (0, 1, 0)),
        'I': ((1, 1, 1, 1),),
        'L': ((1, 0), (1, 0), (1, 1)),
        'J': ((0, 1), (0, 1), (1, 1))
    }

    def __init__(self, shape):
        self.body = self.SHAPES[shape]
        self.compute_peaks()

    def compute_peaks(self) -> None:
        """
        Computes the peaks of a tetromino piece.

        Example:
        >>> shape_t = Tetromino('L')
        >>> print(shape_l.body)
        ((1, 0), (1, 0), (1, 1))

        >>> print(shape_l.peaks)
        (3, 1)

        Explanation:
        The hightest non-empty tile for shape_l are as follows:
        - For column 0, highest occupied tile is at row 0
        - For column 1, highest occupied tile is at row 2
        """
        height = len(self.body)
        width = len(self.body[0])
        peaks = [0] * width

        for col in range(width):
            for row in range(len(self.body)):
                if row == 0 and self.body[row][col] == 1:
                    peaks[col] = height
                elif peaks[col] == 0 and self.body[row][col] == 1:
                    peaks[col] = height-row

        # Update the peaks
        self.peaks = tuple(peaks)

    def flip(self) -> None:
        """Flip a tetromino piece horizontally i.e. on x-axis

        Example:
        >>> shape_t = Tetromino('T')
        >>> print(shape_t.body)
        ((1, 1, 1), (0, 1, 0))

        >>> shape_t.flip()
        >>> print(shape_t.body)
        ((1, 0, 1), (0, 1, 0))
        """
        # Flip the tuple by reversing it idiomatically :)
        self.body = self.body[::-1]


class TetrisGrid:
    """TetrisGrid represents a Tetris gameplay grid.

    Tetrominos can be places on the grid and helper methods like
    `print_ceiling_height`.

    Example:
    >>> grid = TetrisGrid(5,5)
    >>> shape_t = Tetromino('T')

    >>> # Let's flip the tetromino and place it
    >>> shape_t.flip()
    >>> grid.place_piece(shape_t, 1)

    >>> print(grid.grid)
    [[0, 0, 1, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

    >>> grid.print_ceiling_height()
    2

    >>> # Let's turn the grid upside-down to see things visually correctly
    >>> grid.grid.reverse()
    >>> print(grid.grid)
    [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 1, 0, 0]]
    """

    # A list representing a Tetris grid or board
    grid: list[list[int]]
    # A list to track max height of each column in grid
    peaks: list[int]

    def __init__(self, rows: int = 20, columns: int = 10):
        """Initializes a grid with default size of 20 rows and 10 columns"""
        self.grid = [[0] * columns for _ in range(rows)]
        self.peaks = [0] * columns

    @property
    def grid_width(self) -> int:
        """Returns grid's total number of columns"""
        return len(self.grid[0])

    def _place(self, piece: Tetromino, x_pos: int, y_pos: int) -> None:
        """Places a Tetromino on the grid"""

        for row, pair in enumerate(piece.body):
            for col, tile in enumerate(pair):
                # Check for empty space
                if not tile:
                    continue
                # Place piece on grid
                self.grid[y_pos + row][x_pos + col] = tile

    def _update_peaks(self, piece: Tetromino, x_pos: int, y_pos: int) -> None:
        """Updates max heights of each column based on a tetromino's peaks"""
        for index, peak in enumerate(piece.peaks):
            current_height: int = y_pos + peak
            if current_height > self.peaks[x_pos + index]:
                self.peaks[x_pos + index] = current_height

    def increase_buffer(self, buffer: int = 1) -> None:
        """Increases the grid buffer by size (default=1)"""
        self.grid.extend([[0] * self.grid_width] * buffer)

    def check_collision(self, piece: Tetromino, x_pos: int, y_pos: int) -> bool:
        """Returns True if a Tetromino can be placed at given place in grid"""

        # Iterate over each cell to find the collision point.
        for row in range(len(piece.body)):
            for col in range(len(piece.body[row])):
                # Check for empty space
                if piece.body[row][col] == 0:
                    continue

                # If it collides, return True
                if (y_pos + row >= len(self.grid) or
                        x_pos + col >= len(self.grid[0]) or
                        self.grid[y_pos + row][x_pos + col] != 0):
                    return True
        return False

    def clear_full_rows(self) -> None:
        """Clears all the filled rows from the grid and repositions the
        remaining rows accordingly

        Currently, this method scans the entire grid for any filled rows and
        the simultaneously deletes them. This could become expensive once
        if grid height becomes infinitely high, since we are assuming
        there will be an infinite stream of falling tetrominos.

        To improve this, we can use a tetromino's body height to compute the
        number of rows each tetromino will effect and only clear those
        rows in O(piece_height) time
        """

        # List to capture rows for clearance
        rows_to_clear = []
        ceiling = max(self.peaks)

        # Find rows without holes
        for row in range(ceiling):
            if 0 not in self.grid[row]:
                # Mark the row for clearance
                rows_to_clear.append(row)

        for to_clear in range(len(rows_to_clear) - 1, -1, -1):
            # Remove the row from the grid
            self.grid.pop(rows_to_clear[to_clear])

        # Increase grid buffer size
        self.increase_buffer(len(rows_to_clear))

        # Recompute heights
        self.peaks = [h-len(rows_to_clear) for h in self.peaks]

    def place_piece(self, piece: Tetromino, position: int):
        """Checks if a piece can be placed on grid and then places it.

        To simulate falling of tetrominos, and based on the problem statement
        we'll consider the row at zero index of the grid as the bottom row,
        which means the whole grid is basically upside down.

        Since Tetromino objects are stored in a way to keep the visual
        orientation intact and the grid is upside down, there are
        two ways to correctly place tetrominos on grid:
        - Flip tetris grid itself, or
        - Flip each tetromino piece on x-axis

        For ease of use, we'll just flip each tetromino :)
        """
        # Flip it!
        piece.flip()

        # Get max height of column at position where tetromino is supposed
        # to be inserted
        max_height = self.peaks[position] - 1

        # Compute the x,y coordinates where the tetromino will be placed.
        x_pos = position
        y_pos = max_height if max_height >= 0 else 0

        # Check if piece can be placed at desired location in the grid
        while self.check_collision(piece, x_pos, y_pos):
            # Increment y_pos
            y_pos += 1

        self._place(piece, x_pos, y_pos)
        self._update_peaks(piece, x_pos, y_pos)

    def print_ceiling_height(self):
        """Returns the max ceiling height of grid"""
        self.clear_full_rows()
        print(max(self.peaks))


def process_input(input_line: str):
    """Constructs a TetrisGrid and processes a line of tetromino pieces"""
    pieces = input_line.split(',')
    grid = TetrisGrid()

    for piece in pieces:
        tetromino, column = Tetromino(piece[0]), int(piece[1:])
        grid.place_piece(tetromino, column)
        grid.clear_full_rows()

    # Let's print the max height amongst all columns in the grid.
    grid.print_ceiling_height()


def main():
    for line in sys.stdin:
        process_input(line.strip())


if __name__ == "__main__":
    main()
