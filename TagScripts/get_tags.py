#https://steamspy.com/api.php

import requests
import csv
import time

f = open('../CSVFiles/game_id_lookup.csv', 'r', errors="ignore")
line = f.readline()

f2 = open('../CSVFiles/game_tag_list.csv', 'w', newline='')
writer = csv.writer(f2)

while line:
    row = line.split(",")
    appID = row[0]
    #grab app info for every game in app_list
    response = requests.get('https://steamspy.com/api.php?request=appdetails&appid={}'.format(appID))

    if(response.status_code == 200):
        app_info = response.json()

        #this api call also lets us skip over the appid to name phase and gives the name directly
        tags = app_info['tags']
        data = [appID]
        print("AppID " + appID)
        for key in tags:
            data.append(key)
        #Writing data row to the CSV file
        writer.writerow(data)

    else:
        print('Something goofed up with the request: {}'.format(response.status_code))
    time.sleep(0.3)
    line = f.readline()
