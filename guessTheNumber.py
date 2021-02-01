import random

number=random.randint(1,100)
trying=0

while True:
    guess=int(input("Please enter the number: "))
    trying+=1
    if number<guess:
        print("decrease the number\n")
    elif guess<number:
        print("increase the number\n")
    else:
        print(f"Congratulations! You found the number on the {trying}th trying")
        break