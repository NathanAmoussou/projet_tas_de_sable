########################################
# groupe MI 2
# Kamila DIMIA
# Marlone BERTUIT
# Nathan AMOUSSOU
# https://github.com/uvsqNathanAmoussou/projet_tas_de_sable
########################################

########################################
# import des librairies

from distutils.command.config import config
from tkinter import *
import random as rd


########################################
# CONSTANTES

TAILLE = 100 # taille de la grille carrée
CENTRE = 10000 # valeur de la case au centre de la grille


########################################
# variables globales

config_courante = []
x, y, d = 10, 10, 5 # taille des cases (en gros)
couleurs = {0:'snow', 1:'lemon chiffon', 2:'navajo white', 3:'PeachPuff4'} # couleurs des cases en fonction de leurs valeurs
grille_de_rectangles = []


########################################
# def des fonctions

def init_grille():
    """Crée la configuration courante vide de grains de sable (donc une liste à deux dimensions de 0).
    Crée une première liste de rectangles et les affiche dans le canevas (les rectangles sont du coup accessible, voir # exemple)."""
    global config_courante, grille_de_rectangles, x, y
    # on réinitialise le bordel
    config_courante = []
    grille_de_rectangles = []
    # on crée les listes vides
    config_courante = [[0]*TAILLE for i in range(TAILLE)]
    grille_de_rectangles = [[0]*TAILLE for i in range(TAILLE)]
    # on remplit et affiche la grille de rectangle
    for i in range(len(grille_de_rectangles)):
        for j in range(len(grille_de_rectangles)):
            rectangle = canevas.create_rectangle(x, y, x+d, y+d, outline='black')
            grille_de_rectangles[i][j] = rectangle
            x += 5
        x = 10
        y += 5
    # canevas.itemconfig(grille_de_rectangles[3][7], fill='green') # exemple

def maj_grille():
    """Met à jour la couleur des rectangles en fonction des valeurs de la configuration courante."""
    global grille_de_rectangles
    for lignenum, ligne in enumerate(config_courante):
        for colnum, valeur in enumerate(ligne):
            clr = couleurs[valeur]
            canevas.itemconfig(grille_de_rectangles[lignenum][colnum], fill=clr)


########################################
# programme principal

# définition des widgets
racine = Tk()
racine.title('Tas de sable')
racine.geometry('700x700+100+50')
canevas = Canvas(racine, bg='white')
bouton_config_aleatoire = Button(racine, text='Configuration aléatoire')

# placement des widgets
canevas.pack(fill=BOTH, expand=1)
bouton_config_aleatoire.pack()

# boucle principale
init_grille()
maj_grille()
mainloop()
