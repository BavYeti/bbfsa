import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from context import bbfsa

#read csv file
spectra = pd.read_csv('./tests/workflow/input/700cow.csv', delimiter=',', names= ['wn', 'ab'])



# cristallinity index
s = bbfsa.slice(spectra,700,400) #slice for baseline
b = bbfsa.baseline(s) #baseline 
s2 = bbfsa.slice(b,620,530) #slice for peak picking
pp = bbfsa.peakpickMin (s2) #needs test if 2 values
pn = bbfsa.peakpickMin (s2) #needs test if 1 value

#nearest peak
NV = pp['ab'].where (pp['a'].abs(500)==min(pp['a'].abs(500)))

print (NV)
   

plotmeX = s2.wn
plotmeY = s2.ab

plt.plot(plotmeX, plotmeY)
plt.plot(pp.wn, pp.ab,'ro')
plt.xlim(max(plotmeX)+100, min(plotmeX)-100)
plt.ylim(min(plotmeY), max(plotmeY)+0.1)

#plt.show()
