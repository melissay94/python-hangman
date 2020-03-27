from random import randint

# Store a list of words to pick from
secret_words = ["apple", "bamboo", "cherry", "coconut", "flower", "orange", "peach", "pear", "turnip"]
#Choose a word at random
current_secret_word = hidden_word_str = hidden_word_array = letter_graveyard = hangman_parts = hangman_stand = hangman_coordinates = None

def reset_game_state():
  global secret_words
  global current_secret_word
  global hidden_word_str
  global hidden_word_array
  global letter_graveyard
  global hangman_stand
  global hangman_parts
  global hangman_coordinates

  current_secret_word = secret_words[randint(0, len(secret_words))]

  #Display a string of the same length as the random word but as underscores
  hidden_word_str = "_" * len(current_secret_word)
  hidden_word_array = list(hidden_word_str)
  letter_graveyard = []

  # set up an array of hangman parts
  hangman_parts = ["O", "|", "-", "-", "/", "\\"]

  hangman_stand = [
    [" ", "_", "_", "_", " ", " "],
    ["|", " ", " ", " ", " |", " "],
    ["|", " ", " ", " ", " ", " "],
    ["|", " ", " ", " ", " ", " "],
    ["|", " ", " ", " ", " ", " "],
    ["|", " ", " ", " ", " ", " "]
  ]

  hangman_coordinates = [(2, 4), (3, 4), (3, 3), (3, 5), (4, 3), (4, 5)]

def show_game_state():
  global hangman_stand
  global letter_graveyard
  global hidden_word_array

  print("Your word: " + "".join(hidden_word_array))

  for line in hangman_stand:
    print("".join(line))
  
  print("Letter graveyard: " + ", ".join(letter_graveyard))


def find_occurances(word, letter):
  occurances_array = []
  for i in range(0, len(word)):
    if letter == word[i]:
      occurances_array.append(i)
  return occurances_array

def correct_guess(user_guess):
    global hidden_word_array
    global current_secret_word
    # Reveal that letter if it's in the word
    guess_indices = find_occurances(current_secret_word, user_guess)
    for index in guess_indices:
      hidden_word_array[index] = user_guess

def incorrect_guess(user_guess):
  global hangman_stand
  global hangman_parts
  global hangman_coordinates

  print("That letter doesn't exist")
  hangman_stand[hangman_coordinates[0][0]][hangman_coordinates[0][1]] = hangman_parts[0]
  hangman_coordinates.pop(0)
  hangman_parts.pop(0)

def end_round():
  global hidden_word_array
  global current_secret_word
  global hangman_stand

  if "".join(hidden_word_array) == current_secret_word:
    print("Good job!")
    print("You guessed the word! " + "".join(hidden_word_array))
  else:
    for line in hangman_stand:
      print("".join(line))

    print("Oops... maybe next time")

# Set up loop
def game_loop():
  while(len(hangman_parts) > 0  and "".join(hidden_word_array) != current_secret_word):
  
    show_game_state()

    # Get user input
    user_guess = input("Guess a letter: ").lower()  

    # See if user input is one letter AND within the word
    if len(user_guess) > 1:
      print("You can only guess one letter at a time")
      continue

    if user_guess in letter_graveyard or user_guess in hidden_word_array:
      print("You've already guessed that letter")
      continue
    
    letter_graveyard.append(user_guess)

    if user_guess in current_secret_word:
      correct_guess(user_guess)

    else:
      # Letter is incorrect, draw a nother stick part
      incorrect_guess(user_guess)

  end_round()

play_game = True

while(play_game == True):
  reset_game_state()
  game_loop()
  user_answer = input("Do you want to go again? (yes/no)")

  if user_answer.lower() != "yes":
    print("See you next time!")
    play_game = False

