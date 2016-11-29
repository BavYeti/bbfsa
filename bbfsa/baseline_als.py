#basline Correction
#based on Eilers and Boelens 2005: Baseline Correction with Asymmetric Least Squares
#python code by Sparrowcide from here: http://stackoverflow.com/questions/29156532/python-baseline-correction-library

import numpy as np
import scipy.sparse as sparse
from scipy.sparse.linalg import spsolve

def baseline_als(y, lam=1000000, p=0.001, niter=10):
     L = len(y)
     D = sparse.csc_matrix(np.diff(np.eye(L), 2))
     w = np.ones(L)
     # range == xrange in phyton > 2.x 
     for i in range(niter):
      W = sparse.spdiags(w, 0, L, L)
      Z = W + lam * D.dot(D.transpose())
      z = spsolve(Z, w*y)
      w = p * (y > z) + (1-p) * (y < z)
     return z