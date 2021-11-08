import csv
import os

f = open('./game_list.csv', 'r')
csvreader = csv.reader(f)
next(csvreader)
f2 = open('./game_list_parsed.csv', 'w', newline='')
writer = csv.writer(f2)

output = {}
#Go through game_list.csv file
for row in csvreader:
    steamID = row[0]
    appID = row[1]
    apps=[]
    apps.append(appID)
    #If the steamID already exists in the dictionary
    if(steamID in output):
        output[steamID].append(appID)
        #TODO games exist already due to duplicate public IDs
    # #Add new steamID to the dictionary
    else:
        output[steamID] = apps


for key,value in output.items():

    data = value
    writer.writerow(data)
