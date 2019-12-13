import sys, getopt
from fitparse import FitFile

if len(sys.argv)<2:
    print ("Missing file name")
    exit()
filename = sys.argv[1]
fitfile = FitFile(filename)
print (filename)

    # Get all data messages that are of type record
i = 0    
fo = open(filename + ".hr.csv", "w+")
for record in fitfile.get_messages('record'):
    i = i + 1
    #print i
        # Go through all the data entries in this record
    j = 0    
    s = ""
    s = s + str(i) + ","
    for record_data in record:
        j = j + 1
        #s = s + str(j) + ","
        #print j
            # Print the records name and value (and units if it has any)
        if record_data.name == "currHeartRate":
            s = s + str(record_data.value) + ","
        
        if record_data.name == "heart_rate" :
            s = s + str(record_data.value) + ","
        if record_data.name =="timestamp":
            s = s + '"' + str(record_data.value) + "\","
    fo.write(s + "\n")
    print(s)
fo.close()

fo = open(filename + ".hrv.csv", "w+")
for hrv in fitfile.get_messages("hrv"):
    i = i+1
    for data in hrv:
            #print (data)
            for rr in data.value:
                if (rr): 
                    print(rr)
                    fo.write(str(rr) + "\n")
fo.close()


