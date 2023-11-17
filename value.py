import random

def set_grille_player(difficulty):
    if difficulty == 1:
        x_size = 9
        y_size = 9
    elif difficulty == 2:
        x_size = 16
        y_size = 16
    elif difficulty == 3:
        x_size = 30
        y_size = 16
    grille = [['■' for _ in range(x_size)] for _ in range(y_size)]
    return grille

def set_grille_mine(difficulty):
    if difficulty == 1:
        x_size = 9
        y_size = 9
        nbr_mines = 10
    elif difficulty == 2:
        x_size = 16
        y_size = 16
        nbr_mines = 40
    elif difficulty == 3:
        x_size = 30
        y_size = 16
        nbr_mines = 99
    grille = [['0' for _ in range(x_size)] for _ in range(y_size)]
    for _ in range(nbr_mines):
        mine_placee = False
        while not mine_placee:
            x = random.randint(0, x_size - 1)
            y = random.randint(0, y_size - 1)
            if grille[y][x] != 'M':
                grille[y][x] = 'M'
                mine_placee = True

    for y in range(y_size):
        for x in range(x_size):
            if grille[y][x] != 'M':
                mines_adjacentes = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= y + i < y_size and 0 <= x + j < x_size and grille[y + i][x + j] == 'M':
                            mines_adjacentes += 1
                grille[y][x] = str(mines_adjacentes)

    return grille

def get_value(grille, coord):
    value = grille[coord[0]][coord[1]]
    return value

def set_value(grille, coord, value):
    grille[coord[0]][coord[1]] = value
    return grille

def set_case_vide(grille_player, grille_mine, coord, visited):
    y, x = coord
    visited.add(tuple(coord))

    if grille_mine[y][x] == '0':
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_y, new_x = y + i, x + j
                new_coord = (new_y, new_x)

                if 0 <= new_y < len(grille_mine) and 0 <= new_x < len(grille_mine[0]) and new_coord not in visited:
                    grille_player[new_y][new_x] = grille_mine[new_y][new_x]
                    set_case_vide(grille_player, grille_mine, new_coord, visited)

    return grille_player

def set_flag(grille, coord):
    if grille[coord[0]][coord[1]] == '■':
        grille[coord[0]][coord[1]] = '⚐'
    elif grille[coord[0]][coord[1]] == '⚐':
        grille[coord[0]][coord[1]] = '■'
    return grille

def get_nbr_mine(difficulty):
    if difficulty == 1:
        nbr_mines = 10
    elif difficulty == 2:
        nbr_mines = 40
    elif difficulty == 3:
        nbr_mines = 99
    return nbr_mines

def get_compteur_mines(grille, coord, compteur_mines):
    if grille[coord[0]][coord[1]] == '■':
        compteur_mines = compteur_mines + 1
    elif grille[coord[0]][coord[1]] == '⚐':
        compteur_mines = compteur_mines - 1
    return compteur_mines