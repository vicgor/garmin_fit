import plotly.graph_objects as go

import sys, getopt
from fitparse import FitFile

filename = '4323999883.fit'
fitfile = FitFile(filename)
#print (filename)

    # Get all data messages that are of type record
i = 0    
fo = open(filename + ".hr.csv", "w+")
data_x = []
data_y0 = []
data_y1 = []
for record in fitfile.get_messages('record'):
    i = i + 1
     # Go through all the data entries in this record
    j = 0    
    s = ""
    
    s = s + str(i) + ","
    for record_data in record:
        
        data_x.append(i)
        j = i + j + 1
            # Print the records name and value (and units if it has any)
        if record_data.name == "currHeartRate":
            s = s + str(record_data.value) + ","
            data_y1.append(record_data.value)
        
        if record_data.name == "heart_rate" :
            s = s + str(record_data.value) + ","
            data_y0.append(record_data.value)
        if record_data.name =="timestamp":
            s = s + '"' + str(record_data.value) + "\","
    fo.write(s + "\n")
fo.close()

fo = open(filename + ".hrv.csv", "w+")
for hrv in fitfile.get_messages("hrv"):
    i = i+1
    for data in hrv:
            for rr in data.value:
                if (rr): 
                    fo.write(str(rr) + "\n")
fo.close()







fig = go.Figure()
fig.add_trace(go.Scatter(x=data_x, y=data_y0,
                    mode='lines',
                    
                    name='hr1'))
fig.add_trace(go.Scatter(x=data_x, y=data_y1,
                    
                    mode='lines',
                    name='hr2'))
#fig.add_trace(go.Scatter(x=data_x, y=data_y2, mode='markers', name='markers'))

fig.show()