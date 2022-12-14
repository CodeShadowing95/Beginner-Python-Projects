""" Programme qui effectue le jeu du Morpion """
from player import Joueur
import os

class Morpion:
    
    def __init__(self):
        """Constructeur

        Args:
            tableau (list(list())): tableau sur lequel le jeu se déroulera
            playerO (str): 
        """
        self.tableau = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        
        
    def afficher_tableau(self):
        os.system('cls')
        print('\n')
        print("\t"*3 + "##############################################################################\n")
        print("\t"*3 + "############################## Le jeu du Morpion #############################\n")
        print("\t"*3 + "##############################################################################\n\n")
        for i in range(len(self.tableau)):
            print("\t"*7, end="")
            for j in range(len(self.tableau)):
                if j == 2:
                    print(self.tableau[i][j], end=" ")
                else:
                    print(" " + self.tableau[i][j], end=" ")
                    
                if j != len(self.tableau)-1:
                    print (" | ", end=" ", sep=" ")
            if i != len(self.tableau)-1:
                print ("\n" + "\t"*7 + "-"*4 + "+" + "-"*6 + "+" + "-"*4)
        print("\n")
    
    
    
    def redemarrer(self):
        self.__init__()
        self.afficher_tableau()
    
    
    
    def testTableau(self, joueur):
        # Tests des différentes possibilités de gagner le jeu
        
        """ Vérifier verticalement """
        for i in range(0, 3):
            getScore = []
            for j in range(0, 3):
                if self.tableau[i][j] == joueur:
                    getScore.append((self.tableau[i][j]))
            if len(getScore) == 3:
                return joueur
        
        """ Vérifier horizontalement """
        for i in range(0, 3):
            getScore = []
            for j in range(0, 3):
                if self.tableau[j][i] == joueur:
                    getScore.append((self.tableau[j][i]))
            if len(getScore) == 3:
                return joueur
        
        """ Vérifier les diagonales 1 et 2 """
        getScore = []
        for i in range(0, 3):
            if self.tableau[i][i] == joueur:
                getScore.append((self.tableau[i][i]))
            if len(getScore) == 3:
                return joueur
        
        getScore = []
        for i in range(0, 3):
            if self.tableau[2-i][i] == joueur:
                getScore.append((self.tableau[2-i][i]))
            if len(getScore) == 3:
                return joueur
        
        """ On teste s'il y a encore des emplacements du tableau à compléter """
        c = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.tableau[i][j] != " ":
                    c += 1
                    
        if c == 8:
            if len(getScore) == 3:
                return joueur
            # return True
        if c == 9:
            if len(getScore) == 3:
                return joueur
            return True
        return False
    
    
    
    def saisieValide(self, joueur):
        print("\t"*3 + ">>>> Tour du joueur {}. Entrez un nombre de 1 à 9.".format(joueur))
        nombre = input("\t"*3 + ">>>> ")
        while not nombre.isnumeric() or int(nombre) not in [i for i in range(1,10)]:
            print()
            print("\t"*3 + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Entrez uniquement des chiffres compris entre 1 et 9 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            nombre = input("\t"*3 + ">>>> ")
            
        return int(nombre)
        
        
        
    def tourJoueur(self, joueur):
        p = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        
        print()
        position = self.saisieValide(joueur)
        
        for i in p:
            if i == position:
                if self.tableau[p[i][0]][p[i][1]] == ' ':
                    self.tableau[p[i][0]][p[i][1]] = joueur
                    
                else:
                    print("\n")
                    print("\t"*3 + "--------------------- Attention:  Zone déjà occupée. Choisissez un emplacement vide ---------------------\n\n")
                    self.tourJoueur(joueur)
        self.afficher_tableau()
    
    
    
    def gagnerJeu(self, joueur):
        wins = [
            # De haut en bas
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # De gauche à droite
            [(0, 0), (1, 0), (2, 0)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Diagonales
            [(2, 0), (1, 1,), (0, 2)],
            [(0, 0), (1, 1,), (2, 2)]
        ]
        
        pass
        
        
    
    def tictactoe(self):
        self.afficher_tableau()
        endOfGame= False
        
        while endOfGame is False:
            j1 = Joueur.joueur1
            self.tourJoueur(j1)
            res = self.testTableau(j1)
            if res == j1:
                print("\n\n\n" + "\t"*3 + "++++++++++++++++++++++++++++++++++++ Félicitations ++++++++++++++++++++++++++++++++++++\n")
                print("\t"*3 + "++++++++++++++++++++++++++++++++ Le joueur {} a gagné ++++++++++++++++++++++++++++++++++\n".format(j1))
                print("\t"*3 + "++++++++++++++++++++++++++++++++++++ Félicitations ++++++++++++++++++++++++++++++++++++\n\n")
                os.system("pause")
                self.redemarrer()
                # break
            elif res == True:
                print("\n\n################################## Match nul!!! ##################################")
                os.system("pause")
                self.redemarrer()
            
            
            j2 = Joueur.joueur2
            self.tourJoueur(j2)
            res = self.testTableau(j2)
            if res == j2:
                print("\n\n\n" + "\t"*3 + "++++++++++++++++++++++++++++++++++++ Félicitations ++++++++++++++++++++++++++++++++++++\n")
                print("\t"*3 + "++++++++++++++++++++++++++++++++ Le joueur {} a gagné ++++++++++++++++++++++++++++++++++\n".format(j2))
                print("\t"*3 + "++++++++++++++++++++++++++++++++++++ Félicitations ++++++++++++++++++++++++++++++++++++\n\n")
                os.system("pause")
                self.redemarrer()
            elif res == True:
                print("\n\n################################## Match nul!!! ##################################")
                os.system("pause")
                self.redemarrer()
    
    


m = Morpion()
# m.afficher_tableau()
m.tictactoe()

