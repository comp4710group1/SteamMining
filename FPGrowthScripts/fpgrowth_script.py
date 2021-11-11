from fpgrowth import fpgrowth
from pprint import pprint
import csv

item_set_list= []

with open('../UserScripts/game_list_parsed.csv') as f:
    for line in f:
        #put line into list split on commas
        num_list = line.split(',')
        #remove the \n on the last element
        num_list[len(num_list)-1] = num_list[len(num_list)-1].strip('\n')
        #put all those lists in the bigger list
        item_set_list.append(num_list)

#run fpgrowth
freqItemSet, rules = fpgrowth(item_set_list, minSupRatio = 0.0005, minConf = 0.05)

print('\n')
pprint(rules)
print('\n')
#pprint(freqItemSet)
print('\n')

