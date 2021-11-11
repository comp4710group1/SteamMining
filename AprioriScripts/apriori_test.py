from efficient_apriori import apriori

item_set_list = []

with open('../UserScripts/game_list_parsed.csv') as f:
  for line in f:
    num_list = line.split(',')
    num_list[len(num_list) - 1] = num_list[len(num_list) - 1].strip('\n')
    item_set_list.append(num_list)

itemsets, rules = apriori(item_set_list, min_support=0.0005, min_confidence=0.05)
# print(rules)  # [{eggs} -> {bacon}, {soup} -> {bacon}]

file = open("test.txt", "w")

for itemset in itemsets:
  for item in itemsets[itemset]:
    for i in item:
      if (item.index(i) != len(item) - 1):
        file.write('{},'.format(i))  
      else:
        file.write('{}'.format(i))   
    file.write(':{}\n'.format(itemsets[itemset][item]))
    
file.close()