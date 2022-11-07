import os

# Import files modules
from Difficulties import easy, medium, hard


# Fonction qui demande le mode de jeu: Mode Joueur vs Joueur ou Mode Joueur vs Machine
def selectMode():
    os.system('cls')
    print('\n')
    print("\t"*3 + "################################################################################\n")
    print("\t"*3 + "############################## What's the number ? #############################\n")
    print("\t"*3 + "################################################################################\n\n")
    print("1- One player\n")
    print("2- Player vs Player\n")
    print("3- Player vs COM\n")
    m = input("Select a game mode: ")
    while not m.isnumeric() or int(m) not in range(1, 4):
        m = input("Select a game mode (between 1 and 3): ")
    return int(m)



# Fonction qui demande de sélectionner le niveau de difficulté du jeu
def selectDifficulty():
    os.system('cls')
    print('\n')
    print("1- Easy (1 - 100)\n")
    print("2- Medium (1 - 1000)\n")
    print("3- Hard (1 - 10000)\n\n")
    d = input("Select a level of difficulty: ")
    while not d.isnumeric() or int(d) not in range(1, 4):
        d = input("Select a level of difficulty (between 1 and 3): ")
    return int(d)
    


# Le jeu proprement dit
def game():
    m = selectMode()
    d = selectDifficulty()
    
    if d == 1:
        if m == 1:
            easy.e_play_game()
        if m == 2:
            easy.e_pvp_game()
        if m == 3:
            easy.e_pvcom_game()
    elif d == 2:
        if m == 1:
            medium.m_play_game()
        if m == 2:
            medium.m_pvp_game()
        if m == 3:
            medium.m_pvcom_game()
    elif d == 3:
        if m == 1:
            hard.h_play_game()
        if m == 2:
            hard.h_pvp_game()
        if m == 3:
            hard.h_pvcom_game()



if __name__ == "__main__":
    game()