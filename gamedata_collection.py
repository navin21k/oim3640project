import urllib.request
from pprint import pprint
import json
from player_collection import get_match_data
import time
 
def load_json():
    g = open('matches.json')
    global matches
    matches = json.load(g)
    for item in matches: 
        match_ids = item["match_id"]
    return match_ids

load_json()

# def get_data(): 
#     global match_data 
#     match_data = []
#     first = 0
#     last = 19
#     start_time = time.time()
#     while True:
#         current_time = time.time()
#         elapsed_time = current_time - start_time
#         if elapsed_time> 20:
#             data = get_match_data(matches[first:last])
#             match_data.append(data)
#             first += 20
#             last =+ 20
#             elapsed_time = 0
#             start_time = time.time()
#         if last >= 20:
#             break

# pprint(get_data())

# def get_arams(): 
#     aram_data = []
#     for items in match_data: 
#         if items['info']['gameMode'] == 'ARAM':
#             aram_data.append(items)
#     return aram_data



# def get_aram(players):
#     aram_matches = []
#     total_matches = get_matches(players)
#     total_data = get_match_data(total_matches)
#     for items in total_data: 
#         if items['info']['gameMode'] == 'ARAM':
#             aram_matches.append(items)
#     return aram_matches

# pprint(get_aram(puuids))

# json_object = json.dumps(aram_matches, indent = 4)
# with open("aram_data.json", "w") as outfile: 
#     outfile.write(json_object)