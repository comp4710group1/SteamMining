import csv

f = open('../CSVFiles/game_list.csv', 'r', errors="ignore")
#Read lines to get rid of headers
f.readline()
line = f.readline()
f2 = open('../CSVFiles/game_list_parsed.csv', 'w', newline='')
writer = csv.writer(f2)

output = {}
#Go through game_list.csv file
while line:
    split = line.split(",")
    #Checking if the read line is valid
    if(len(split) > 1):
        steamID = split[0]
        appID = split[1]
        apps=[]
        apps.append(appID)
        #If the steamID already exists in the dictionary
        if(steamID in output):
            if(appID not in output[steamID]):
                output[steamID].append(appID)

        # #Add new steamID to the dictionary
        else:
            output[steamID] = apps
    line = f.readline()

for key,value in output.items():

    data = value
    writer.writerow(data)
