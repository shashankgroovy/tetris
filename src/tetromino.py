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
        "Q": ((1, 1), (1, 1)),
        "Z": ((1, 1, 0), (0, 1, 1)),
        "S": ((0, 1, 1), (1, 1, 0)),
        "T": ((1, 1, 1), (0, 1, 0)),
        "I": ((1, 1, 1, 1),),
        "L": ((1, 0), (1, 0), (1, 1)),
        "J": ((0, 1), (0, 1), (1, 1)),
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
                    peaks[col] = height - row

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
