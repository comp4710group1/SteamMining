#https://steamspy.com/api.php

import requests

#grab app info for CSGO
response = requests.get('https://steamspy.com/api.php?request=appdetails&appid=730')

if(response.status_code == 200):
    app_info = response.json()

    #this api call also lets us skip over the appid to name phase and gives the name directly
    name = app_info['name']
    tags = app_info['tags']

    tag_string = ''
    for key in tags:
        #could easily get check tags above a certain threshold
        tag_string += '{} tagged {} times, '.format(key, tags[key])

    print('Game: {}, Tags: {}'.format(name, tag_string))

else:
    print('Something goofed up with the request: {}'.format(response.status_code))
