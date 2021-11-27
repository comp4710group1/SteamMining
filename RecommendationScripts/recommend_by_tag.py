import requests
import heapq

STEAM_ID = 76561198092171249
API_KEY = '09FEA56EF1B8EDD4A8602AC5AB529C72'

#how many tags to extract from user
STRICTNESS = 10

f = open('../TagScripts/game_tag_list.csv', 'r')

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
                    if(int(game['playtime_forever']) > 600): #at least 10 hours of play time
                        game_list.append(game['appid'])
                except BaseException as e:
                    print(str(e))

    else:
        print(response.status_code)

    return game_list

def get_tags(game_list):
    tag_dict = {}

    for line in f: #for every line in the game to tag file
        tags = line.split(',') #tags[0] will be the appid, the rest will be the tags
        if len(tags) > 1: #make sure the game actually has tags
            if int(tags[0]) in game_list: #check if the appid from file is in this user's game list
                for tag in range(1, len(tags)): #look through all the tags from that game
                    if tags[tag] not in tag_dict: #if the tag isnt in the dict yet, add it
                        tag_dict[tags[tag]] = 1
                    else:                         #otherwise, increment the count by 1
                        tag_dict[tags[tag]] += 1 
    
    #grabs the top 'STRICTNESS' tags from this user. If we used all the tags, any user with like 50
    #games would get recommended basically every game
    print(heapq.nlargest(STRICTNESS, tag_dict, key=tag_dict.get))

if __name__ == "__main__":
    game_list = api_call()
    get_tags(game_list)