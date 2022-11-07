import os

os.chdir(r"C:/Users/ukisu\Documents/Beginner-Projects-Python/Contact Book")
tab = []
with open('MyContacts.txt', 'r') as fp:
    stacktest = [line.strip() for line in fp.readlines()]
    print(stacktest)