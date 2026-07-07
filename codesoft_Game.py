import random

# Initialize scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("===================================")
print("   ROCK - PAPER - SCISSORS GAME")
print("===================================")

while True:
    # User input
    user = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue

    # Computer choice
    computer = random.choice(choices)

    print("You chose      :", user)
    print("Computer chose :", computer)

    # Game logic
    if user == computer:
        print("Result: It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nCurrent Score")
    print("You      :", user_score)
    print("Computer :", computer_score)

    # Play again
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        break

print("\n===================================")
print("Final Score")
print("You      :", user_score)
print("Computer :", computer_score)

if user_score > computer_score:
    print("Congratulations! You won the game.")
elif computer_score > user_score:
    print("Computer won the game.")
else:
    print("The game ended in a tie.")

print("Thank you for playing!")
