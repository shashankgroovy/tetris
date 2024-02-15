import numpy as np
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

    def __init__(self, rows: int = 10, columns: int = 10):
        """Initializes a grid with default size of 20 rows and 10 columns"""
        self.grid = np.zeros((rows, columns), dtype=int)
        self.grid_height = rows
        self.grid_width = columns
        self.peaks = [0] * columns

    def _place(self, piece: tetromino.Tetromino, x_pos: int, y_pos: int) -> None:
        """Places a Tetromino on the grid"""

        self.grid[
            y_pos : y_pos + len(piece.body), x_pos : x_pos + len(piece.body[0])
        ] += np.array(piece.body)

    def _update_peaks(self, piece: tetromino.Tetromino, x_pos: int, y_pos: int) -> None:
        """Updates max heights of each column based on a tetromino's peaks"""
        for index, peak in enumerate(piece.peaks):
            current_height = y_pos + peak
            self.peaks[x_pos + index] = max(self.peaks[x_pos + index], current_height)

    def increase_buffer(self, buffer: int = 1) -> None:
        """Increases the grid buffer by size (default=1)"""
        new_rows = np.zeros((buffer, self.grid_width), dtype=self.grid.dtype)
        self.grid = np.vstack([self.grid, new_rows])

    def check_collision(
        self, piece: tetromino.Tetromino, x_pos: int, y_pos: int
    ) -> bool:
        """Returns True if a Tetromino can be placed at given place in grid"""

        collision_matrix = self.grid[
            y_pos : y_pos + len(piece.body), x_pos : x_pos + len(piece.body[0])
        ]
        return bool(np.any(np.logical_and(piece.body, collision_matrix)))

    def clear_full_rows(self) -> None:
        """Clears all the filled rows from the grid and repositions the
        remaining rows accordingly"""
        rows_to_clear = np.all(self.grid == 1, axis=1)
        self.grid = self.grid[~rows_to_clear]

        # Recompute heights
        if np.sum(rows_to_clear) > 0:
            self.peaks = [h - np.sum(rows_to_clear) for h in self.peaks]

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
            y_pos += 1
            # Check if we have run out of space
            if y_pos >= self.grid_height or y_pos + 1 >= self.grid_height:
                # Double the buffer size
                self.increase_buffer(self.grid_height * 2)

        self._place(piece, x_pos, y_pos)
        self._update_peaks(piece, x_pos, y_pos)

    def get_ceiling_height(self):
        """Returns the max ceiling height of grid"""
        self.clear_full_rows()
        return max(self.peaks)
