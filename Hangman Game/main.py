from random import randint
import os, getpass



def expand_word(s):
    rand_idx, text_length, uniq = 0, len(s), []
    guess_str = ['']*text_length
    for _ in range(3):
        rand_idx = randint(0, text_length - 1)
        while rand_idx in uniq:
            rand_idx = randint(0, text_length)
        guess_str[rand_idx] = list(s)[rand_idx]
        uniq.append(rand_idx)
    
    return guess_str
    
    

def print_status(text):
    for j in range(len(text)):
        if text[j] == '':
            print(" _ ", end='')
        else:
            print(f" {text[j]} ", end='')
    print("\n")
    
    return text



def print_board(tab_players, tab_points):
    os.system('cls')
    print("\n\n-+----------+----+-")
    print(f" | Joueur {tab_players[0]} |  {tab_points[0]} | ")
    print("-+----------+----+-")
    print(f" | Joueur {tab_players[1]} |  {tab_points[1]} | ")
    print("-+----------+----+-\n\n")
    
    
    


nobody_won = True
players = [1, 2]
points = [0, 0]
p1 = 0
p2 = 1
attempts = 5

while nobody_won:
    print_board(players, points)
    
    # Check if the word exists in the file dictionary of words
    os.chdir(r"C:/Users/ukisu\Documents/Beginner-Projects-Python/Hangman Game")
    fp = open('words_library.txt', 'r')
    words = fp.readlines()
    fp.close()
    mystery_word = getpass.getpass(prompt=f"Player {players[p1]}, write the word to guess: ")
    # mystery_word = mystery_word.lower()
    while (type(mystery_word) != str or mystery_word in ",;:!ù*^$?./§%µ£¨=)àç_è-('\"é&²+°0987654321¤}]@^\`|[{#~") or mystery_word+'\n' not in words:
        mystery_word = getpass.getpass(prompt="Write a correct word: ")
    mystery_word = mystery_word.lower()

    
    os.system('cls')
    tab1 = expand_word(mystery_word)
    notFound = True
    
    while notFound:
        tab1 = print_status(tab1)
        c = 0
        
        inputNextPlayer = input(f"Player {players[p2]}, what's the word: ")
        while len(inputNextPlayer) != len(mystery_word):
            inputNextPlayer = input("Hint: Write a word of {:d} letters: ".format(len(mystery_word)))
        tab2 = list(inputNextPlayer)
        
        for i in range(len(tab2)):
            if tab2[i] == list(mystery_word)[i]:
                if tab1[i] == '':
                    tab1[i] = tab2[i]
                c += 1
        if c == len(mystery_word):
            print(f"++++++++++++++++++++++++++++++++++++ Bravo Player {players[p2]}, You found the word!!!! ++++++++++++++++++++++++++++++++++++")
            os.system("pause")
            points[p2] += 1
            if points[p2] == 3:
                nobody_won = False
                break
            p1, p2 = p2, p1
            tab1, tab2 = [], []
            attempts = 5
            break
        else:
            attempts -= 1
            print(f"\n***** {attempts} attempts left *****\n\n")
            if attempts == 0:
                print(f"-------------------------------- Sorry Player {players[p2]}!!! You have no more attempts left!!! --------------------------------")
                os.system("pause")
                tab1, tab2 = [], []
                attempts = 5
                p1, p2 = p2, p1
                break
            
                

if not nobody_won:
    print("\t"*3 + "####################################### Congratulations #######################################")
    print("\t"*3 + f"Player {players[p2]}, you won")
    print("\t"*3 + "####################################### Congratulations #######################################\n\n")
    
    
    