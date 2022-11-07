import os
from random import randint

if __name__ == '__main__':
    os.system("cls")

    c = True
    tab = []
    while c:
        n = randint(1, 6)
        if n == 1:
            print("-------")
            print("       ")
            print("   0   ")
            print("       ")
            print("-------")
        if n == 2:
            print("-------")
            print("      0")
            print("       ")
            print("0      ")
            print("-------")
        if n == 3:
            print("-------")
            print("      0")
            print("   0   ")
            print("0      ")
            print("-------")
        if n == 4:
            print("-------")
            print("0     0")
            print("       ")
            print("0     0")
            print("-------")
        if n == 5:
            print("-------")
            print("0     0")
            print("   0   ")
            print("0     0")
            print("-------")
        if n == 6:
            print("-------")
            print("0  0  0")
            print("       ")
            print("0  0  0")
            print("-------")
        # print("The dice displays: {}".format(n))
        print()
        new_turn = input("Rolling dice again?(y/n) ")
        y = ["y", "Y", "Yes", "yes"]
        n = ["n", "N", "No", "no"]
        while not isinstance(new_turn, str) or (new_turn not in y and new_turn not in n):
            print("Answer by yes or no")
            new_turn = input("Rolling dice again?(y/n) ")
        if new_turn in n:
            c = False
