from tkinter import RADIOBUTTON
import urllib.request
from pprint import pprint
import json

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data
riot_apikey = 'RGAPI-f6be3f32-59f4-4342-b7e1-34ee1c34fef7'
puuid_api = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'
match_history_api = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/'
match_data_api = 'https://americas.api.riotgames.com/lol/match/v5/matches/'

riot_id = [{'summoner' :'151433x', 'tagline':'na1'},{'summoner' : 'asura','tagline' :'nav1'}]

puuid = []
def get_puuid(ids):
    for items in ids:
        id = items['summoner']
        tag = items['tagline']
        json = get_json(f'{puuid_api}{id}/{tag}?api_key={riot_apikey}')
        puuid.append(json['puuid'])
    return puuid

get_puuid(riot_id)

match_history = []
def get_matches(ids):
    type ='normal'
    start = 0
    count = 1
    for items in ids: 
        json = get_json(f'{match_history_api}{items}/ids?type={type}&start={start}&count={count}&api_key={riot_apikey}')
        for match_ids in json:
            match_history.append(match_ids)
    return match_history
    
get_matches(puuid)

match_data = []
def get_match_data(matches): 
    for items in matches: 
        json = get_json(f'{match_data_api}{items}?api_key={riot_apikey}')
        match_data.append(json)
    return match_data

get_match_data(match_history)

player_crawl = []
def get_more_puuids(games):
    for items in games:
        players = items['metadata']['participants']
        for ids in players:
            player_crawl.append(ids)
    return player_crawl

get_more_puuids(match_data)

aram_matches = []
def get_aram(players):
    total_matches = get_matches(players)
    total_data = get_match_data(total_matches)
    for items in total_data: 
        if items['info']['gameMode'] == 'ARAM':
            aram_matches.append(items)
    return aram_matches

pprint(get_aram(player_crawl))







