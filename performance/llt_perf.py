from __future__ import annotations

import scipy
from plotting import perf_plotting
from timing import calc_timing

if __name__ == "__main__":
    numpy_stats1 = calc_timing(
        (lambda x: scipy.linalg.cholesky(x, lower=True)), range(10, 100, 10), 10000
    )
    stats_arr = [numpy_stats1]

    perf_plotting(stats_arr, ["scipy.linalg.cholesky()"], "TestPlot")
