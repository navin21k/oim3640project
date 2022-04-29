from player_collection import riot_apikey
import json
import urllib

summoner_name_to_encrypted_api="https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
'151433x?api_key=RGAPI-304ed216-0466-4eea-abed-3716b4d04aeb'

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
    encrypted_summoner_id=get_json(f'{summoner_name_to_encrypted_api}/{summoner_name}?api_key={riot_apikey}')
    return encrypted_summoner_id
print(summoner_name_to_encrypted('151433x'))