# Wordle Game main
# The user enters their choice and checks it against a randomly selected secret word. 
# The program provides feedback on each guess and keeps track of the number of guesses made. 

from wordle_functions import (
    choose_word,
    get_guess,
    evaluate_guess,
    display_guess,
    has_won,
    max_guesses,
)
 
 
def play_game():
    #Play one round of the game.
    secret_word = choose_word()
    previous_guesses = []   # list that stores every guess made so far
    won = False
 
    #The player gets up to max_guesses attempts.
    while len(previous_guesses) < max_guesses and not won:
        attempts_left = max_guesses - len(previous_guesses)
        print(f"Attempt {len(previous_guesses) + 1} of {max_guesses} "
              f"({attempts_left} left)")
 
        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)
 
        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)
 
        won = has_won(feedback)
 
    # Game over: tell the player how it went.
    if won:
        print(f"Congratulations! You guessed the word in "
              f"{len(previous_guesses)} attempt(s)!")
    else:
        print(f"Sorry, you're out of guesses. The word was "
              f"{secret_word.upper()}.")
 
 
def main():
    #Welcome the player and keep playing until they decline.
    print("Welcome to the Word Guessing Game!")
    print("Guess the secret 5-letter word in 6 tries.")
    print("  G = right letter, right place")
    print("  Y = right letter, wrong place")
    print("  - = letter is not in the word")
 
    play_again = "yes"
    while play_again == "yes":
        play_game()
 
        # Ask until the player gives a clear yes or no answer.
        answer = ""
        while answer not in ("yes", "no", "y", "n"):
            answer = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            play_again = "yes"
            print()
        else:
            play_again = "no"
 
    print("Thanks for playing! Goodbye.")
 
 
if __name__ == "__main__":
    main()