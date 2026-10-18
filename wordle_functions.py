# Wordle Game functions
# The user enters their choice and checks it against a randomly selected secret word. 
# The program provides feedback on each guess and keeps track of the number of guesses made. 
 
import random
 
# Number of letters in every word and number of allowed guesses.
word_length = 5
max_guesses = 6
 
# Secret words to choose from. None of these words contain a repeated letter.
word_list = [
    "plant", "crane", "stone", "light", "brick", "flame", "grape",
    "house", "music", "night", "ocean", "pearl", "quilt", "raven"
]
 
def choose_word():
    #Pick a random secret word from WORD_LIST and return it.
    return random.choice(word_list)
 
 
def get_guess(previous_guesses):
    #Ask the player for a guess until a valid one is entered.
    #A valid guess has exactly five letters and has not been used yet.
    #Returns the guess in lowercase.
    
    while True:
        guess = input("Enter your guess: ").strip().lower()
 
        # Rule 1: the guess must be exactly five letters.
        if len(guess) != word_length or not guess.isalpha():
            print("Your guess must contain exactly 5 letters. Try again.")
        # Rule 2: the guess cannot repeat an earlier guess.
        elif guess in previous_guesses:
            print("You already guessed that word. Try a different one.")
        else:
            return guess
 
 
def evaluate_guess(guess, secret_word):
    #Compare the guess with the secret word.
 
    #Returns a list of five feedback symbols, one per letter:
    #  G = right letter, right position
    #  Y = letter is in the word, but in a different position
    #  - = letter is not in the word
    
    feedback = []
 
    for position in range(word_length):
        letter = guess[position]
 
        if letter == secret_word[position]:
            feedback.append("G")          # correct letter, correct spot
        elif letter in secret_word:
            feedback.append("Y")          # correct letter, wrong spot
        else:
            feedback.append("-")          # letter not in the word
 
    return feedback
 
 
def display_guess(guess, feedback):
    # Show the guess and the feedback symbols lined up.
    print()
    print("Guess:    " + " ".join(guess.upper()))
    print("Feedback: " + " ".join(feedback))
 
    # Explain each letter in words.
    for position in range(word_length):
        letter = guess[position].upper()
        if feedback[position] == "G":
            print(f"  {letter} is correct and in the right place.")
        elif feedback[position] == "Y":
            print(f"  {letter} is in the word, but in the wrong place.")
        else:
            print(f"  {letter} is not in the word.")
    print()
 
 
def has_won(feedback):
    #Return True if every letter is green (the word was guessed).
    return feedback == ["G"] * word_length