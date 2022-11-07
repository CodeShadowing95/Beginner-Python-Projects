from random import randint, choice
import os

# game_title = __import__('game_title').game_title

# Display the title of the game
# game_title()

# Get the word from the words' library
def load_word():
    os.chdir(r"C:/Users/ukisu\Documents/Beginner-Projects-Python/Mystery Word Game")
    fp = open('words_library.txt', 'r')
    words = fp.readlines()
    word = choice(words)
    fp.close()
    
    return word


# String to guess
str_text = load_word()
# str_text = "refrigerator\n"
text_length = len(str_text)-1
# text_length = len(str_text)

guess_str, rand_idx, length_str, not_found = [''] * text_length, 0, 0, True
count, uniq = 0, -1

# show the letters at 2 random positions from the string to guess
for i in range(3):
    rand_idx = randint(0, text_length - 1)
    while rand_idx == uniq:
        rand_idx = randint(0, text_length)
    guess_str[rand_idx] = str_text[rand_idx]
    uniq = rand_idx

# Guess the string, until the entire word is found
print("************************ What's the mystery word ? ************************\n")
while not_found:
    print("Status: ", end="")
    for j in range(len(guess_str)):
        if guess_str[j] == '':
            print(" _ ", end='')
        else:
            print(f" {guess_str[j]} ", end='')
    print("\n")
    
    # Type the word to guess
    guess_word = input("Type the word to guess: ")
    # while the length of the word is different from the length of the input string, repeat the process
    while len(guess_word) != len(guess_str):
        guess_word = input("Hint: Type a word of {:d} letters: ".format(len(guess_str)))
    
    # Turn the input string into a list of letters
    word_list = list(guess_word)
    
    # For each correct letter from the string str_text, complete the letter in the string guess_str
    for k in range(len(word_list)):
        if word_list[k] == str_text[k]:
            guess_str[k] = word_list[k]
            guess_str_len = len([x for x in guess_str if x != ''])
    
    # If the mystery word has been found, exit the loop
    if guess_str_len == text_length:
        print("\n" * 3)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("The mystery word has been found. It was {}.".format(str_text))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        not_found = False
        break
