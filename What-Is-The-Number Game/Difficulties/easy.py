import os
from random import randint

# Import files modules
from Difficulties.check_inputs import checkInput, isGuessed


def e_play_game():
    os.system('cls')
    print('\n')
    
    while True:
        mysteryNumber = randint(1, 100)
        guesses = 5
        while guesses > 0:
            nbr = checkInput(input("Guess the mystery number: "))
            while nbr == False:
                nbr = checkInput(input("Guess the mystery number: "))
            
            if isGuessed(nbr, mysteryNumber):
                print("Bravooooo!!! The number was {}\n\n".format(mysteryNumber))
                c = True
                break
            else:
                if nbr < mysteryNumber:
                    print("\n-- More --\n")
                else:
                    print("\n-- Less --\n")
                guesses -= 1
                if guesses == 0:
                    c = False
                    break
                print("{} attempts left".format(guesses))
        if c == True:
            break
        else:
            print("You lost!!! The number was {}\n\n".format(mysteryNumber))


def print_board(a, b):
    print()
    print("Players          Points")
    print("-------          -------\n")
    for c in range(len(a)):
        print(f"Player {a[c]}          {b[c]}\n")
    return 0


def revenge():
    answer = input("Do you want to play a new game? (y/n): ")
    while answer != 'y' and answer != 'n':
        answer = input("Do you want to play a new game? (y/n): ")
    if answer == 'n':
        return False
    return True


def guessNumber(player):
    os.system('cls')
    print('\n')
    
    while True:
        mysteryNumber = randint(1, 100)
        guesses = 5
        while guesses > 0:
            nbr = checkInput(input("Player {}, guess the mystery number: ".format(player)))
            while nbr == False:
                nbr = checkInput(input("Player {}, guess the mystery number: ".format(player)))
            
            if isGuessed(nbr, mysteryNumber):
                print("\n\n----------------------- Great!!! The number was {} -----------------------\n\n".format(mysteryNumber))
                c = True
                break
            else:
                if nbr < mysteryNumber:
                    print("\n-- More --\n")
                else:
                    print("\n-- Less --\n")
                guesses -= 1
                if guesses == 0:
                    c = False
                    break
                print("{} attempts left\n".format(guesses))
        if c == True:
            return 1
        else:
            print("You lost!!! The number was {}\n\n".format(mysteryNumber))
            os.system("pause")
            return 0


def e_pvp_game():
    os.system('cls')
    print('\n')
    
    p = checkInput(input("Type the number of players: "))
    while p == False or int(p) <= 1:
        p = input("Type the number of players (More than 1): ")
    
    new_game = 1
    players = list(range(1, p+1))
    points = [0 for _ in range(len(players))]
    
    while new_game:
        print_board(players, points)
        os.system('pause')
        
        i = 0
        while i < len(players):
            if guessNumber(players[i]):
                points[i] += 1
            if 5 in points:
                win = True
                break
            if i == len(players)-1:
                i = 0
                print_board(players, points)
                os.system('pause')
            else:
                i += 1
                print_board(players, points)
                os.system('pause')

        if win:
            winner_index = points.index(5)
            winner = players[winner_index]
            print("\n\n" + "\t"*4 + "######################################### Congratulations #########################################\n")
            print(f"######################################### The winner is {winner} #########################################\n")
            print("\t"*4 + "######################################### Congratulations #########################################\n\n")
            
        if revenge() == False:
            new_game = 0
        else:
            players = list(range(1, p+1))
            points = [0 for _ in range(len(players))]


def guessNumber_com():
    os.system('cls')
    print('\n')
    
    while True:
        mysteryNumber = randint(1, 100)
        guesses = 5
        minVal, maxVal = 1, 100
        while guesses > 0:
            nbr = randint(minVal, maxVal)
            print(f"Min = {minVal}, Max = {maxVal}")
            
            if isGuessed(nbr, mysteryNumber):
                print("\n\n----------------------- Great!!! The number was {} -----------------------\n\n".format(mysteryNumber))
                c = True
                break
            else:
                if nbr < mysteryNumber:
                    print(f"{nbr}")
                    print("\n-- More --\n")
                    minVal = nbr + 1
                else:
                    print(f"{nbr}")
                    print("\n-- Less --\n")
                    maxVal = nbr - 1
                guesses -= 1
                if guesses == 0:
                    c = False
                    break
                print("{} attempts left\n".format(guesses))
                os.system('pause')
        if c == True:
            return 1
        else:
            print("You lost!!! The number was {}\n\n".format(mysteryNumber))
            os.system("pause")
            return 0


def e_pvcom_game():
    os.system('cls')
    print('\n')
    
    new_game = 1
    p = ["Me", "COM"]
    m = [0, 0]
    
    while new_game:
        print_board(p, m)
        os.system('pause')
        
        i = 0
        while i < len(p):
            if p[i] == "Me":
                if guessNumber(p[i]):
                    m[i] += 1
            elif p[i] == "COM":
                if guessNumber_com():
                    m[i] += 1
                
            if 5 in m:
                win = True
                break
            if i == len(p)-1:
                i = 0
                print_board(p, m)
                os.system('pause')
            else:
                i += 1
                print_board(p, m)
                os.system('pause')

        if win:
            winner_index = m.index(5)
            winner = p[winner_index]
            print("\n\n" + "\t"*4 + "######################################### Congratulations #########################################\n")
            print("\t"*4 + "######################################### The winner is {winner} #########################################\n".format(winner))
            print("\t"*4 + "######################################### Congratulations #########################################\n\n")
            
        if revenge() == False:
            new_game = 0
        else:
            m = [0, 0]
    
        
    