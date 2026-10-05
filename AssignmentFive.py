# Rock, Paper, Scissors Game
# The user enters their choice, and the program randomly generates a choice for the computer. 
# The program then determines the winner of each round and keeps track of the score.

import random

CHOICES = ("rock", "paper", "scissors")

# What each choice beats
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_player_choice():
    #Prompt the player, convert to lowercase, validate, and return the choice.
    while True:
        choice = input("Enter rock, paper, scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        else:
            print(f"Sorry, {choice} is not a valid choice. Please try again.")


def determine_winner(player, computer):
    #Compare the two choices and return 'win', 'loss', or 'tie' for the player.
    if player == computer:
        return "tie"
    elif BEATS[player] == computer:
        return "win"
    else:
        return "loss"


def get_number_of_rounds():
    #Ask for the number of rounds and make sure it is a positive odd number.
    prompt = "How many rounds would you like to play: "
    while True:
        response = input(prompt).strip()
        if not response.isdecimal():
            prompt = "Sorry, please enter a whole number. Please try again: "
            continue
        
        rounds = int(response)

        if rounds < 1 or rounds % 2 == 0:
            prompt = "Sorry, the number must be an odd number. Please try again: "
            continue

        return rounds


def main():
    print("Welcome to Rock Paper Scissors!")
    total_rounds = get_number_of_rounds()

    player_wins = 0
    player_losses = 0
    computer_wins = 0
    computer_losses = 0

    rounds_played = 0
    while rounds_played < total_rounds:
        player_choice = get_player_choice()
        computer_choice = random.choice(CHOICES)
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            print("Tie! Play again.")
            continue  # A tie does not count as a round

        elif result == "win":
            print("You won!")
            player_wins += 1
            computer_losses += 1
        else:
            print("You lost!")
            player_losses += 1
            computer_wins += 1

        rounds_played += 1

    print(f"Score is You: {player_wins} | Computer: {computer_wins}")

    if player_wins > computer_wins:
        print("You win!!!")
    else:
        print("The computer wins!")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()