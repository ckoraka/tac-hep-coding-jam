import scipy.linalg
import numpy as np
import timeit

#takes in a function and a list of matrix sizes N (for NxN matrices) and tests performance for each matrix
def timing(func, sizes):
    stats = np.zeros((len(sizes), 3)) #N, mean execution time, std execution time

    for i, n in enumerate(sizes):
        matrix = np.random.rand(n, n)
        sym_pos_def = 0.5*(matrix + matrix.T) + n*np.identity(n) #ensure matrix is symmetric positive definite
        time = timeit.repeat(lambda: func(sym_pos_def), repeat=10000, number=1)
        stats[i] = [n, np.mean(time), np.std(time)]

    return stats

cholesky_performance = timing(lambda x: scipy.linalg.cholesky(x, lower=True), range(10,100,10))
