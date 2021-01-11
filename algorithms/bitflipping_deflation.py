"""
This script estimates multiple Lp-norm (p <= 1) Principal-Components of a matrix
"""
__author__ = 'Dimitris G. Chachlakis'
__email__ = 'dimitris@mail.rit.edu'
__affiliation__ = 'Rochester Institute of Technology'
import numpy as np
from utils import *
from algorithms import bitflipping
def bitflipping_deflation(X, p, K):
    """
    Input: 
    --  --  -- -
    X: data matrix of size D-by-N: N D-dimensional measurements
    p: Lp-norm parameter, p should be less than or equal to 1
    K: number of componets to be extracted by deflation
    Output:
    --  --  -- -
    Qest: multiple Lp-norm (p <= 1) Principal-Component estimates
    Bsest: estimate of the optimal antipodal binary matrix
    """
    D = X.shape[0]
    Qest = np.zeros((D, K))
    Qest[:, 0] = bitflipping(X, p)[0]
    for k in range(K-1):
        P = np.eye(D)-Qest@Qest.T
        Qest[:, k+1] = bitflipping(P@X, p)[0]
    Best = np.sign(X.T@Qest)
    return Qest, Best