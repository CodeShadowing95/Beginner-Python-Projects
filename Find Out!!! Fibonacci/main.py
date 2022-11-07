import os
import sys
sys.path.append('C:/Users/ukisu/Documents/Beginner-Projects-Python/')
# To import a module from a different folder
from ci import check_input


os.system('cls')

def is_in_Fibonacci_suite(n):
    a = 0
    b = 1
    if n == 0 or n == 1:
        return True
    while 1:
        # a, b = b, a+b
        temp = a
        a = b
        b += temp
        if b == n:
            return True
        elif b > n:
            return False


if __name__ == '__main__':
    p = input("Type a number: ")
    while not check_input.validate_input(p):
        p = input("Type a correct number: ")
    p = int(p)
    res = is_in_Fibonacci_suite(p)
    if res:
        print("{} in the Fibonacci sequence.".format(p))
    else:
        print("{} not in the Fibonacci sequence.".format(p))
        
        