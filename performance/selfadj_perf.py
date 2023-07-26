from __future__ import annotations

from numpy import linalg
from plotting import perf_plotting
from timing import calc_timing

if __name__ == "__main__":
    # print(timeit.repeat(timer=t,repeat = 1000000, number = 1))
    # sig2 = np.array([[0,-1j],[1j,0]])
    # time_arr = timeit.repeat(lambda: eighbench_mark(sig2),repeat=1000000,number=1)
    # print(np.mean(time_arr))

    numpy_stats1 = calc_timing((lambda x: linalg.eigh(x)), range(10, 100, 10))
    numpy_stats2 = calc_timing((lambda x: linalg.eigh(x)), range(10, 100, 10))
    stats_arr = [numpy_stats1]

    perf_plotting(stats_arr, ["numpy.linalg.eigh()"], "TestPlot")

# plt.plot(timeArr,'*')
# plt.savefig("TestPlot.png")
# print(timeit.timeit(lambda: eighbench_mark(), globals=globals()))
