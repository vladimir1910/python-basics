import random
win_combos = [("ROCK", "SCISSORS"), ("PAPER", "ROCK"), ("SCISSORS", "PAPER")]
choices_str = ("ROCK","PAPER","SCISSORS")
choices_map = {
    "1" : "ROCK",
    "2" : "PAPER",
    "3" : "SCISSORS"
}


def check_winner(computer,user):
    computer = choices_map[computer]
    print(f"The computer chose {computer}")

    if user == computer:
        print("Its a tie ")
        return "Tie"
    elif (user, computer) in win_combos:  
        print("You won ")
        return "Win"
    else:
        print("You lost ")
        return "Loss"


def user_choice():
    score ={ "Win":0 , "Loss":0, "Tie":0 }
    print("Choose an option\n1 - Rock\n2 - Paper\n3 - Scissors\n")
    while True:
        computer_choice=str(random.randint(1,3))
        while True:
            try:
                choice = input("Your choice: ").strip().upper()
                if choice in choices_str:
                    break

                elif choice in choices_map:
                    choice=choices_map[choice]                    
                    break  

                else:
                    print("Input a valid option")
                    continue

            except ValueError:
                print("Input a valid option")
                continue

        print(f"You chose {choice}")
        score[check_winner(computer_choice, choice)] += 1
        print(f"Score -> Wins: {score['Win']} | Losses: {score['Loss']} | Ties: {score['Tie']}\n")

        if again:=input("If you want to play again type A/a or anything else if you want to exit ").strip().upper() == "A":
            print("\n--- NEW ROUND ---")
            continue

        else:
            print(f"Final score -> Wins: {score['Win']} | Losses: {score['Loss']} | Ties: {score['Tie']}\n")
            print("Thanks for playing")
            return


    
print("Welcome to Rock-Paper-Scissors")
user_choice()

"""
def choice_to_str(choice):
    if choice == "1":
        choice = "ROCK"
    elif choice == "2":
        choice = "PAPER"
    elif choice == "3":
        choice = "SCISSORS"
    return choice
"""