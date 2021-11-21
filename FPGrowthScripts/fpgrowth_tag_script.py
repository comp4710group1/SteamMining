from fpgrowth import fpgrowth
from utils import getSupport

import csv

#when extracting split on '} ,'

item_set_list= []

f = open('./dataset/data_tags.csv', 'w', newline='')
writer = csv.writer(f, quotechar=' ')

with open('../TagScripts/game_tag_list.csv') as f:
    for line in f:
        #put line into list split on commas
        num_list = line.split(',')
        num_list.pop(0)
        #remove the \n on the last element
        if(len(num_list) > 0):
            num_list[len(num_list)-1] = num_list[len(num_list)-1].strip('\n')
            #put all those lists in the bigger list
            item_set_list.append(num_list)

#run fpgrowth
freqItemSet, rules = fpgrowth(item_set_list, minSupRatio = 0.1, minConf = 0.2)

for item in freqItemSet:
    support = 'support: ' + str(getSupport(item, item_set_list))
    if len(item) > 1:
        data = [item, support]
        
        writer.writerow(data)
