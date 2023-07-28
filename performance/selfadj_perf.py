from __future__ import annotations

from numpy import linalg
from plotting import perf_plotting
from timing import calc_timing

if __name__ == "__main__":
    numpy_stats1 = calc_timing((lambda x: linalg.eigh(x)), range(10, 100, 10), 10000)
    stats_arr = [numpy_stats1]

    perf_plotting(stats_arr, ["numpy.linalg.eigh()"], "TestPlot")
