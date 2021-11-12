from fpgrowth import fpgrowth
from pprint import pprint
from utils import getSupport

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
freqItemSet, rules = fpgrowth(item_set_list, minSupRatio = 0.005, minConf = 0.2)

for item in freqItemSet:
    support = 'support: ' + str(getSupport(item, item_set_list))
    print(str(item) + ' | ' + support)

#print(getSupport(['1009850', '1068820', '250820', '438100'], item_set_list))

#pprint(rules)
#pprint(freqItemSet)

