import random
attempts=7
number=random.randint(1,100)
x=0
guess=None
while x < attempts and guess != number:
    guess=int(input("Type a number between 1 and 100: "))
        
    if guess>number:
        print("Lower.. ")
        x+=1
    elif guess<number:
        print("Higher..")
        x+=1
if guess==number:
    print(f"You won! The number was {number}")
else:
    print(f"You lost! The number was {number}")
