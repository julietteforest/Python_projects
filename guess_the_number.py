

"""
Try to guess a number between 0 and 10. You have 3 trials.
08/2019
Author:
        Juliette Forest
"""


import random
def guess():
    attempt = 0
    computer_choice = random.randint(0,10)
    while attempt < 3 or computer_choice == player_choice:
        player_choice = input("What is the secret number ? ")
        player_choice = int(player_choice)
        if  player_choice == computer_choice:
            print("You won")
            break
        else:
            attempt += 1
            print("Try again")
            if attempt == 3:
                print("You lost, the secret number was {}.".format(computer_choice))
