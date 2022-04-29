from player_collection import riot_apikey
import json
import urllib

summoner_name_to_encrypted_api="https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

def summoner_name_to_encrypted():
    encrypted_summoner_id=get_json("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/naaaaavin?api_key=RGAPI-60746c4e-c609-4ee5-8394-851977ea8750")
    return encrypted_summoner_id

print(summoner_name_to_encrypted())