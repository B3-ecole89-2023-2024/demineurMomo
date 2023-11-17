def print_start():
    print(f'*'*50)
    print(f'*',' '*46,'*')
    print(f'*\tWelcome to this terminal Minesweeper\t *')
    print(f'*',' '*46,'*')
    print(f'*'*50)
    print("\nChoisir la difficulté :")
    print("\t1 : Facile    | 9x9   avec 10 mines")
    print("\t2 : Moyen     | 16x16 avec 40 mines")
    print("\t3 : Difficile | 30x16 avec 99 mines\n")

def print_grille(grille):
    print("\n   ", end="")
    for col in range(len(grille[0])):
        print(f'{col:2}', end=" ")
    print()
    print("  +" + "---" * len(grille[0]))

    for i, ligne in enumerate(grille):
        print(f"{i:2}| {'  '.join(ligne)}")

def game_over():
    print("Vous êtes tombé sur une mine, vous avez perdu !!!")