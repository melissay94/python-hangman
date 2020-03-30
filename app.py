from flask import Flask, render_template, request, redirect
from hangman import reset_game_state, get_hangman_stand, get_letter_graveyard, get_user_progress, update_game

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "GET":
    reset_game_state()
  
  else:
    user_guess = request.form["guess"]
    update_game(user_guess.lower())
  
  hangman_stand = get_hangman_stand()
  return render_template("index.html", 
    stand=hangman_stand, 
    len=len(hangman_stand), 
    letter_graveyard=get_letter_graveyard(),
    user_progress=get_user_progress()
  )
    

if __name__ == "__main__":
  app.run()