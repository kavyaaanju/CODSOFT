import random

PLAY = True
while PLAY:
    # print the instructions to the player
    print("\nPlease enter your choice: Rock, Paper, or Scissors")
    player_turn = input("Choose: ").lower()

    # validate user input
    while player_turn not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose from Rock, Paper, or Scissors.")
        player_turn = input("Choose: ").lower()

    # generate a random choice for the computer
    computer_turn = random.choice(["rock", "paper", "scissors"])

    print(f"Player: {player_turn.capitalize()}\tComputer: {computer_turn.capitalize()}")

    # determine the winner
    if player_turn == computer_turn:
        print("It's a Tie!")
    elif (player_turn == "rock" and computer_turn == "paper") or \
         (player_turn == "paper" and computer_turn == "scissors") or \
         (player_turn == "scissors" and computer_turn == "rock"):
        print("Computer wins!")
    else:
        print("Player wins!")

    # ask the user if they want to continue playing
    print("\nDo you want to play again? (y/n)")
    if input().lower() == "n":
        PLAY = False
        print("Thank you for playing!")
    else:
        continue
