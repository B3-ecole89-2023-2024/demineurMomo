import os
import time

def get_difficulty():
    difficulty = input("1/2/3 : ")
    try:
        difficulty = int(difficulty)
        if difficulty in {1, 2, 3}:
            return difficulty
        else:
            return get_difficulty()
    except ValueError:
        return get_difficulty()
        
def get_coord(difficulty, mine = False):
    if difficulty == 1:
        x_size = 9
        y_size = 9
    elif difficulty == 2:
        x_size = 16
        y_size = 16
    elif difficulty == 3:
        x_size = 30
        y_size = 16
    x = x_size
    y = y_size
    while (x >= x_size) or (y >= y_size):
        if mine == True:
            print("Choisir les coordonnées du drapeau à placer :")
        else:
            print("Choisir les coordonnées de la case à retourner :")
        x = input("x : ")
        y = input("y : ")
        try:
            x = int(x)
            y = int(y)
            if x >= x_size or y >= y_size:
                return get_coord(difficulty, mine)
            coord = [y, x]
            return coord
        except:
            return get_coord(difficulty, mine)

def get_action():
    action = input("Voulez-vous découvrir une case (U) ou capturer une mine (F)\n")
    return action

def read_nbr_dir():
    liste_elements = os.listdir('saves')

    liste_dossiers = [element for element in liste_elements if os.path.isdir(os.path.join('saves', element))]

    return len(liste_dossiers)

def make_dir(dirname):
    parent_dir = "saves"
    path = os.path.join(parent_dir, dirname)  
    os.mkdir(path)
    return path

def set_dir(grille):
    nbr = read_nbr_dir()
    dirname = make_dir(str(nbr))
    with open(dirname + "/grille.map", "w") as grille_file:
        for line in grille:
            grille_file.write(",".join(line) + "\n")
    return dirname

def set_score_win(dirname, timer):
    temps_ecoule = round(time.time() - timer, 2)
    heures, reste = divmod(temps_ecoule, 3600)
    minutes, secondes = divmod(reste, 60)
    heures = int(heures)
    minutes = int(minutes)
    secondes = int(secondes)
    print(f"Temps écoulé : {heures:02}:{minutes:02}:{secondes:02}")
    print("Bravo vous avez découvert toutes les mines")
    name = input("Entrez votre nom : ")
    save_file = dirname + '/' + name + ".txt"
    with open(save_file, "w") as txt_file:
        txt_file.write("".join(f'{heures:02}:{minutes:02}:{secondes:02}'))
