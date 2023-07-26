from __future__ import annotations

import timeit

import numpy as np
import scipy.linalg


# takes in a function and a list of matrix sizes N (for NxN matrices) and tests performance for each matrix
def timing(func, sizes):
    stats = np.zeros((len(sizes), 3))  # N, mean execution time, std execution time
    rand_gen = np.random.default_rng(seed=42)

    for i, n in enumerate(sizes):
        matrix = rand_gen.random([n, n])
        sym_pos_def = 0.5 * (matrix + matrix.T) + n * np.identity(
            n
        )  # ensure matrix is symmetric positive definite
        time = timeit.repeat(lambda x=sym_pos_def: func(x), repeat=10000, number=1)
        stats[i] = [n, np.mean(time), np.std(time)]

    return stats


cholesky_performance = timing(
    (lambda x: scipy.linalg.cholesky(x, lower=True)), range(10, 100, 10)
)
