from crypt import methods
from flask import Flask, render_template,request
from end_use_case import live_game_finder,list_bois

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def feeder():
    if request.method=="POST":
        global live_game
        live_game=request.form["riot_id"]
        try:
            team_1_players,team_1_champs,team_2_champs,team_2_players,gamemode=live_game_finder(live_game,list_bois)
            if gamemode!='ARAM':
                print("we only show ARAM data")
        except TypeError:
            print("there is no live game with this username.")
        return render_template("final_page.html",team_1_players=team_1_players,team_1_champs=team_1_champs,team_2_players=team_2_players,team_2_champs=team_2_champs,gamemode=gamemode)
