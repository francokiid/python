from time import sleep
from os import system

print("EXERCISE 8. Rock Scissors Paper".center(75))

sleep(1)

print("\nPlease enter your name:")
name_player1 = input("Player 1: ")
name_player2 = input("Player 2: ")

score_player1 = 0
score_player2 = 0

sleep(1)

while True:
        
    system('cls')

    print("EXERCISE 8. Rock Paper Scissors".center(75))
    print('''\nPlease pick one:
    rock
    paper
    scissors\n''')

    rsp_player1 = input(name_player1 + ": ")

    if rsp_player1.lower() in ["rock", "paper", "scissors"]:

        rsp_player2 = input(name_player2 + ": ")

        if rsp_player2.lower() in ["rock", "paper", "scissors"]:
            
            sleep(1)

            rsp_dict = {"rock": 1, "paper": 2, "scissors": 3}

            p1 = rsp_dict.get(rsp_player1)
            p2 = rsp_dict.get(rsp_player2)
            dif = p1 - p2

            print("\r")

            if dif in [-2, 1]:
                print(name_player1 + " wins!")
                score_player1 += 1
            elif dif in [-1, 2]:
                print(name_player2 + " wins!")
                score_player2 += 1
            else:
                print("It's a draw!")
        else:
            print("\nInvalid input.")
    else:
        print("\nInvalid input.")

    while True:
        play_again = input("\nPlay again?   [Y] Yes   [N] No    ")

        sleep(1)

        if play_again.lower() == "y":
            break
        elif play_again.lower() == "n":
            system('cls')

            print("EXERCISE 8. Rock Paper Scissors".center(75))
            print("\nThank you for playing the game!\n\nScoreboard:")

            print(name_player1 + " - " + str(score_player1))
            print(name_player2 + " - " + str(score_player2))

            sleep(1)
            exit()
        else:
            print("\nInvalid input.")
