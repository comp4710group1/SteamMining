from fpgrowth import fpgrowth
from pprint import pprint
import csv


itemSetList = []

with open('./dataset/data.csv', newline='') as f:
    reader = csv.reader(f)
    itemSetList = list(reader)

freqItemSet, rules = fpgrowth(itemSetList, minSupRatio = 0.75, minConf = 0.5)

print(itemSetList)

print('\n')
pprint(rules)
print('\n')
pprint(freqItemSet)
print('\n')

