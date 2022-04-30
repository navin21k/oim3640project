from config import API_KEY1
from player_collection import riot_apikey
import json
import urllib
import pprint as pp
summoner_name_to_encrypted_api="https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
live_game_finder_api='https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'
def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

# def loadData():
#     # for reading also binary mode is important
#     picklefile = open('./champion_ids.pickle','rb')     
#     champion_names = pickle.load(picklefile)
#     picklefile.close()
#     return champion_names
# list_bois=loadData()

def summoner_name_to_encrypted(summoner_name):
    encrypted_summoner_json=get_json(f'{summoner_name_to_encrypted_api}{summoner_name}?api_key={API_KEY1}')
    return encrypted_summoner_json['id']

def live_game_finder(name,champs):
    encrypted_id=summoner_name_to_encrypted(name)
    big_live_boi=get_json(f'{live_game_finder_api}{encrypted_id}?api_key={API_KEY1}')
    gamemode=big_live_boi['gameMode']
    team_1_players=[]
    team_1_champs=[]
    team_2_players=[]
    team_2_champs=[]
    winrate_team_1=dict()
    winrate_team_2=dict()
    dict1=dict()
    winrates=json.load(open('C:/Users/x1514/Documents/GitHub/oim3640project/data/champion_winrate.json'))
    for item in winrates:
        name=list(item)        
        dict1[name[0]]= item[name[0]][0]["winrate"]
    for i in big_live_boi['participants']:
        if i['teamId']==100:
            team_1_champs.append(champs[str(i['championId'])].replace(' ',''))
            team_1_players.append(i['summonerName'])
        else:

            team_2_champs.append(champs[str(i['championId'])].replace(' ',''))
            team_2_players.append(i['summonerName'])
    for champ in team_1_champs:
        winrate_team_1[champ]=dict1[champ]
    for champ in team_2_champs:
        winrate_team_2[champ]=dict1[champ]
    
    # dict2=dict()
    # counter=json.load(open('C:/Users/x1514/Documents/GitHub/oim3640project/data/counter_rate.json'))
    # for item in counter:s
    #     name=list(item)
    #     for champ in item        
    #     dict2[name[0]]= item[name[0]][0]["winrate"]

    # for items in team_1_champs:
        
    
    return team_1_players,winrate_team_1,winrate_team_2,team_2_players,gamemode

def get_list_champs():
    """created a dictionary"""
    names=dict(line.rstrip().split(':', 1) for line in open('champion_ids.txt'))
    return names



# live_game_finder('yemyyem',dict(line.rstrip().split(':', 1) for line in open('C:/Users/x1514/Documents/GitHub/oim3640project/data/champion_ids.txt')))


