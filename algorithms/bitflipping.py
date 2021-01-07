"""
This script estimates the Lp-norm (p<=1) Principal-Component of a matrix
"""
__author__='Dimitris G. Chachlakis'
__email__='dimitris@mail.rit.edu'
__affiliation__='Rochester Institute of Technology'
import numpy as np
from utils import *
def bitflipping(X, p):
    """
    Input: 
    -------
    X: data matrix of size D-by-N: N D-dimensional measurements
    p: Lp-norm parameter, p should be less than or equal to 1
    Output:
    -------
    qest: an optimal Lp-PC of X
    bsest: an optimal antipodal binary vectror
    metest: the maximum attainable metric
    metric_evolution: the evolution of the metric that is being optimized
    """
    tol=1e-6
    D=X.shape[0]
    N=X.shape[1]
    q=np.random.randn(D,1)
    q=q/np.sqrt(q.T@q)
    best=np.sign(X.T@q).flatten()
    qest,metest=solver_fixedb(X,best,p)
    metric_evolution=[metest]
    I=np.eye(N)
    while True:
        val=np.zeros((N,1))
        for n in range(N):
            bn=best-2*best[n]*I[:,n]
            q,met=solver_fixedb(X,bn,p)
            val[n]=met
        met=np.max(val)
        if met-metest>tol:
            metest=met
            idx=np.argmax(val)
            best=best-2*best[idx]*I[:,idx]
            metric_evolution.append(metest)
        else:
            break
    return qest,best,metest,metric_evolution