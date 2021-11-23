# SteamMining
This project looks to data mine the online gaming platform Steam. We will be analyzing what trends appear in the data. Furthermore we will be evaluating looking at the way Steam recommends games that are similar to what a user has played before. We will be using the FP growth algorithm to compute the frequent item sets of users recently played games with a minimum support of hours played and the user-defined tags (adventure, multiplayer, puzzle) that those games fall under. 

We are going to compare game recommendations based on the data available. For example, what games would be recommended based on the user-defined tags of games a user plays (e.g User A mostly plays games with the ‘strategy’ tag). Or what games would be recommended based on what games users usually play together (e.g 60% of users who play game A also play game B). Steam’s current ‘Interactive Recommender’ does not use tags or metadata to come up with their recommendations. We will come up with a data set where we utilize the user-defined tags to influence what games are recommended.

## Prerequisites 

## API Calls

### Terms
- API_KEY refers to your own API key from steam

### Calls

<details><summary><b>Get Public Users</b></summary>

This API call was used to get a list of public Steam users. As we need to know a user's games, their profile must be public for it to be useful to us. Unfortunately, there is no obvious method to check a user's profile visibility status. The best way to achieve this was to check the response for fields only a public profile would provide. An example would be 'realname' is only provided if the profile is public

API call: https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=API_KEY&steamids=

- For steamids you would provide a '+' deliminated list of steam ids up to a max of 100 ids per call.

Request:
```
https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=API_KEY&steamids=76561198052460701
```
Response:
```
{
    "response":{
        "players":[
            {
                "steamid":"76561198052460701",
                "communityvisibilitystate":3,
                "profilestate":1,
                "personaname":"Nate",
                "profileurl":"https://steamcommunity.com/id/ethic_xz/",
                "avatar":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/b7/b74c35ea69412656548ced1861fd09e081fb907d.jpg",
                "avatarmedium":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/b7/b74c35ea69412656548ced1861fd09e081fb907d_medium.jpg",
                "avatarfull":"https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/b7/b74c35ea69412656548ced1861fd09e081fb907d_full.jpg",
                "avatarhash":"b74c35ea69412656548ced1861fd09e081fb907d",
                "personastate":0,
                "realname":"Nate",
                "primaryclanid":"103582791429521408",
                "timecreated":1321121194,
                "personastateflags":0,
                "loccountrycode":"GB"
            }
        ]
    }
}
```

</details>


<details><summary><b>Get Users Games</b></summary>

The purpose of this call is to get a list of all the recently played games from a public user. Getting only the recently played games allows us to keep the recommendations as up to date as possible. Additionally, Steam's API call to get all played games is very spotty and only works half the time.

API call: https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key=<em>API_KEY</em>&steamid=<em>PUBLIC_STEAM_ID</em>&format=json

- PUBLIC_STEAM_ID refers to a single public steam id

Request:
```
https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key=API_KEY&steamid=76561198052460701&format=json
```

Response:
```
{
    "response":{
        "total_count":4,
        "games":[
            {
                "appid":39210,
                "name":"FINAL FANTASY XIV Online",
                "playtime_2weeks":1778,
                "playtime_forever":36508,
                "img_icon_url":"98527a5229540d86ced171d8a5dff2f8a560fe80",
                "img_logo_url":"7888f35ccda304c0421951950c74b28357ea09bd",
                "playtime_windows_forever":36508,"playtime_mac_forever":0,
                "playtime_linux_forever":0
            },
            {
                "appid":1276790,
                "name":"Ruined King: A League of Legends Story™",
                "playtime_2weeks":380,
                "playtime_forever":380,
                "img_icon_url":"cac53a5db43167ab2bfe2be1496505bf0762710d",
                "img_logo_url":"1fda11413554296d710c8d81c73c65a6b4249329",
                "playtime_windows_forever":380,
                "playtime_mac_forever":0,
                "playtime_linux_forever":0
            },
            {
                "appid":359320,
                "name":"Elite Dangerous",
                "playtime_2weeks":145,
                "playtime_forever":8150,
                "img_icon_url":"670f2f289a180f7ac291585df847009640ebf1c5",
                "img_logo_url":"e7ae8414879ff5e547df85935ba5576dbc0639e3",
                "playtime_windows_forever":8150,
                "playtime_mac_forever":0,
                "playtime_linux_forever":0
            },
            {
                "appid":739630,
                "name":"Phasmophobia",
                "playtime_2weeks":81,
                "playtime_forever":1115,
                "img_icon_url":"125673b382059f666ec81477173380a76e1df0be",
                "img_logo_url":"e63390ac4ae4bf78787e09f5345629eb5955c6f1",
                "playtime_windows_forever":1115,
                "playtime_mac_forever":0,
                "playtime_linux_forever":0
            }
        ]
    }
}
```

</details>


<details><summary><b>Get Game Tags</b></summary>

For the purpose of recommendations we also wanted to retrieve user define tags. Steam doesn't provide a way to get these, so we relied on a third party API.

API call: https://steamspy.com/api.php?request=appdetails&appid=APP_ID

- APP_ID is the app id of the game you want details on

Request:
```
https://steamspy.com/api.php?request=appdetails&appid=730
```

Response:
```
{
    "appid":730,
    "name":"Counter-Strike: Global Offensive",
    "developer":"Valve, Hidden Path Entertainment",
    "publisher":"Valve",
    "score_rank":"",
    "positive":5309071,
    "negative":714606,
    "userscore":0,
    "owners":"50,000,000 .. 100,000,000",
    "average_forever":28420,
    "average_2weeks":842,
    "median_forever":6139,
    "median_2weeks":316,
    "price":"0",
    "initialprice":"0",
    "discount":"0",
    "ccu":741841,
    "languages":"English, Czech, Danish, Dutch, Finnish, French, German, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Portuguese - Brazil, Romanian, Russian, Simplified Chinese, Spanish - Spain, Swedish, Thai, Traditional Chinese, Turkish, Bulgarian, Ukrainian, Greek, Spanish - Latin America, Vietnamese",
    "genre":"Action, Free to Play",
    "tags":{
        "FPS":87052,
        "Shooter":62454,
        "Multiplayer":59663,
        "Competitive":51113,
        "Action":45695,
        "Team-Based":44633,
        "e-sports":41488,
        "Tactical":39816,
        "First-Person":37809,
        "PvP":32986,
        "Online Co-Op":32725,
        "Co-op":29180,
        "Strategy":29049,
        "Military":27704,
        "War":27139,
        "Difficult":25214,
        "Trading":24786,
        "Realistic":24590,
        "Fast-Paced":24580,
        "Moddable":5865
    }
}
```

</details>

## Script Calls

In order to drastically increase the speed of hundreds of thousands of calls these scripts make great use of multi-threading

- Running python scripts can be a bit weird sometimes. If py doesn't work try python and python3

<details><summary><b>Get Public Users</b></summary>

After making the API call this script parses the results, removing private profiles. It then writes those unpruned profiles to another file to be processed later.

Calling from the top level directory:
```sh
...\SteamMining> py .\UserScripts\get_public_users.py
```

</details>

<details><summary><b>Get Public Users</b></summary>

After making the API call this script parses the results, removing private profiles. It then writes those unpruned profiles to another file to be processed later.

Calling from the top level directory:
```sh
...\SteamMining> py .\UserScripts\get_public_users.py
```

</details>

## Resources