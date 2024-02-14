from src.grid import TetrisGrid
from src.tetromino import Tetromino


def test_place_piece():
    grid = TetrisGrid(5, 5)
    q_shape = Tetromino('Q')
    grid.place_piece(q_shape, 1)

    expected_grid = [
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert grid.grid == expected_grid

    i_shape = Tetromino('I')
    grid.place_piece(i_shape, 0)
    expected_grid_2 = [
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert grid.grid == expected_grid_2


def test_clear_full_rows():
    grid = TetrisGrid(6, 6)
    shape_q = Tetromino('Q')

    grid.place_piece(shape_q, 0)
    grid.place_piece(shape_q, 2)
    grid.place_piece(shape_q, 4)
    grid.place_piece(shape_q, 2)

    filled_grid = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    assert grid.grid == filled_grid

    grid.clear_full_rows()
    cleared_grid = [
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert grid.grid == cleared_grid


def test_get_ceiling_height():
    grid = TetrisGrid(5, 5)
    q_shape = Tetromino('Q')

    # Add the first piece
    grid.place_piece(q_shape, 1)
    assert grid.get_ceiling_height() == 2

    # Add another piece
    grid.place_piece(q_shape, 2)
    assert grid.get_ceiling_height() == 4


def test_increase_buffer():
    grid = TetrisGrid(5, 5)
    grid.increase_buffer(2)

    expected_grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert grid.grid == expected_grid
