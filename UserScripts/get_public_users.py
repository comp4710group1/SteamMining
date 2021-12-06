import requests
import csv
import os
import threading

#Headers for the CSV file
header = ['steamID']

#Opening file and file writer
f = open('../CSVFiles/public_ids.csv', 'a', newline='')
writer = csv.writer(f)

#Checking if the headers already exist in CSV so we do not append them again.
if os.stat('../CSVFiles/public_ids.csv').st_size == 0:
    writer.writerow(header)

#Starter steamID for increment
steamID = 76561198056000000 #add 1 000 000 the next time you run
#Total API calls = NUM_THREADS * 100(due to 100 checks per call)
ID_INCREMENT = 100 #DONT CHANGE

NUM_THREADS = 1000

def api_call(self):
    current_id = self.starting_id
    #Loop through i next ID's
    api_string = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=&steamids='
    for i in range(100):
        current_id += i
        api_string += str(current_id) + '+'
    api_string = api_string[:-1]
    try:
        response = requests.get(api_string)
    except BaseException as e:
        print(str(e))
    data = response.json()
    for player in data["response"]["players"]:
        if 'realname' in player:
            output=[player["steamid"]]
            writer.writerow(output)



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

