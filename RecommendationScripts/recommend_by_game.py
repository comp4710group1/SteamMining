import requests

#steam id to recommend for
STEAM_ID = 76561198092171249
#you should never put your api key out in public but whatever
API_KEY = '09FEA56EF1B8EDD4A8602AC5AB529C72'


def api_call():
    try: 
        response = requests.get('https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key={}&steamid={}&format=json'.format(API_KEY,STEAM_ID))
    except BaseException as e:
        print(str(e))
    
    if response.status_code == 200:
        data = response.json()
        if data['response'] != {} and data['response']['total_count'] > 0:
            for game in data['response']['games']:
                try:
                    print(game["name"])
                except BaseException as e:
                    print(str(e))

    else:
        print(response.status_code)

if __name__ == "__main__":
    api_call()

