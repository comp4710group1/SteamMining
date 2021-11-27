import requests
import heapq

STEAM_ID = 76561198092171249
API_KEY = '09FEA56EF1B8EDD4A8602AC5AB529C72'

#how many tags to extract from user
STRICTNESS = 10

f = open('../TagScripts/game_tag_list.csv', 'r')
f2 = open('../FPGrowthScripts/dataset/data_test.csv', 'r')

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
    #******* havent tested when dict is smaller than STRICTNESS ********
    return heapq.nlargest(STRICTNESS, tag_dict, key=tag_dict.get)

def generate_recommendations(top_tags):
    recommendation_list = []
    fp_list = []

    for line in f2:
        fp = line.split("'")[1::2]
        fp_list.append(fp)

    for tag in top_tags: #look through users recently played games
        for pattern in fp_list: #look at each pattern in the frequent pattern list
            if str(tag) in pattern: #if the user's game is in a pattern
                for item in pattern: #look through each item in that frequent pattern
                    if item not in recommendation_list and str(item) not in top_tags: #add items that are not already recommended and not in the user's game list
                        recommendation_list.append(item)
    
    return recommendation_list

def prune_recommendations():
    print('placeholder')

if __name__ == "__main__":
    game_list = api_call()
    top_tags = get_tags(game_list)
    print(top_tags)
    print(generate_recommendations(top_tags))
