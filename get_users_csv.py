import requests
import csv
import os
import threading
#
# THIS SCRIPT TAKES IN THE public_ids.csv file and will output a script with the games
#
#


#API Key
apiKey = "C4364E1FFD0AFF0CA0FD74ACBD3ADBFF"

#Headers for the CSV file
header = ['steamID', 'appID', 'time']

#Opening file and file writer
f = open('./public_ids.csv', 'r')
f2 = open('./game_list.csv', 'a', newline='')
writer = csv.writer(f2)

#Checking if the headers already exist in CSV so we do not append them again.
if os.stat('./game_list.csv').st_size == 0:
    writer.writerow(header)

#Starter steamID for increment
#steamID = 92171249
steamID = 92100009
#Total API calls = API_CALLS_PER_THREAD * NUM_THREADS
API_CALLS_PER_THREAD = 200
NUM_THREADS = 5

def api_call(self):
    #Loop through i next ID's
    for i in range(API_CALLS_PER_THREAD):
        try:
            response = requests.get('https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}&format=json'.format(apiKey,self.starting_id))
        except BaseException as e:
            print(str(e))
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
                        data = [int(self.starting_id), appID, time]
                        #Writing data row to the CSV file
                        writer.writerow(data)
            else:
                print("no games from {}".format(self.starting_id))
        else:
            print(response.status_code)
        #print('Getting steamID: {}'.format(current_id))
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
