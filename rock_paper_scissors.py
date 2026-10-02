import random
print("Welcome to Rock-Paper-Scissors")
choices = ["ROCK","PAPER","SCISSORS"]
def game():
    print("Choose an option\n1 - Rock\n2 - Paper\n3 - Scissors\n")
    while True:
        try:
            choice = input("Your choice: ").strip().upper()
            if choice in choices:
                break
            elif int(choice) in [1,2,3]:
                choice_num=int(choice)
                if choice_num == 1:
                    choice = "ROCK" 
                    break
                elif choice_num == 2:
                    choice = "PAPER"
                    break
                else:
                    choice = "SCISSORS"
                    break
            else:
                print("Input a valid option")
                continue

        except ValueError:
            print("Input a valid option")
            continue
                

game()
