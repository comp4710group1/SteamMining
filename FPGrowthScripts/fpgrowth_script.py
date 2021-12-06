from fpgrowth import fpgrowth
from utils import getSupport

import csv

item_set_list= []

f = open('./dataset/data_games.csv', 'w', newline='')
writer = csv.writer(f, quotechar=' ')

with open('../CSVFiles/game_list_parsed.csv') as f:
    for line in f:
        #put line into list split on commas
        num_list = line.split(',')
        #remove the \n on the last element
        num_list[len(num_list)-1] = num_list[len(num_list)-1].strip('\n')
        #put all those lists in the bigger list
        item_set_list.append(num_list)

#run fpgrowth
freqItemSet, rules = fpgrowth(item_set_list, minSupRatio = 0.0003, minConf = 0.1)

for item in freqItemSet:
    support = 'support: ' + str(getSupport(item, item_set_list))
    if len(item) > 1:
        data = [item, support]

        writer.writerow(data)






#print(getSupport(['1009850', '1068820', '250820', '438100'], item_set_list))

#pprint(rules)
#pprint(freqItemSet)

