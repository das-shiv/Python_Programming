import random

while True:
    decision = ['rock', 'paper', 'scissor']
    computer = random.choice(decision)
    human = None
    while human not in decision:
        human = input("Select one... rock,paper or scissor? ").lower()
    
    if human == computer:
        print("You choose: ",human)
        print("Computer chose: ",computer)
        print("It's a tie")
    elif  human == "rock":
        if computer == "paper":
            print("You choose: ",human)
            print("Computer chose: ",computer)
            print("You lose..")
        
        if computer == "scissor":
            print("You choose: ",human)
            print("Computer chose: ",computer)
            print("You won..")

    elif  human == "paper":
        if computer == "rock":
            print("You choose: ",human)
            print("Computer chose: ",computer)
            print("You won...")
        
        if computer == "scissor":
            print("You choose: ",human)
            print("Computer chose: ",computer)
            print("You lose..")

    elif  human == "scissor":
        if computer == "paper":
            print("You choose: ",human)
            print("Computer chose: ",computer)
            print("You won..")
        
        if computer == "rock":
            print("You choose: ",human)
            print("Computer chose: ",computer)
            print("You lose..")

    play_again = input("Play again? (Y/N): ").lower()

    if play_again != "y" and play_again != "yes":
        break
print("Bye.....")