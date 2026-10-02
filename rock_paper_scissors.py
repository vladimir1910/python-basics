import random
print("Welcome to Rock-Paper-Scissors")
choices_str = ["ROCK","PAPER","SCISSORS"]
choices_num = ["1","2","3"]
def choice_to_str(choice):
    if choice == "1":
        choice = "ROCK"
    elif choice == "2":
        choice = "PAPER"
    elif choice == "3":
        choice = "SCISSORS"
    return choice

def check_winner(computer,user):
    computer = choice_to_str(computer)
    print(f"The computer chose {computer}")

    if user == computer:
        print("Its a tie ")
    elif user == "ROCK" and computer == "SCISSORS":
        print("You won ")
    elif user == "PAPER" and computer == "ROCK":
        print("You won ")
    elif user == "SCISSORS" and computer == "PAPER":
        print("You won ")
    else:
        print("You lost ")


        

def user_choice():
    print("Choose an option\n1 - Rock\n2 - Paper\n3 - Scissors\n")
    while True:
        computer_choice=str(random.randint(1,3))
        while True:
            try:
                choice = input("Your choice: ").strip().upper()
                if choice in choices_str:
                    break
                elif choice in choices_num:
                    choice=choice_to_str(choice)
                    break
                    
                else:
                    print("Input a valid option")
                    continue

            except ValueError:
                print("Input a valid option")
                continue
        
        check_winner(computer_choice,choice)

        if again:=input("If you want to play again type A/a or anything else if you want to exit ").strip().upper() == "A":
            continue
        else:
            return


     
user_choice()
