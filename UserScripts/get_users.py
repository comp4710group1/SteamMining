import requests
import csv
import os
import threading

#API Key
apiKey = "C4364E1FFD0AFF0CA0FD74ACBD3ADBFF"

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
#Total API calls = ID_INCREMENT * NUM_THREADS
ID_INCREMENT = 200
NUM_THREADS = 5

def api_call(self):
    current_id = self.starting_id
    #Loop through i next ID's
    for i in range(ID_INCREMENT):
        try:
            response = requests.get('https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid=765611980{}&format=json'.format(apiKey,current_id))
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
                        data = [current_id, appID, time]
                        #Writing data row to the CSV file
                        writer.writerow(data)
            else:
                print("no games lul")
        else:
            print(response.status_code)
        #print('Getting steamID: {}'.format(current_id))
        current_id += 1

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

#Main
if __name__ == "__main__":
    workers = []

    #Making NUM_THREADS worker threads
    for count in range(NUM_THREADS):
        workers.append(my_thread(count, 'thread {}'.format(count), steamID))
        steamID += ID_INCREMENT
        
    #Start each worker "run"
    for x in workers:
        x.start()

