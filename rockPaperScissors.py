import random

shape=["rock","paper","scissors"]

def randomShape():
    return random.choice(shape)

print(("-" * 15) + "Welcome to the 'Rock Paper Scissors' Game " + ("-" * 15))
userScore,computerScore=0,0

while True:
    choose=int(input("\n0-for quit\n1-rock\n2-paper\n3-scissors\nChoose a shape:"))

    if(choose==0):
        print(("-" * 30) + "Rock Paper Scissors" + ("-" * 30))
        break

    if(choose<1 or choose>3):
        print("\nWrong number please press 1 for rock, 2 for paper, 3 for scissors\n")
        print(("-" * 30) + "Rock Paper Scissors" + ("-" * 30))
        continue

    chooseOfComputer=randomShape()
    chooseOfUser=shape[choose-1]

    print(f"\nYour choice: {chooseOfUser}\nComputer choice: {chooseOfComputer}")

    if(chooseOfUser==shape[0]):
        if(chooseOfComputer==shape[0]):
            print("Draw")
        elif(chooseOfComputer==shape[1]):
            print("You lost")
            computerScore+=1
        else:
            print("You won")
            userScore+=1
    
    elif(chooseOfUser==shape[1]):
        if(chooseOfComputer==shape[1]):
            print("Draw")
        elif(chooseOfComputer==shape[2]):
            print("You lost")
            computerScore+=1
        else:
            print("You won")
            userScore+=1

    else:
        if(chooseOfComputer==shape[2]):
            print("Draw")
        elif(chooseOfComputer==shape[0]):
            print("You lost")
            computerScore+=1
        else:
            print("You won")
            userScore+=1

    print(("-" * 30) + "Rock Paper Scissors" + ("-" * 30))

print("Game Over")

if(userScore>computerScore):
    print(f"\nYou won!\nYour score: {userScore}\nComputer score: {computerScore}")
elif(userScore<computerScore):
    print(f"\nYou lost!\nYour score: {userScore}\nComputer score: {computerScore}")
else:
    print(f"\nDraw!\nYour score: {userScore}\nComputer score: {computerScore}")