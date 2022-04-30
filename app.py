from distutils.log import error
from flask import Flask, redirect, render_template,request
from end_use_case import live_game_finder,get_list_champs

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def feeder():
    if request.method=="POST":
        global live_game
        live_game=request.form["riot_id"]
        try:
            team_1_players,team_1_champs,team_2_champs,team_2_players,gamemode=live_game_finder(live_game,dict(line.rstrip().split(':', 1) for line in open('C:/Users/x1514/Documents/GitHub/oim3640project/data/champion_ids.txt')))
            if gamemode!='ARAM':
                print('aram')
                return render_template("form.html",error="we only do ARAM data")
        except :
            print('live')
            return render_template("form.html",error="there are no live games")
        return render_template("result.html",team_1_players=team_1_players,team_1_champs=team_1_champs,team_2_champs=team_2_champs,team_2_players=team_2_players,gamemode=gamemode)
    return render_template("form.html",error='')
    # return redirect('form.html')