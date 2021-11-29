def id_to_name(appid):
    f = open('../AppScripts/game_id_lookup.csv', 'r')
    name = 'none'

    for line in f:
        data = line.split(',')
        if len(data) == 2:
            if int(appid) == int(data[0]):
                name = str(data[1])
    
    return name
