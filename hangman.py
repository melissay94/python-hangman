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

  current_secret_word = secret_words[randint(0, len(secret_words)-1)]

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

def get_hangman_stand():
  global hangman_stand
  row_arr = []
  for line in hangman_stand:
    row_arr.append(("".join(line)))
  
  return row_arr;

def get_user_progress():
  global hidden_word_array
  return "".join(hidden_word_array)

def get_letter_graveyard():
  global letter_graveyard
  return ", ".join(letter_graveyard)


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

def incorrect_guess():
  global hangman_stand
  global hangman_parts
  global hangman_coordinates

  hangman_stand[hangman_coordinates[0][0]][hangman_coordinates[0][1]] = hangman_parts[0]
  hangman_coordinates.pop(0)
  hangman_parts.pop(0)

def end_round():
  global hidden_word_array
  global current_secret_word
  global hangman_stand

  if "".join(hidden_word_array) == current_secret_word:
    return True
  else:
    return False

def update_game(guess):
  
  if len(guess) > 1:
    return "You can only guess one letter at a time"
  
  if guess.isalpha() == False:
    return "You can only guess letters"
  
  if guess in letter_graveyard:
    return "You have already guessed that letter"

  letter_graveyard.append(guess)

  if guess in current_secret_word:
    correct_guess(guess)

  else: 
    incorrect_guess()

  if len(hangman_parts) <= 0 or "".join(hidden_word_array) == current_secret_word:
    if end_round() == True:
      return "You Won!"
    else: 
      return "Better Luck Next Time"

