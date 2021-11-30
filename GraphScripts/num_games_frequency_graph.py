import csv

f = open('../UserScripts/game_list_parsed.csv')
f1 = open('../AppScripts/game_id_lookup.csv')
f2 = open('./game_frequency.csv', 'w', newline='')
writer = csv.writer(f2)

game_dict = {}
game_lookup_dict = {}

for l in f1:
  game_lookup_dict[l.split(',')[0].strip('\n')] = name = l.split(',')[1].strip('\n')

for line in f:
  game_ids = line.split(',')
  
  for game_id in game_ids:
    if game_id.isdigit():
      name = game_lookup_dict[game_id.strip('\n')]
      
      if name not in game_dict:
        game_dict[name] = 1
      else:
        game_dict[name] += 1

for game in game_dict:
  writer.writerow([game.strip("\n"), game_dict[game]])