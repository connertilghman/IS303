# Number Guessing Game
# The computer picks a secret number between 1 and 100.
# The player keeps guessing until they get it right.
 
import random
 
play_again = "y"
 
# Keeps the game going as long as the player wants to play again
while play_again == "y" or play_again == "Y":
 
    # Pick a new random secret number for this round
    secret_number = random.randint(1, 100)
 
    num_guesses = 0
    guess = -1  # start with a value that can't match the secret number
 
    print("\nI'm thinking of a number between 1 and 100. Try to guess it!")
 
    # Keeps asking for guesses until the player gets it right
    while guess != secret_number:
 
        guess = int(input("Enter your guess (1-100): "))
 
        # Check that the guess is in the valid range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        else:
            # Valid guess, so count it
            num_guesses = num_guesses + 1
 
            if guess < secret_number:
                print("Too low! Guess higher.")
            elif guess > secret_number:
                print("Too high! Guess lower.")
            else:
                print("Congratulations! You guessed it!")
 
    # Print how many guesses it took
    print(f"It took you {num_guesses} guesses.")
 
    # Print a message based on the number of guesses
    if num_guesses <= 3:
        print("Amazing!")
    elif num_guesses <= 5:
        print("Impressive!")
    elif num_guesses <= 7:
        print("Good job!")
    elif num_guesses <= 9:
        print("Took a little longer, but you got there!")
    else:
        print("You need to lock in.")
 
    # Ask if the player wants to play again
    play_again = input("\nWould you like to play again? (Y/N): ")
 
print("Thanks for playing! Goodbye.")
    