import random

def pickRandomCard():
    rank=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    suit=["Clubs","Diamonds","Hearts","Spades"]
    return "{} of {}".format(random.choice(rank),random.choice(suit))

print(pickRandomCard())