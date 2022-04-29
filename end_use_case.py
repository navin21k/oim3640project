from config import API_KEY1
from player_collection import riot_apikey
import json
import urllib

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

def summoner_name_to_encrypted(summoner_name):
    encrypted_summoner_json=get_json(f"{summoner_name_to_encrypted}{summoner_name}?api_key={API_KEY1}")
    return encrypted_summoner_json['id']
    
def live_game_finder(name):
    encrypted_id=summoner_name_to_encrypted(name)
    big_live_boi=get_json(f'{live_game_finder_api}{encrypted_id}?api_key={API_KEY1}')
    gamemode=big_live_boi['gameMode']
    champions=[]
    for i in big_live_boi['participants']:
        
        champions.append()




print(summoner_name_to_encrypted())