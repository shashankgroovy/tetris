import numpy as np

from src.grid import TetrisGrid
from src.tetromino import Tetromino


def test_place_piece():
    grid = TetrisGrid(5, 5)
    q_shape = Tetromino('Q')
    grid.place_piece(q_shape, 1)

    expected_grid = np.asarray([
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ], dtype=int)
    assert grid.grid.shape == expected_grid.shape

    i_shape = Tetromino('I')
    grid.place_piece(i_shape, 0)
    expected_grid_2 = np.asarray([
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ], dtype=int)
    assert grid.grid.shape == expected_grid_2.shape


def test_clear_full_rows():
    grid = TetrisGrid(6, 6)
    shape_q = Tetromino('Q')

    grid.place_piece(shape_q, 0)
    grid.place_piece(shape_q, 2)
    grid.place_piece(shape_q, 4)
    grid.place_piece(shape_q, 2)

    filled_grid = np.asarray([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ], dtype=int)
    assert grid.grid.shape == filled_grid.shape

    grid.clear_full_rows()
    grid.increase_buffer(2)
    cleared_grid = np.asarray([
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ], dtype=int)
    assert grid.grid.shape == cleared_grid.shape


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

    expected_grid = np.asarray([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ], dtype=int)
    assert grid.grid.shape == expected_grid.shape
