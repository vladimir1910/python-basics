import random
def game(wins=0, losses=0):   
    attempts=7
    number=random.randint(1,100)
    for turn in range(attempts):
        while True:
            try:
                guess=int(input(f"Turn {turn+1}, Type a number between 1 and 100: "))
                break
            except ValueError:
                print("Input a valid number ")
                continue
        if guess==number:
            print("You won ")
            wins+=1
            break
        if turn+1<attempts:
            print("Higher " if guess<number else "Lower")
    else:
        print(f"You lost! The number was {number}")
        losses+=1

    print("================================")
    print(f"📊 SCOREBOARD | Wins: {wins} | Losses: {losses}")
    print("================================")

    again=input("Type AGAIN if you want to play again, type anything else to exit ").strip().upper()
    if again == "AGAIN":
        print("Starting another game..")
        game(wins,losses)
    else:
        print("Thanks for playing")

game()