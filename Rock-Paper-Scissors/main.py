import os
import random

os.system('cls')

def validate_input(s):
    if not s.isnumeric() or not s or s not in "123":
        return False
    return int(s)


def random_output():
    tab = ["", "", ""]
    l = ["Rock", "Paper", "Scissors"]
    i = 0
    while i < len(tab):
        n = random.randint(0, len(tab)-1)
        if tab[n] == "":
            tab[n] = l[i]
            i += 1
    return tab


def game():
    rps = random_output()
    print("ROCK!!! PAPERS!!! SCISSORS!!! START")
    print("+++++++++++++++++++++ Notice: (the texts Rock, Paper and Scissors don't follow the orders of these numbers, they're random) +++++++++++++++++++++\n\n")
    p1 = input("Player A, choose a number (1, 2 or 3):  ")
    while not validate_input(p1):
        p1 = input("Player A, choose a number (1, 2 or 3):  ")
    p1 = rps[int(p1)-1]
    print("Player A, you choose {}.\n".format(p1))
        
    p2 = input("Player B, Choose a number (1, 2 or 3):  ")
    while not validate_input(p2):
        p2 = input("Player B, Choose a number (1, 2 or 3):  ")
    p2 = rps[int(p2)-1]
    print("Player B, you choose {}.\n".format(p2))
    
    
    print(result_game(p1, p2))
    
    


def result_game(r1, r2):
    if r1 == "Rock" and r2 == "Paper":
        return ("Paper swallows Rock")
    elif r1 == "Rock" and r2 == "Scissors":
        return ("Rock breaks Scissors")
    elif r1 == "Paper" and r2 == "Rock":
        return ("Paper swallows Rock")
    elif r1 == "Paper" and r2 == "Scissors":
        return ("Scissors cuts Paper")
    elif r1 == "Scissors" and r2 == "Rock":
        return ("Rock breaks Scissors")
    elif r1 == "Scissors" and r2 == "Paper":
        return ("Scissors cuts Paper")
    else:
        return ("DRAW!!!")

    



if __name__ == '__main__':
    game()