import peakutils
import pandas as pd

from .baseline_als import baseline_als

#returns local maximum(s)
def peakpickMax (spectra,thres=0.02, min_dist=10):
    p = peakutils.indexes (spectra.ab.values, thres=thres, min_dist=min_dist)
    d = {'wn':spectra.wn[p],'ab':spectra.ab[p]}
    z = pd.DataFrame (d)
    return z

#returns local minimum(s)
def peakpickMin (spectra,thres=0.02, min_dist=10):
    n= spectra.ab * -1 # multiplies absorbance with -1, because peak.indexes cannot find local minimum
    p = peakutils.indexes (n, thres=thres, min_dist=min_dist)
    d = {'wn':spectra.wn[p],'ab':spectra.ab[p]}
    z = pd.DataFrame (d)
    return z

#returns a basline corrected spectra
def baseline (spectra):
    spectra['ab']=spectra.ab - baseline_als(spectra.ab)
    return spectra

# returns a sliced spectra ranging from max to min Wavelength (WN)
def slice (spectra, maxWN, minWN, label='wn'):
    z = spectra.query(str(minWN) + '<='+label+'<=' + str(maxWN)).reset_index()
    return z