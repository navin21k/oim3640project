from flask import Flask, redirect, render_template,request
from end_use_case import live_game_finder,get_list_champs

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def feeder():
    if request.method=="POST":
        global live_game
        live_game=request.form["riot_id"]
        try:
            team_1_players,team_1_champs,team_2_champs,team_2_players,gamemode=live_game_finder(live_game,get_list_champs())
            if gamemode!='ARAM':
                print("we only show ARAM data")
        except TypeError:
            return "there is no live game with this username."
        return render_template("result.html",team_1_players=team_1_players,team_1_champs=team_1_champs,team_2_champs=team_2_champs,team_2_players=team_2_players,gamemode=gamemode)
    return redirect('result.html')