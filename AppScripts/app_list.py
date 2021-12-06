import csv
import os

f = open('../CSVFiles/game_list.csv', 'r', errors="ignore")
#Read lines to get rid of headers
f.readline()
line = f.readline()
f2 = open('../CSVFiles/game_id_lookup.csv', 'w', newline='')
writer = csv.writer(f2)

output = {}
#Go through game_list.csv file
while line:
    split = line.split(",")
    #Checking if the read line is valid
    if(len(split) > 2 and len(split[0]) == 17):
        appID = split[1]
        name = split[2]
        #If the appID not already exists in the dictionary
        if(appID not in output):
            #Writing data row to the CSV file
            output[appID] = [appID, name]
    line = f.readline()

for key,value in output.items():

    data = value
    writer.writerow(data)
