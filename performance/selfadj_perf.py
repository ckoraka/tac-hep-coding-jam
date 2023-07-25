import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import timeit
#from timeit import timeit, repeat

def eighbench_mark(inMat):
	evecs, evals = linalg.eigh(sig2)


if __name__ == "__main__":
	#print(timeit.repeat(timer=t,repeat = 1000000, number = 1))
	sig2 = np.array([[0,-1j],[1j,0]])
	timeArr = timeit.repeat(lambda: eighbench_mark(sig2),repeat=1000000,number=1)
	#plt.plot(timeArr,'*')
	#plt.savefig("TestPlot.png")
	#print(timeit.timeit(lambda: eighbench_mark(), globals=globals()))
