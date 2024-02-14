from src import tetromino


class TetrisGrid:
    """TetrisGrid represents a Tetris gameplay grid.

    Tetrominos can be places on the grid and helper methods like
    `get_ceiling_height` can be used to compute peak from the grid.

    Example:
    >>> grid = TetrisGrid(5,5)
    >>> shape_t = tetromino.Tetromino('T')

    >>> # Let's flip the tetromino and place it
    >>> shape_t.flip()
    >>> grid.place_piece(shape_t, 1)

    >>> print(grid.grid)
    [[0, 0, 1, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

    >>> grid.get_ceiling_height()
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

    def _place(self, piece: tetromino.Tetromino, x_pos: int, y_pos: int) -> None:
        """Places a Tetromino on the grid"""

        for row, pair in enumerate(piece.body):
            for col, tile in enumerate(pair):
                # Check for empty space
                if not tile:
                    continue
                # Place piece on grid
                self.grid[y_pos + row][x_pos + col] = tile

    def _update_peaks(self, piece: tetromino.Tetromino, x_pos: int, y_pos: int) -> None:
        """Updates max heights of each column based on a tetromino's peaks"""
        for index, peak in enumerate(piece.peaks):
            current_height: int = y_pos + peak
            if current_height > self.peaks[x_pos + index]:
                self.peaks[x_pos + index] = current_height

    def increase_buffer(self, buffer: int = 1) -> None:
        """Increases the grid buffer by size (default=1)"""
        self.grid.extend([[0] * self.grid_width] * buffer)

    def check_collision(
        self, piece: tetromino.Tetromino, x_pos: int, y_pos: int
    ) -> bool:
        """Returns True if a Tetromino can be placed at given place in grid"""

        # Iterate over each cell to find the collision point.
        for row in range(len(piece.body)):
            for col in range(len(piece.body[row])):
                # Check for empty space
                if piece.body[row][col] == 0:
                    continue

                # If it collides, return True
                if (
                    y_pos + row >= len(self.grid)
                    or x_pos + col >= len(self.grid[0])
                    or self.grid[y_pos + row][x_pos + col] != 0
                ):
                    return True
        return False

    def clear_full_rows(self) -> None:
        """Clears all the filled rows from the grid and repositions the
        remaining rows accordingly

        Currently, this method scans the entire grid for any filled rows and
        then simultaneously deletes them. This could become expensive once
        grid height becomes infinitely high, since we are assuming
        there will be an infinite stream of falling tetrominos.

        To improve this, we can use a tetromino's body height to compute the
        number of rows each tetromino will effect and only clear those
        rows in O(piece_height) time.
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
        self.peaks = [h - len(rows_to_clear) for h in self.peaks]

    def place_piece(self, piece: tetromino.Tetromino, position: int):
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

    def get_ceiling_height(self):
        """Returns the max ceiling height of grid"""
        self.clear_full_rows()
        return max(self.peaks)
