from flask import Flask, render_template, request, redirect
from hangman import reset_game_state, stringify_hangman_stand

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "GET":
    reset_game_state()
    hangman_stand = stringify_hangman_stand()
    return render_template("index.html", stand=hangman_stand, len=len(hangman_stand))
  
  else:
    user_guess = request.form["guess"]

if __name__ == "__main__":
  app.run()