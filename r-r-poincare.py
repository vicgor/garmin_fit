"""
=============
Scatter Demo2
=============

Demo of scatter plot with varying marker colors and sizes.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import sys, getopt
from fitparse import FitFile
from datetime import datetime
from datetime import timedelta
import statistics as st

#filename = '4003285187.fit'
filename = '4339768833.fit'
filename = '4108081447.fit' # marathon Berlin
##filename='4323999883.fit'
fitfile = FitFile(filename)

data_rr = []
i=0
for hrv in fitfile.get_messages("hrv"):
    i = i+1
    for data in hrv:
            for rr in data.value:
                if (rr):
                    print (rr)
                    data_rr.append(rr)

delta1 = np.diff(data_rr) / data_rr[:-1]

# Marker size in units of points^2
#volume = (15 * data_rr.volume[:-2] / data_rr.volume[0])**2
#close = 0.003 * data_rr.close[:-2] / 0.003 * data_rr.open[:-2]



fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:])

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title(filename)
lim = 0.2
plt.xlim(-lim,lim)
plt.ylim(-lim,lim)

ax.grid(True)
fig.tight_layout()

plt.show()
