import requests
import csv
import os
import threading
#
# THIS SCRIPT TAKES IN THE public_ids.csv file and will output a script with the games
#
#


#API Key
apiKey = "09FEA56EF1B8EDD4A8602AC5AB529C72" # probably change this to your own api key before you start running

#Headers for the CSV file
header = ['steamID', 'appID', 'name', 'time']

#Opening file and file writer
f = open('./public_ids.csv', 'r',encoding='utf-8')
for i in range (1690000): #increment by 10000 before running
    next(f)

f2 = open('./game_list.csv', 'a', newline='')
writer = csv.writer(f2)

#Checking if the headers already exist in CSV so we do not append them again.
if os.stat('./game_list.csv').st_size == 0:
    writer.writerow(header)

#Total API calls = API_CALLS_PER_THREAD * NUM_THREADS
API_CALLS_PER_THREAD = 200
NUM_THREADS = 50

def api_call(self):
    #Loop through i next ID's
    for i in range(API_CALLS_PER_THREAD):
        #include_played_free_games=true gets free games, can be removed if we only want to do paid games
        try:
            response = requests.get('https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key={}&steamid={}&format=json'.format(apiKey,self.starting_id))
        except BaseException as e:
            print(str(e))
        if response.status_code == 200:
            data = response.json()
            #If data is not empty
            if data['response'] != {} and data['response']['total_count'] > 0:
                #grab game info for steam user
                for game in data['response']['games']:
                    appID = game["appid"]
                    try:
                        name = game["name"]
                        #Encoding and decoding the name to remove unused ascii characters
                        name = name.encode("ascii", "ignore")
                        name = name.decode()
                        time = '{:.2f}'.format(game["playtime_forever"] / 60)

                        #Checking if the games play time is > 10 hours to eliminate owned but not played games
                        if float(time) > 10:
                            #Formatting data
                            data = [int(self.starting_id), appID, name, time]
                            #Writing data row to the CSV file
                            writer.writerow(data)
                    except BaseException as e:
                        print(str(e))
                        print(self.starting_id)

        else:
            print(response.status_code)
        self.increment()

#Defining thread class
class my_thread (threading.Thread):

    #Initializing a thread with variables
    def __init__(self, threadID, name, starting_id):
        threading.Thread.__init__(self)
        self.threadID = threadID
        #Thread name
        self.name = name
        #For steam ID
        self.starting_id = starting_id

    def run(self):
        print ('Starting ' + self.name)
        #Thread calls api_call
        api_call(self)
        print ('Exiting ' + self.name)

    def increment(self):
        self.starting_id = f.readline().strip()

        while not self.starting_id.isdigit():
            self.starting_id = f.readline().strip()


#Main
if __name__ == "__main__":
    workers = []

    #Making NUM_THREADS worker threads
    for count in range(NUM_THREADS):
        workers.append(my_thread(count, 'thread {}'.format(count), f.readline().strip()))
        
    #Start each worker "run"
    for x in workers:
        x.start()

