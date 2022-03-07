import random
taille = 7
centre = 17

grille = [[0]*taille for i in range(taille)]

def afficher():
    for ligne in grille:
        print(' '.join(str(x) for x in ligne))
    print()

grille[taille // 2][taille // 2] = centre

# grille[0][0] = centre

afficher()


def abelian():
    while True:
        found = False
        for r in range(taille):
            for c in range(taille):
                if grille[r][c] > 3:
                    distribute(grille[r][c], r, c)
                    found = True
        if not found:
            return


def distribute(nbr, ligne, col):
        qty, remain = divmod(nbr, 4)
        grille[ligne][col] = remain
        try:
            for r, c in [(ligne+1, col), (ligne-1, col), (ligne, col+1), (ligne, col-1)]:
                grille[r][c] += qty
        except IndexError:
            print("pd")
        return


def distribute2_the_return(nbr, ligne, col):
        qty, remain = divmod(nbr, 4)
        grille[ligne][col] = remain
        
        return


abelian()
afficher()

grille = [[0]*taille for i in range(taille)]
for x in range(taille):
    for y in range(taille):
        grille[x][y] = random.randint(1, 3)

afficher()
abelian()
afficher()