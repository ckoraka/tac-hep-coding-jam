from __future__ import annotations

import timeit

import numpy as np
from numpy import linalg as LA
import plotting


# takes in a function and a list of matrix sizes N (for NxN matrices) and tests performance for each matrix
def calc_timing(func, sizes):
    stats = np.zeros((len(sizes), 3))  # N, mean execution time, std execution time
    rng = np.random.default_rng()

    for i, n in enumerate(sizes):
        matrix = rng.random(size=(n, n))
        sym_pos_def = 0.5 * (matrix + matrix.T) + n * np.identity(n)  # ensure matrix is symmetric positive definite
        time = timeit.repeat(lambda sym_pos_def=sym_pos_def: func(sym_pos_def),  repeat=10000,number=1)
        
        stats[i] = [n, np.mean(time), np.std(time)]

    return stats

results = calc_timing(lambda x: LA.eig(x), range(10, 50, 10))


plotting.perf_plotting([results], ["Eigensolver"], "TestPlot")

