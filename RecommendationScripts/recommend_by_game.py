import requests
import re

from appid_to_name import translate

#steam id to recommend for
STEAM_ID = 76561198067451956
#you should never put your api key out in public but whatever
API_KEY = '203D1B12FF0FE7CD49A5AA30BE98C45'

f = open('../FPGrowthScripts/dataset/data_games.csv', 'r')

print("List of Recommended Games:")

def api_call():
    game_list = []

    try: 
        response = requests.get('https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={}&steamid={}&format=json'.format(API_KEY,STEAM_ID))
    except BaseException as e:
        print(str(e))
    
    if response.status_code == 200:
        data = response.json()
        if data['response'] != {} and data['response']['game_count'] > 0:
            for game in data['response']['games']:
                try:
                    game_list.append(game['appid'])
                except BaseException as e:
                    print(str(e))

    else:
        print(response.status_code)

    return game_list

def gen_recommendations(game_list):
    recommendation_list = []
    fp_list = []

    for line in f:
        fp = re.findall(r'\d+', line)
        fp.pop()
        fp_list.append(fp)

    for game in game_list: #look through users recently played games
        for pattern in fp_list: #look at each pattern in the frequent pattern list
            if str(game) in pattern: #if the user's game is in a pattern
                for item in pattern: #look through each item in that frequent pattern
                    if item not in recommendation_list and int(item) not in game_list: #add items that are not already recommended and not in the user's game list
                        recommendation_list.append(item)
                        
    return recommendation_list
                
if __name__ == "__main__":
    game_list = api_call()
    final_list = gen_recommendations(game_list)
    for item in translate(final_list):
        print(item.strip("\""))

