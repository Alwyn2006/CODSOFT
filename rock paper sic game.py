import random

def play():
    users = 0
    computers = 0
    choices = ["rock", "paper", "scissors"]

    while True:
        print("\nRock-Paper-Scissors Game")
        user = input("Choose: rock, paper, or scissors (or 'quit' to exit): ").lower()

        if user == 'quit':
            print("Thanks for playing!")
            break
        elif user not in choices:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print("\nYou chose:",user)
        print("The computer chose: ",computer)

        if user == computer:
            print("tie!")
        elif (user == "rock" and computer == "scissors") or(user == "scissors" and computer== "paper") or (user == "paper" and computer == "rock"):
            print("You win")
            users += 1
        else:
            print("You lose")
            computers += 1

        print("Score - You: ",users)
        print("Score - computer: ",computers)


if __name__ == "__main__":
    play()
    
    
    
    
    
