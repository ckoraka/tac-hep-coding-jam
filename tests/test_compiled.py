from __future__ import annotations

import numpy as np
import pytest

import tac_hep_coding_jam._core as m

"""
Type mappings for C++/Python
- MatrixType (MatrixXd) | NDArray[np.float64] 
- int | int
- GeneralizedSelfAdjointEigenSolver<MatrixType<N>> | some python class with the following functions:
    - .eigenvalues() -> float vector of length <N>
    - .eigenvectors() -> float matrix of shape <N x N>

Functions that will exist:
- eigenvalues
- eigenvectors
"""

def test_add():
    assert m.add(2, 3) == 5
    assert m.add(-10, 9) == -1
    assert m.add(0, 0) == 0
    assert m.add(-100, -100) == -200
    try:
        m.add(1.5, .5) 
        assert False, "Function m.add should take only integer inputs"
    except Exception as e:
        assert isinstance(e, TypeError)

def test_subtract():
    assert m.subtract(7, 5) == 2
    assert m.subtract(-4, 5) == -9 
    assert m.subtract(5, -4) == 9 
    assert m.subtract(-100, 100) == -200 
    assert m.subtract (5,5) == 0

def test_matrix():
    assert m.matrix(3) == pytest.approx(np.zeros((3, 3)))
    arr = m.matrix(0)
    assert len(arr.shape) == 2
    for s in arr.shape:
        assert s == 0

    n = 500
    assert m.matrix(n) == pytest.approx(np.zeros((n, n))) 

    try:
        m.matrix(1.5)
        assert False, "Function m.matrix should take only integer inputs"
    except Exception as e:
        assert isinstance(e, TypeError)
