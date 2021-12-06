def id_to_name(appid):
    f = open('../CSVFiles/game_id_lookup.csv', 'r')
    name = 'none'

    for line in f:
        data = line.split(',')
        if len(data) == 2:
            if int(appid) == int(data[0]):
                name = str(data[1])
    
    return name.strip('\n')

def translate(old_list):
    new_list = []

    for id in old_list:
        new_list.append(id_to_name(int(id)))
    
    return new_list
