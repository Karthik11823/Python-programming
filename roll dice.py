import random

def roll_dice():
    return random.randrange(1,7)
while True:
    a=input("Enter 'd' to roll:")
    if (a.lower()=='d' ):
        print(roll_dice())
    else:
        break
    
        
