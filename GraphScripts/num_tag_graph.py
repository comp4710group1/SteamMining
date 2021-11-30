import csv

f = open('../TagScripts/game_tag_list.csv', 'r')
f2 = open('./tag_frequency.csv', 'w', newline='')
writer = csv.writer(f2)

tag_dict = {}

for line in f: #for every line in the game to tag file
  tags = line.split(',') #tags[0] will be the appid, the rest will be the tags
  if len(tags) > 1: #make sure the game actually has tags
    for tag in range(1, len(tags)): #look through all the tags from that game
      if tags[tag] not in tag_dict: #if the tag isnt in the dict yet, add it
        tag_dict[tags[tag]] = 1
      else:                         #otherwise, increment the count by 1
        tag_dict[tags[tag]] += 1 

for tag in tag_dict:
  writer.writerow([tag.strip("\n"), tag_dict[tag]])


