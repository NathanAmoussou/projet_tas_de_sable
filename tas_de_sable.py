########################################
# import des librairies

from tkinter import *
import random as rd


########################################
# CONSTANTES

TAILLE = 100 # taille de la grille carrée
CENTRE = 10000 # valeur de la case au centre de la grille


########################################
# variables globales

couleurs = {0:'snow', 1:'lemon chiffon', 2:'navajo white', 3:'PeachPuff4'} # couleurs des cases en fonction de leurs valeurs
x, y, d = 10, 10, 5 # taille des cases (en gros)
grille = [[0]*TAILLE for i in range(TAILLE)] # grille sous forme d'un tableau de valeurs
grille[TAILLE // 2][TAILLE // 2] = CENTRE # affectation de CENTRE au centre de la grille


########################################
# def des fonctions

def configuration_courante(t=100):
    global TAILLE, grille, x, y
    TAILLE = t
    grille = [[0]*TAILLE for i in range(TAILLE)]
    for ligne in grille:
        for valeur in ligne:
            clr = couleurs[valeur]
            canevas.create_rectangle(x, y, x+d, y+d, outline='black', fill=clr)
            x += 5
        x = 10
        y += 5

def abelian():
    global grille
    while True:
        found = False
        for r in range(TAILLE):
            for c in range(TAILLE):
                if grille[r][c] > 3:
                    distribute(grille[r][c], r, c)
                    found = True
        if not found:
            return

def distribute(nbr, ligne, col):
    global grille
    qty, remain = divmod(nbr, 4)
    grille[ligne][col] = remain
    try:
        for r, c in [(ligne+1, col), (ligne-1, col), (ligne, col+1), (ligne, col-1)]:
            grille[r][c] += qty
    except IndexError:
        print("pd")
    return

def maj_config_courante():
    global TAILLE, grille, x, y
    for ligne in grille:
        for valeur in ligne:
            clr = couleurs[valeur]
            canevas.create_rectangle(x, y, x+d, y+d, outline='black', fill=clr)
            x += 5
        x = 10
        y += 5


########################################
# programme principal

racine = Tk()
racine.title('Tas de sable')
racine.geometry('700x700+100+50')
canevas = Canvas(racine, bg='white')
canevas.pack(fill=BOTH, expand=1)
abelian()
maj_config_courante()
mainloop()
