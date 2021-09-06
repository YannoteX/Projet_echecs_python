from case import *
from json import *

def deplace_piece(ch):
    '''
    Cette fonction permet de déplacer la pièce UNIQUEMENT lorsque la case de déplacement est valable.
    input : ch -> Chaine entrée par le joueur pour déplacer la pièce
            y -> Tableau de jeu

    ouput : x -> Tableau de jeu modifié
    '''

def placement_pion(posit, tableau, couleur):
    '''
    Cette fonction permet de déterminer les cases sur lesquelles peuvent aller les tours.

    input : posit -> position de la pièce (en str)
            tableau -> tableau de jeu
            couleur -> couleur de la pièce (pour le dicionnaire)
    '''

    possibilites=[]


    if (couleur == "blanc"):

        if(case_est_dans_tableau( place_str( place_decimal(posit)+8)) == True):

            possibilites.append( place_str( place_decimal(posit)+8))

    else :

        if(case_est_dans_tableau( place_str( place_decimal(posit)-8)) == True):

            possibilites.append( place_str( place_decimal(posit)-8))