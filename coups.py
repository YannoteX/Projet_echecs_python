from case import *
from json import *

def deplace_piece(ch):
    '''
    Cette fonction permet de déplacer la pièce UNIQUEMENT lorsque la case de déplacement est valable.
    input : ch -> Chaine entrée par le joueur pour déplacer la pièce
            y -> Tableau de jeu

    ouput : x -> Tableau de jeu modifié
    '''

def placement_tour(posit, tableau, couleur):
    '''
    Cette fonction permet de déterminer les cases sur lesquelles peuvent aller les tours.

    input : posit -> position de la pièce (en str)
            tableau -> tableau de jeu
            couleur -> couleur de la pièce (pour le dicionnaire)
    '''
    validite=True
    check=posit
    tableauPosit=[]

    while (validite ==True):

        ligne=(ord(check[0])-1-49)*8
        colonne= ord(check[1])-1-97

        check= place_decimal(chr((colonne%8)+97), chr((ligne//8)+49))
        print(check)
        occupe=case_occupee(check, tableau)

        if (case_est_dans_tableau(check) ==True and (occupe == False or occupe[2]=='n')):
            tableauPosit.append(check)

        else:
            validite == False

    check=posit
    validite=True

    while (validite ==True):

        colonne= (ord(check[0])+1-49)*8
        ligne= ord(check[1])+1-97

        check=place_decimal(colonne, ligne)
        occupe=case_occupee(check, tableau)

        if (case_est_dans_tableau(check) ==True and (occupe == False or occupe[2]=='n')):
            tableauPosit.append(check)

        else:
            validite == False

    check=posit
    validite=True

    while (validite ==True):

        colonne= (ord(check[0])+1-49)*8
        ligne= ord(check[1])-1-97

        check= place_decimal(colonne, ligne)
        occupe=case_occupee(check, tableau)

        if (case_est_dans_tableau(check) ==True and (occupe == False or occupe[2]=='n')):
            tableauPosit.append(check)

        else:
            validite == False

    check=posit
    validite=True

    while (validite ==True):

        colonne= (ord(check[0])-1-49)*8
        ligne= ord(check[1])+1-97

        check= place_decimal(colonne, ligne)
        occupe=case_occupee(check, tableau)

        if (case_est_dans_tableau(check) ==True and (occupe == False or occupe[2]=='n')):
            tableauPosit.append(check)

        else:
            validite == False

    print(tableauPosit)

tableau=[]
for i in range (64):
    tableau.append('   ')

placement_tour('d5', tableau, 'noir')