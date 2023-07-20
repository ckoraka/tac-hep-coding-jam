from __future__ import annotations

import numpy as np
import pytest

import tac_hep_coding_jam._core as m


def test_add():
    assert m.add(2, 3) == 5


def test_subtract():
    assert m.subtract(7, 5) == 2


def test_matrix():
    assert m.matrix(3) == pytest.approx(np.zeros((3, 3)))
