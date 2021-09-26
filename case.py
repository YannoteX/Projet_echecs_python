'''
Fonctionnalité pour les cases.
'''

import json

def get_position(coor):
    '''
    Transforme une coordonée (ex : 56, ligne-colonne) en valeur entière dans le tableau
    in : coor -> int(ligne-colonne)
    out : posit -> int (>=0 && <64)
    '''
    ligne=int(coor/10)
    colonne=coor-ligne*10

    return (ligne-1)*8+colonne-1




def get_coor(posit):
    '''
    Transforme une position (ex : 49) en coordonée (ligne-colonne)
    in : posit -> int (>=0 && <64)
    out : coor -> int(ligne-colonne)
    '''
    ligne=int(posit/8)
    colonne=posit-ligne*8

    return (ligne+1)*10+colonne+1




def get_piece(tableauDeJeu, coor):
    '''
    Trouve la piece par coordonée de case (ou pas)
    in : coor -> int(ligne-colonne)
         tableauDeJeu -> :)
    out : str (piece) ou False
    '''

    position=get_position(coor)

    if (tableauDeJeu[position].strip()!= ""):
        return tableauDeJeu[position].strip()

    return False



def get_couleur(piece):
    '''
    Renvoie la couleur de la piece (True-blanc False-noir)
    in -> Piece à vérifier
    out -> couleur (boolean)
    '''
    for i in range (len(piece)):
        if (piece[i]=="b"):
            return True
        elif(piece[i]=="n"):
            return False



def dans_tableau(coor):
    '''
    Vérifie si la case en paramètre est dans le tableau
    in -> coor : coordonée de la case
    out -> True ou False
    '''

    ligne=int(coor/10)
    colonne=coor-ligne*10

    if(ligne>0 and ligne <9 and colonne >0 and colonne <9):
        return True

    return False


