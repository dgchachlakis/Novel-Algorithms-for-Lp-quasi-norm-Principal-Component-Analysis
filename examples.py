import numpy as np
import algorithms as lppca
import matplotlib.pyplot as plt
import imagesc as imagesc
# =========Example 1: illustration of Algorithm 1
D = 10
N = 15
p = 1/2
X = np.random.randn(D, N)
qest, best, metest, metric_evolution = lppca.bitflipping(X, p)
plt.plot(range(len(metric_evolution)), metric_evolution)
plt.ylabel('Lp-PCA metric')
plt.xlabel('Iteration index')
plt.show()
# =========Example 2: illustration of Algorithm 2
D = 8
N = 10
K = 3
p = 1/2
X = np.random.randn(D, N)
Qest, Best = lppca.bitflipping_deflation(X, p, K)
fig = imagesc.seaborn(Qest.T@Qest)
