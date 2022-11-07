import os
import random

os.system('cls')

def list_rand_numbers():
    tab = []
    tab2 = list()
    i = 1
    while i <= 100:
        n = random.randint(0, 100)
        if not tab or n not in tab2:
            tab.append(n)
            tab2.append(n)
            i += 1
        if i == 100:
            break
    return (tab)


def list_numbers():
    return [x for x in range(0, 101)]


def binary_search_random(my_list, n):
    while len(my_list) != 0:
        middle = len(my_list) // 2
        if my_list[middle] == n:
            return True
        if len(my_list) == 0:
            return False
        # If the half of the list is greater than n, then we slice the list from the half to the end
        elif my_list[middle] > n:
            my_list = my_list[:middle]
        # If the half of the list is less than n, then we slice the list from beginning until the middle (included)
        elif my_list[middle] < n:
            my_list = my_list[middle+1:]
    

if __name__ == '__main__':
    print("Binary Search Algorithm")
    s = input("Number between 1 and 100: ")
    while not s.isnumeric() or not s:
        s = input("Number between 1 and 100:")
    s = int(s)
    
    tab = list_rand_numbers()
    res = binary_search_random(tab, s)
    if res:
        print("Found!!! The index of {} is {}".format(s, tab.index(s)))
    else:
        print("Can't find the index of {}".format(s))
        