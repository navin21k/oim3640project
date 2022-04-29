import json
import pprint as pp

#load file
def load_json():
    f=open('winrate1.json')
    global winrate
    winrate=json.load(f)
    return winrate

load_json()

#win rate per champ
def champlist():
    global champions
    champions=[]
    for items in winrate:
        champname=items['champion']
        if champname not in champions:
            champions.append(champname)
    return champions

champlist()
    
def game_split():
    global total_games
    total_games = []
    first = 0 
    last = 10 
    while True: 
        games = []
        for items in winrate[first:last]: 
            games.append(items)
        first += 10
        last += 10
        total_games.append(games)    
        if last >= len(winrate):
            break
    return total_games

game_split()

def team_split(): 
    team_list = []
    for items in total_games:
        team1 = []
        team2= []
        for player in items():
            if player["win"] == True:
                team1.append(player)
            else:
                team2.append(player)
        game = [team1, team2]
        team_list.append(game)
    return team_list

pp.pprint(team_split())



