import urllib.request
from pprint import pprint
import json

from config import API_KEY1

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

riot_apikey = API_KEY1
puuid_api = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'
match_history_api = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/'
match_data_api = 'https://americas.api.riotgames.com/lol/match/v5/matches/'

riot_id = [{'summoner' :'151433x', 'tagline':'na1'},{'summoner' : 'asura','tagline' :'nav1'}]

puuid = []
def get_puuid(ids):
    for items in ids:
        id = items['summoner']
        tag = items['tagline']
        output = get_json(f'{puuid_api}{id}/{tag}?api_key={riot_apikey}')
        puuid.append(output['puuid'])
    return puuid

# get_puuid(riot_id)

match_history = []
def get_matches(ids):
    type ='normal'
    start = 0
    count = 20
    for items in ids: 
        json = get_json(f'{match_history_api}{items}/ids?type={type}&start={start}&count={count}&api_key={riot_apikey}')
        for match_ids in json:
            match_history.append(match_ids)
    return match_history
    
# get_matches(puuid)

match_data = []
def get_match_data(matches): 
    for items in matches: 
        json = get_json(f'{match_data_api}{items}?api_key={riot_apikey}')
        match_data.append(json)
    return match_data

# get_match_data(match_history)

player_crawl = []
def get_more_puuids(games):
    for items in games:
        players = items['metadata']['participants']
        participants = {"participants": players}
        player_crawl.append(participants)
    return player_crawl

# pprint(get_more_puuids(match_data))





