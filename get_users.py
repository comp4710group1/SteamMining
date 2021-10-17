import requests
import csv
import os

apiKey = "09FEA56EF1B8EDD4A8602AC5AB529C72"

#Headers for the CSV file
header = ['steamID', 'appID', 'time']

#Opening file and file writer
f = open('./output.csv', 'a', newline='')
writer = csv.writer(f)

#Checking if the headers already exist in CSV so we do not append them again.
if os.stat('./output.csv').st_size == 0:
    writer.writerow(header)

#Starter steamID for increment
#steamID = 92171249
steamID = 92100009

#Loop through i next ID's
for i in range(100):

    response = requests.get('https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid=765611980{}&format=json'.format(apiKey,steamID))

    if response.status_code == 200:
        data = response.json()

        #If data is not empty
        if data['response'] != {} and data['response']['game_count'] > 0:
            #grab game info for steam user
            for game in data['response']['games']:
                appID = game["appid"]
                time = '{:.2f}'.format(game["playtime_forever"] / 60)

                #Checking if the games play time is > 10 hours to eliminate owned but not played games
                if float(time) > 10:
                    #Formatting data
                    data = [steamID, appID, time]
                    #Writing data row to the CSV file
                    writer.writerow(data)
    print(steamID)
    steamID += 1

