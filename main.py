import affichage
import input
import value
import time

affichage.print_start()
difficulty = input.get_difficulty()
compteur_mines = value.get_nbr_mine(difficulty)
premier_coup = True
grille_player = value.set_grille_player(difficulty)
affichage.print_grille(grille_player)
while True:
    if premier_coup == True:
        coord = input.get_coord(difficulty)
        case = ''
        while case != '0':
            grille_mine = value.set_grille_mine(difficulty)
            case = value.get_value(grille_mine, coord)
        value.set_value(grille_player, coord, case)
        grille_player = value.set_case_vide(grille_player, grille_mine, coord, set())
        affichage.print_grille(grille_player)
        premier_coup = False
        dirname = input.set_dir(grille_mine)
        timer = time.time()
    else:
        action = input.get_action()
        if action == 'U':
            coord = input.get_coord(difficulty)
            case = value.get_value(grille_mine, coord)
            if case == 'M':
                affichage.game_over()
                exit()
            elif case == '0':
                grille_player = value.set_case_vide(grille_player, grille_mine, coord, set())
            value.set_value(grille_player, coord, case)
            affichage.print_grille(grille_player)
        elif action == 'F':
            coord = input.get_coord(difficulty, True)
            value.set_flag(grille_player, coord)
            affichage.print_grille(grille_player)
            if value.get_value(grille_mine, coord) == 'M':
                compteur_mines = value.get_compteur_mines(grille_player, coord, compteur_mines)
        if compteur_mines == 0:
            input.set_score_win(dirname, timer)
            exit()