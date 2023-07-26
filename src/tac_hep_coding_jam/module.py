from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

# pylint: disable-next=no-name-in-module
import tac_hep_coding_jam._core as m


def add(_x: int, _y: int) -> int:
    """This function is used for adding two integers together."""
    assert isinstance(_x, int), "Arguments must be integers."
    assert isinstance(_y, int), "Arguments must be integers."

    return m.add(_x, _y)


def subtract(_x: int, _y: int) -> int:
    """This function returns the difference of two integer. This will take argument 1, and subtract argument 2 from it."""
    assert isinstance(_x, int), "Arguments must be integers."
    assert isinstance(_y, int), "Arguments must be integers."

    return m.subtract(_x, _y)


def matrix(_x: int) -> NDArray[np.float64]:
    """This function returns a square zero array matrix of integer size."""
    assert isinstance(_x, int), "Matrix must have integer size"
    if _x < 0:
        msg = "Matrix must have positive length."
        raise ValueError(msg)

    return m.matrix(_x)
