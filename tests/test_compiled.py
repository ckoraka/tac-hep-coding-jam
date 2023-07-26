from __future__ import annotations

import numpy as np
import pytest

import tac_hep_coding_jam.module as m
import tac_hep_coding_jam.real_matrices as rm

# import tac_hep_coding_jam.real_matrices as rm

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
    # adddd
    assert m.add(2, 3) == 5
    assert m.add(-10, 9) == -1
    assert m.add(0, 0) == 0
    assert m.add(-100, -100) == -200

    # with pytest.raises(TypeError):
    #     m.add(1.5, 0.5)


def test_subtract():
    # Subtractt
    assert m.subtract(7, 5) == 2
    assert m.subtract(-4, 5) == -9
    assert m.subtract(5, -4) == 9
    assert m.subtract(-100, 100) == -200
    assert m.subtract(5, 5) == 0


def test_matrix():
    # little matrix
    assert m.matrix(3) == pytest.approx(np.zeros((3, 3)))

    # zero matrix
    arr = m.matrix(0)
    assert len(arr.shape) == 2
    for s in arr.shape:
        assert s == 0

    # big matrix
    n = 500
    assert m.matrix(n) == pytest.approx(np.zeros((n, n)))

    # do not allow matricies with non-integer size (duh)
    # with pytest.raises(TypeError):
    #     m.matrix(1.5)


<<<<<<< Updated upstream
def test_eigenvalues():
    rm.eigenvectors(np.array([[5, 3], [3, 1]]))
=======
def test_eigenvectors():
    test_matrix = np.array([[5, 1], [3, 1]])
    vecs = rm.eigenvectors(test_matrix)
    assert vecs.shape == (2, 2)

>>>>>>> Stashed changes
    return
