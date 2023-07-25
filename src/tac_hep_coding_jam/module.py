from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

import tac_hep_coding_jam._core as m


def add(x: int, y: int) -> int:
    """This function is used for adding two integers together."""
    if not isinstance(x, int):
        msg = "x must be an integer"
        raise TypeError(msg)
    if not isinstance(y, int):
        msg = "y must be an integer"
        raise TypeError(msg)

    return m.add(x, y)


def subtract(x: int, y: int) -> int:
    """This function returns the difference of two integer."""
    if not isinstance(x, int):
        msg = "x must be an integer."
        raise TypeError(msg)
    if not isinstance(y, int):
        msg = "y must be an integer."
        raise TypeError(msg)

    return m.subtract(x, y)


def matrix(x: int) -> NDArray[np.float64]:
    """This function returns a square zero array matrix of integer size."""
    if not isinstance(x, int):
        msg = "Matrix must be integer size."
        raise TypeError(msg)
    if x < 0:
        msg = "Matrix must have positive length."
        raise ValueError(msg)

    return m.matrix(x)
