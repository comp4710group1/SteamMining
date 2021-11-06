#76561198092171249 # my steam id
#API key = 09FEA56EF1B8EDD4A8602AC5AB529C72 remove this later/get a new one

import requests

#request game info from user specified in steamid
response = requests.get('https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=09FEA56EF1B8EDD4A8602AC5AB529C72&steamid=76561198092171249&format=json')
#list of mapping all appid's to actual game names
applist = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')

if(response.status_code == 200):
    data = response.json()
    games = applist.json()

   #grab game info for steam user
    for game in data['response']['games']:
        name = game["appid"]
        time = game["playtime_forever"] / 60
        actual_name = "name"

        #convert appid to actual name
        for titles in games['applist']['apps']:
            if(int(name) == int(titles['appid'])):
                actual_name = titles['name'] 


        print('Game: {}, Time played: {} hours'.format(actual_name, time))
else:
    print(response.status_code)

    
