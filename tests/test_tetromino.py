from src.tetromino import Tetromino


def test_flip():
    t_shape = Tetromino('T')
    t_shape.flip()
    assert t_shape.body == ((0, 1, 0), (1, 1, 1))

    s_shape = Tetromino('S')
    s_shape.flip()
    assert s_shape.body == ((1, 1, 0), (0, 1, 1))

    z_shape = Tetromino('Z')
    z_shape.flip()
    assert z_shape.body == ((0, 1, 1), (1, 1, 0))

    l_shape = Tetromino('L')
    l_shape.flip()
    assert l_shape.body == ((1, 1), (1, 0), (1, 0))

    j_shape = Tetromino('J')
    j_shape.flip()
    assert j_shape.body == ((1, 1), (0, 1), (0, 1))


def test_compute_peaks():
    t_shape = Tetromino('T')
    t_shape.compute_peaks()
    assert t_shape.peaks == (2, 2, 2)

    s_shape = Tetromino('S')
    s_shape.compute_peaks()
    assert s_shape.peaks == (1, 2, 2)

    z_shape = Tetromino('Z')
    z_shape.compute_peaks()
    assert z_shape.peaks == (2, 2, 1)

    l_shape = Tetromino('L')
    l_shape.compute_peaks()
    assert l_shape.peaks == (3, 1)

    j_shape = Tetromino('J')
    j_shape.compute_peaks()
    assert j_shape.peaks == (1, 3)
