#Rock-Paper-Scissors Game
import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    
    # Initialize scores
    user_score = 0
    computer_score = 0
    rounds_played = 0

    choices = ["rock", "paper", "scissors"]

    while True:
        print("\nRound", rounds_played + 1)
        print("Choose your option: Rock, Paper, or Scissors (or type 'exit' to quit)")
        
        # User input
        user_choice = input("Your choice: ").strip().lower()
        if user_choice == "exit":
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        # Computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice.capitalize()}")

        # Determine the result
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Update rounds
        rounds_played += 1
        print(f"Score: You {user_score} - {computer_score} Computer")

    # Final results
    print("\nGame Over!")
    print(f"Total Rounds Played: {rounds_played}")
    print(f"Final Score: You {user_score} - {computer_score} Computer")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif user_score < computer_score:
        print("Computer wins overall. Better luck next time!")
    else:
        print("It's a tie overall!")

# Run the game
rock_paper_scissors()
