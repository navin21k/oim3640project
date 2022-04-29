import pprint as pp
import json

from matplotlib.font_manager import json_load

def load_json():
    f = open("winloss.json")
    global winloss
    winloss = json.load(f)
    return winloss

load_json()

def load_json1():
    f=open('aram_gamedata.json')
    global winrate
    winrate=json.load(f)
    return winrate

load_json1()

def champlist():
    global champions
    champions=[]
    for items in winrate:
        champname=items['champion']
        if champname not in champions:
            champions.append(champname)
    return champions

champlist()

def versus_winrate(): 
    global versus_champ_winrate
    versus_champ_winrate = []
    for champs in champions:
        counter_rate = []
        versus =[x for x in champions if x != champs]
        for enemy in versus:
            wins = 0
            losses = 0
            for games in winloss: 
                if champs in games["winner"] and enemy in games["loser"]: 
                    wins +=1 
                if champs in games["loser"] and enemy in games["winner"]: 
                    losses += 1
            if wins + losses == 0:
                win_perc = "NA"
            else:
                win_perc = (wins/(wins+losses))*100
            counter = {enemy : win_perc}
            counter_rate.append(counter)
        counter_list = {champs : counter_rate}
        versus_champ_winrate.append(counter_list)
    return versus_champ_winrate

versus_winrate()
        
def synergy_winrate(): 
    global synergy_champ_winrate
    synergy_champ_winrate = []
    for champs in champions:
        synergy_rate = []
        teammates =[x for x in champions if x != champs]
        for player in teammates:
            wins = 0
            losses = 0
            for games in winloss: 
                if champs in games["winner"] and player in games["winner"]: 
                    wins += 1 
                if champs in games["loser"] and player in games["loser"]: 
                    losses += 1
            if wins + losses == 0:
                win_perc = "NA"
            else:
                win_perc = (wins/(wins+losses))*100
            synergy = {player : win_perc}
            synergy_rate.append(synergy)
        synergy_list = {champs : synergy_rate}
        synergy_champ_winrate.append(synergy_list)
    return synergy_champ_winrate
        
synergy_winrate()        

def save_file(): 
    json_object1 = json.dumps(versus_champ_winrate, indent = 4)
    with open("counter_rate.json", "w") as outfile1:
        outfile1.write(json_object1)
    json_object2 = json.dumps(synergy_champ_winrate, indent = 4)
    with open("synergy_rate.json", "w") as outfile2: 
        outfile2.write(json_object2)

save_file()
