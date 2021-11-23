# SteamMining
This project looks to data mine the online gaming platform Steam. We will be analyzing what trends appear in the data. Furthermore we will be evaluating looking at the way Steam recommends games that are similar to what a user has played before. We will be using the FP growth algorithm to compute the frequent item sets of users recently played games with a minimum support of hours played and the user-defined tags (adventure, multiplayer, puzzle) that those games fall under. 

We are going to compare game recommendations based on the data available. For example, what games would be recommended based on the user-defined tags of games a user plays (e.g User A mostly plays games with the ‘strategy’ tag). Or what games would be recommended based on what games users usually play together (e.g 60% of users who play game A also play game B). Steam’s current ‘Interactive Recommender’ does not use tags or metadata to come up with their recommendations. We will come up with a data set where we utilize the user-defined tags to influence what games are recommended.

## Prerequisites 

## API Calls

<details><summary><b>Get Public Users</b></summary>

This API call was used to get a list of public Steam users. As we need to know a user's games, their profile must be public for it to be useful to us. Unfortunately, there is no obvious method to check a user's profile visibility status. The best way to achieve this was to check the response for fields only a public profile would provide. An example would be 'realname' is only provided if the profile is public

API call: https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=API_KEY&steamids=

- API_KEY would be your own steam dev API key.
- For steamids you would provide a '+' deliminated list of steam ids up to a max of 100 ids per call.

Request:
```
https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=09FEA56EF1B8EDD4A8602AC5AB529C72&steamids=
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

## Script Calls

## Resources