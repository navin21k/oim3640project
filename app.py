from crypt import methods
from flask import Flask, render_template,request

app=Flask(__name__)

# @app.route("/",methods=["POST","GET"])
# def feeder():
#     if request.method=="POST":
#         global live_game
#         live_game=request.form["riot_id"]
#         try:
#             stand=live_game_finder(live_game)
#         except TypeError:
#             print("there is no live game with this username.")
#         return render_template("final_page.html",)