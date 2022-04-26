import urllib.request
from pprint import pprint
import json
from player_collection import get_matches
import time

def load_json(file):
    f = open(file)
    puuid = json.load(f) 
    return puuid

participants = load_json("summoners_puuids.json")

def get_players(): 
    global puuids 
    puuids = []
    for items in participants: 
        ids = items['participants']
        for players in ids: 
            puuids.append(players)
    return puuids

get_players()

def get_data():
    global total_matches
    total_matches = []
    start_time = time.time()
    first = 0 
    last = 40
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time 
        if elapsed_time > 60:
            matches = get_matches(puuids[first:last])
            total_matches.append(matches)
            first += 41
            last += 41
            elapsed_time = 0
            start_time = time.time()
        if last > 380: 
            break
    return total_matches

get_data()

def make_json(): 
    new_dict = []
    for items in total_matches: 
        matches = {"match_id" : items}
        new_dict.append(matches)
    json_object = json.dumps(new_dict, indent = 4)
    with open("matches.json", "w") as outfile: 
        outfile.write(json_object)

make_json()
   