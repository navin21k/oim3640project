import urllib.request
from pprint import pprint
import json
from player_collection import get_match_data
import time
 
def load_json():
    g = open('matches.json')
    global match_ids
    matches = json.load(g)
    for item in matches: 
        match_ids = item["match_id"]
    return match_ids

load_json()

def get_data(): 
    global match_data 
    match_data = []
    first = 0
    last = 19
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time> 20:
            data = get_match_data(match_ids[first:last])
            for items in data: 
                match_data.append(items)
            first += 20
            last =+ 20
            elapsed_time = 0
            start_time = time.time()
        if last >= 4000:
            break
    return match_data

get_data()

def get_arams(): 
    aram_data = []
    for items in match_data: 
        if items['info']['gameMode'] == 'ARAM':
            aram_data.append(items)
    json_object = json.dumps(aram_data, indent = 4)
    with open("aram_data.json", "w") as outfile: 
        outfile.write(json_object)

get_arams()