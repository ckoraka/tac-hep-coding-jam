from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

import tac_hep_coding_jam._core as m


def add(x_1: int, x_2: int) -> int:
    """This function is used for adding two integers together."""
    assert isinstance(x_1, int), "Arguments must be integers."
    assert isinstance(x_2, int), "Arguments must be integers."

    return m.add(x_1, x_2)


def subtract(x_1: int, x_2: int) -> int:
    """This function returns the difference of two integer."""
    assert isinstance(x_1, int), "Arguments must be integers."
    assert isinstance(x_2, int), "Arguments must be integers."

    return m.subtract(x_1, x_2)


def matrix(x_1: int) -> NDArray[np.float64]:
    """This function returns a square zero array matrix of integer size."""
    assert isinstance(x_1, int), "Matrix must have integer size"
    if x_1 < 0:
        msg = "Matrix must have positive length."
        raise ValueError(msg)

    return m.matrix(x_1)
