"""
=============
Scatter Demo2
=============

Demo of scatter plot with varying marker colors and sizes.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from pandas import read_csv
from pandas import DataFrame
from pandas import concat

import sys, getopt
import zipfile
from fitparse import FitFile
from datetime import datetime
from datetime import timedelta
import statistics as st


filename = '4003285187.fit'
zipfilename = '4396421076'

zf = zipfile.ZipFile(zipfilename + '.zip')
filename = zf.extract(zipfilename + '.fit')
#filename = '4339768833.fit'
#filename = '4108081447.fit' # marathon Berlin
##filename='4323999883.fit'
fitfile = FitFile(filename)
i=0
data_x = []
data_y0 = []
data_y1 = []
for record in fitfile.get_messages('record'):
    i = i + 1
     # Go through all the data entries in this record
    j = 0    
    for record_data in record:
            # Print the records name and value (and units if it has any)
        if record_data.name == "currHeartRate":
            data_y1.append(record_data.value)
        
        if record_data.name == "heart_rate" :
            data_y0.append(record_data.value)
        if record_data.name =="timestamp":
            data_x.append(record_data.value)
            if i==1:
                startDate=record_data.value


data_rr = np.array([], float)
dd = startDate

data_x2 = []
data_y2 = []
data_y3 = []
for hrv in fitfile.get_messages("hrv"):
    i = i+1
    for data in hrv:
            for rr in data.value:
                if (rr):
                    data_x2.append( dd)
                    data_y2.append(60/rr) 
                    data_rr = np.append(data_rr, rr)
                    dd =dd + timedelta(0,rr)
                    print (dd)

# Marker size in units of points^2
#volume = (15 * data_rr.volume[:-2] / data_rr.volume[0])**2
#close = 0.003 * data_rr.close[:-2] / 0.003 * data_rr.open[:-2]



plt.plot(data_x2, data_y2)
plt.plot(data_x, data_y0)


plt.show()
'''
fig, ax = plt.subplots()
ax.scatter(data_x2, data_y2)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title(filename)
lim = 0.2
#plt.xlim(-lim,lim)
#plt.ylim(-lim,lim)

ax.grid(True)
fig.tight_layout()

'''