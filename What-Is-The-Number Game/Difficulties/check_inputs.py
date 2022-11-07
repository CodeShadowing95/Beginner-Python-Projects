# Fonction qui teste si l'entrée user est un nombre
def checkInput(user_input):
    if not user_input.isnumeric():
        return False
    return int(user_input)



# Fonction qui retourne True si le nombre est trouvé et False sinon
def isGuessed(user_input, nbr_to_guess):
    if user_input == nbr_to_guess:
        return True
    return False
