# Number of games that have x number of tags

import csv

f = open('../TagScripts/game_tag_list.csv', 'r')
f2 = open('./game_tag_frequency.csv', 'w', newline='')
writer = csv.writer(f2)

tag_amount = []

for line in f: #for every line in the game to tag file
  tags = line.split(',')
  amount = len(tags) - 1
  
  # Remove VR only from the list
  if 'VR Only\n' in tags:
    amount -= 1
  
  tag_amount.append(amount)

output = {}

for amount in tag_amount:
  if amount not in output:
    output[amount] = 1
  else:
    output[amount] += 1 
  
  
for item in output:  
  writer.writerow([item, output[item]])