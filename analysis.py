import json
import pprint

# propensity scoring
def propensitiy():
    pass

# vision per minute
def vision():
    pass

#load file
def load_json():
    f=open('winrate1.json')
    global winrate
    winrate=json.load(f)
    return winrate
#win rate per champ
load_json()
def champlist():
    global champions
    champions=[]
    for items in winrate:
        champname=items['champion']
        if champname not in champions:
            champions.append(champname)
    return champions
champlist()
def winrate_champ():
    global win_perc_list
    win_perc_list = []
    for i in champions:
        count = 0
        wins = 0
        for items in winrate: 
            if items['champion'] == i: 
                count += 1
            if items['champion'] == i and items['win'] == True:
                wins +=1
        win_percent=wins/count*100
        champ_perc = {i:[{"winrate" : win_percent},{"count": count}, {"wins": wins}]}
        win_perc_list.append(champ_perc)
    return win_perc_list
    
winrate_champ()
            
def save_file():
    json_object = json.dumps(win_perc_list, indent = 4)
    with open("champion_winrate.json", "w") as outfile:
        outfile.write(json_object)

save_file()
