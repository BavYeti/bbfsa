import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sparse
import pandas as pd
import peakutils as peak
from scipy.sparse.linalg import spsolve

#read csv file
spectra = pd.read_csv('ftir_data.txt', delim_whitespace=True, names= ['wn', 'ab'])

#basline Correction
#based on Eilers and Boelens 2005: Baseline Correction with Asymmetric Least Squares
#python code by Sparrowcide from here: http://stackoverflow.com/questions/29156532/python-baseline-correction-library
#

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

# cuts a slice out of the Spectra ranging from max to min
def wnSlice (spectra, maxWN, minWN, label='wn'):
    
    z = spectra.query(str(minWN) + '<='+label+'<=' + str(maxWN))
    return z

#Cristallinity Index based on Thomp
def CIndex (spectra)

crindex =wnSlice(spectra, 2000, 1500).reset_index()
#crindex = spectra.query('1500 <= wn <= 2000').reset_index()
#x= np.clip (wn, 2000, 3000)
baseline_ab = baseline_als(crindex.ab)

ab_c = crindex.ab - baseline_ab
abcc = ab_c.values

indexes = peak.indexes (abcc, thres=0.02/max(abcc), min_dist=100)
print (indexes)
print (ab_c[indexes])

plt.plot(crindex.wn, ab_c)

plt.plot(crindex.wn[indexes], ab_c[indexes], 'ro')

plt.xlim(2000, 1500)
plt.ylim(0, 1.0)

plt.show()