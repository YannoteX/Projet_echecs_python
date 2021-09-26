'''
Bibliothèque pour calculer le déplacement de chaque piece
'''

from case import get_couleur
from case import dans_tableau
from case import get_piece

def calculPion(position, couleur, tableauDeJeu):
    '''
    in -> coor (position de la piece (ligne-colonne)
          couleur (couleur de la piece, True-blanc False-noir)
          tableauDeJeu
    out -> A : Tableau de déplacement
    '''
    A=[]
    ligneD=int(position/10)
    colonneD=position-ligneD*10


    if (couleur==True):                                 #pour les pions blancs
        if (ligneD==2):
            ligne=ligneD

            for i in range (2):
                ligne+=1
                if(get_piece(tableauDeJeu, (ligne*10+colonneD))!= False):
                    if (get_couleur(get_piece(tableauDeJeu, (ligne*10+colonneD))==False)):
                        A.append(ligne*10+colonneD)
                        break
                else:
                    A.append(ligne*10+colonneD)

        else:
            if (dans_tableau((ligneD+1)*10+colonneD)==True):
                A.append((ligneD+1)*10+colonneD)

        if(dans_tableau((ligneD+1)*10+(colonneD-1))==True):
            if (get_piece(tableauDeJeu, (ligneD+1)*10+(colonneD-1)) != False):                                #pour les diagonales
                if (get_couleur(get_piece(tableauDeJeu, (ligneD+1)*10+(colonneD-1))) == False):
                    A.append((ligneD+1)*10+(colonneD-1))

        elif(dans_tableau((ligneD+1)*10+(colonneD+1))==True):
            if (get_piece(tableauDeJeu, (ligneD+1)*10+(colonneD+1)) != False):
                if (get_couleur(get_piece(tableauDeJeu, (ligneD+1)*10+(colonneD+1))) == False):
                    A.append((ligneD+1)*10+(colonneD+1))



    else:                                                           #pour les pions noirs

        if (ligneD==7):
            ligne=ligneD

            for i in range (2):
                ligne-=1
                if(get_piece(tableauDeJeu, (ligne*10+colonneD))!= False):
                    if (get_couleur(get_piece(tableauDeJeu, (ligne*10+colonneD))==True)):
                        A.append(ligne*10+colonneD)
                        break
                else:
                    A.append(ligne*10+colonneD)

        else:
            if(dans_tableau((ligneD-1)*10+colonneD)==True):
                A.append((ligneD-1)*10+colonneD)

        if(dans_tableau((ligneD-1)*10+(colonneD-1))==True):
            if (get_piece(tableauDeJeu, (ligneD-1)*10+(colonneD-1)) != False):                                #pour les diagonales
                if (get_piece(tableauDeJeu, (ligneD-1)*10+(colonneD-1)) == True):
                    A.append((ligneD-1)*10+(colonneD-1))


        elif(dans_tableau((ligneD-1)*10+(colonneD+1))==True):
            if (get_piece(tableauDeJeu, (ligneD-1)*10+(colonneD+1)) != False):
                if (get_couleur(get_piece(tableauDeJeu, (ligneD-1)*10+(colonneD+1))) == True):
                    A.append((ligneD+1)*10+(colonneD+1))


    return A




def calculTour(position, couleur, tableauDeJeu):
    '''
    in -> coor (position de la piece (ligne-colonne)
          couleur (couleur de la piece, True-blanc False-noir)
          tableauDeJeu
    out -> B : Tableau de déplacement
    '''
    B=[]
    ligneD=int(position/10)
    colonneD=position-ligneD*10

    #haut

    ligne=ligneD
    stop=False

    while (stop==False):
        ligne+=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    B.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                B.append(ligne*10+colonneD)
        else:
            break

    #bas

    ligne=ligneD

    while (stop==False):
        ligne-=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu, ligne*10+colonneD))!=couleur):
                    B.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                B.append(ligne*10+colonneD)
        else:
            break

    #gauche

    colonne=colonneD

    while (stop==False):
        colonne-=1
        if(dans_tableau(ligneD*10+colonne)==True):
            if(get_piece(tableauDeJeu, ligneD*10+colonne)!=False):
                if (get_couleur(get_piece(tableauDeJeu, ligneD*10+colonne))!=couleur):
                    B.append(ligneD*10+colonne)
                    break
                else:
                    break
            else:
                B.append(ligneD*10+colonne)
        else:
            break

    #droite

    colonne=colonneD

    while (stop==False):
        colonne+=1
        if(dans_tableau(ligneD*10+colonne)==True):
            if(get_piece(tableauDeJeu, ligneD*10+colonne)!=False):
                if (get_couleur(get_piece(tableauDeJeu, ligneD*10+colonne))!=couleur):
                    B.append(ligneD*10+colonne)
                    break
                else:
                    break
            else:
                B.append(ligneD*10+colonne)
        else:
            break

    return B

def calculCavalier(position, couleur, tableauDeJeu):
    '''
    in -> coor (position de la piece (ligne-colonne)
          couleur (couleur de la piece, True-blanc False-noir)
          tableauDeJeu
    out -> C : Tableau de déplacement
    '''
    C=[]
    ligneD=int(position/10)
    colonneD=position-ligneD*10

    #g-g-h

    if(dans_tableau((ligneD+1)*10+colonneD-2)==True):
        if(get_piece(tableauDeJeu, (ligneD+1)*10+colonneD-2) != False):
            if(get_couleur(get_piece(tableauDeJeu, (ligneD+1)*10+colonneD-2))!=couleur):
                C.append((ligneD+1)*10+colonneD-2)

        else:
            C.append((ligneD+1)*10+colonneD-2)

    #g-g-b

    if(dans_tableau((ligneD-1)*10+colonneD-2)==True):
        if(get_piece(tableauDeJeu, (ligneD-1)*10+colonneD-2) != False):
            if(get_couleur(get_piece(tableauDeJeu, (ligneD-1)*10+colonneD-2))!=couleur):
                C.append((ligneD-1)*10+colonneD-2)

        else:
            C.append((ligneD-1)*10+colonneD-2)

    #d-d-h

    if(dans_tableau((ligneD+1)*10+colonneD+2)==True):
        if(get_piece(tableauDeJeu, (ligneD+1)*10+colonneD+2) != False):
            if(get_couleur(get_piece(tableauDeJeu, (ligneD+1)*10+colonneD+2))!=couleur):
                C.append((ligneD+1)*10+colonneD+2)

        else:
            C.append((ligneD+1)*10+colonneD+2)

    #d-d-b

    if(dans_tableau((ligneD-1)*10+colonneD+2)==True):
        if(get_piece(tableauDeJeu, (ligneD-1)*10+colonneD+2) != False):
            if(get_couleur(get_piece(tableauDeJeu, (ligneD-1)*10+colonneD+2))!=couleur):
                C.append((ligneD-1)*10+colonneD+2)

        else:
            C.append((ligneD-1)*10+colonneD+2)

    #g-h-h

    if(dans_tableau((ligneD+2)*10+colonneD-1)==True):
        if(get_piece(tableauDeJeu, (ligneD+2)*10+colonneD-1) != False):
            if(get_couleur(get_piece(tableauDeJeu, (ligneD+2)*10+colonneD-1))!=couleur):
                C.append((ligneD+2)*10+colonneD-1)

        else:
            C.append((ligneD+2)*10+colonneD-1)

    #g-b-b

    if(dans_tableau((ligneD-2)*10+colonneD-1)==True):
        if(get_piece(tableauDeJeu, (ligneD-2)*10+colonneD-1) != False):
            if(get_couleur(get_piece(tableauDeJeu, (ligneD-2)*10+colonneD-1))!=couleur):
                C.append((ligneD-2)*10+colonneD-1)

        else:
            C.append((ligneD-2)*10+colonneD-1)

    #d-h-h

    if(dans_tableau((ligneD+2)*10+colonneD+1)==True):
        if(get_piece(tableauDeJeu, (ligneD+2)*10+colonneD+1) != False):
            if(get_couleur(get_piece(tableauDeJeu, (ligneD+2)*10+colonneD+1))!=couleur):
                C.append((ligneD+2)*10+colonneD+1)

        else:
            C.append((ligneD+2)*10+colonneD+1)

    #d-b-b

    if(dans_tableau((ligneD-2)*10+colonneD+1)==True):
        if(get_piece(tableauDeJeu, (ligneD-2)*10+colonneD+1) != False):
            if(get_couleur(get_piece(tableauDeJeu, (ligneD-2)*10+colonneD+1))!=couleur):
                C.append((ligneD-2)*10+colonneD+1)

        else:
            C.append((ligneD-2)*10+colonneD+1)


    return C



def calculFou(position, couleur, tableauDeJeu):
    '''
    in -> coor (position de la piece (ligne-colonne)
          couleur (couleur de la piece, True-blanc False-noir)
          tableauDeJeu
    out -> D : Tableau de déplacement
    '''
    D=[]
    ligneD=int(position/10)
    colonneD=position-ligneD*10

    stop=False

    #haut-droite

    ligne=ligneD
    colonne=colonneD

    while (stop==False):
        ligne+=1
        colonne+=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    D.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                D.append(ligne*10+colonneD)
        else:
            break

    #haut-gauche

    ligne=ligneD
    colonne=colonneD

    while (stop==False):
        ligne+=1
        colonne-=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    D.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                D.append(ligne*10+colonneD)
        else:
            break

    #bas-droite

    ligne=ligneD
    colonne=colonneD

    while (stop==False):
        ligne-=1
        colonne+=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    D.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                A.append(ligne*10+colonneD)
        else:
            break

    #bas-gauche

    ligne=ligneD
    colonne=colonneD

    while (stop==False):
        ligne-=1
        colonne-=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    A.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                D.append(ligne*10+colonneD)
        else:
            break

    return D



def calculReine(position, couleur, tableauDeJeu):
    '''
    in -> coor (position de la piece (ligne-colonne)
          couleur (couleur de la piece, True-blanc False-noir)
          tableauDeJeu
    out -> E : Tableau de déplacement
    '''
    E=[]
    ligneD=int(position/10)
    colonneD=position-ligneD*10

    stop=False

    #haut-droite

    ligne=ligneD
    colonne=colonneD

    while (stop==False):
        ligne+=1
        colonne+=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    E.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                E.append(ligne*10+colonneD)
        else:
            break

    #haut-gauche

    ligne=ligneD
    colonne=colonneD

    while (stop==False):
        ligne+=1
        colonne-=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    E.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                E.append(ligne*10+colonneD)
        else:
            break

    #bas-droite

    ligne=ligneD
    colonne=colonneD

    while (stop==False):
        ligne-=1
        colonne+=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    E.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                E.append(ligne*10+colonneD)
        else:
            break

    #bas-gauche

    ligne=ligneD
    colonne=colonneD

    while (stop==False):
        ligne-=1
        colonne-=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    E.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                E.append(ligne*10+colonneD)
        else:
            break

    #haut

    ligne=ligneD

    while (stop==False):
        ligne+=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu,ligne*10+colonneD))!= couleur):
                    E.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                E.append(ligne*10+colonneD)
        else:
            break

    #bas

    ligne=ligneD

    while (stop==False):
        ligne-=1
        if(dans_tableau(ligne*10+colonneD)==True):
            if(get_piece(tableauDeJeu, ligne*10+colonneD)!=False):
                if (get_couleur(get_piece(tableauDeJeu, ligne*10+colonneD))!=couleur):
                    E.append(ligne*10+colonneD)
                    break
                else:
                    break
            else:
                E.append(ligne*10+colonneD)
        else:
            break

    #gauche

    colonne=colonneD

    while (stop==False):
        colonne-=1
        if(dans_tableau(ligneD*10+colonne)==True):
            if(get_piece(tableauDeJeu, ligneD*10+colonne)!=False):
                if (get_couleur(get_piece(tableauDeJeu, ligneD*10+colonne))!=couleur):
                    E.append(ligneD*10+colonne)
                    break
                else:
                    break
            else:
                E.append(ligneD*10+colonne)
        else:
            break

    #droite

    colonne=colonneD

    while (stop==False):
        colonne+=1
        if(dans_tableau(ligneD*10+colonne)==True):
            if(get_piece(tableauDeJeu, ligneD*10+colonne)!=False):
                if (get_couleur(get_piece(tableauDeJeu, ligneD*10+colonne))!=couleur):
                    E.append(ligneD*10+colonne)
                    break
                else:
                    break
            else:
                E.append(ligneD*10+colonne)
        else:
            break

    return E


def calculRoi(position):
    return [77,88,99]



def calculDeplacement(coor, piece, tableauDeJeu):
    '''
    Calcul les déplacements de la piece en paramètre
    in : coor -> bon on sais
         piece -> str (la piece en question)
         tableauDeJeu
    out : tab -> tableau de déplacement
    '''
    couleur=get_couleur(piece)
    tab=[]

    if (piece[0]=="p"):
        tab=calculPion(coor, couleur, tableauDeJeu)
    elif (piece[0]=="t"):
        tab=calculTour(coor, couleur, tableauDeJeu)
    elif (piece[0]=="c"):
        tab=calculCavalier(coor, couleur, tableauDeJeu)
    elif(piece[0]=="f"):
        tab=calculFou(coor, couleur, tableauDeJeu)
    elif(piece[0]=="r"):
        tab=calculReine(coor, couleur, tableauDeJeu)
    else:
        tab=[]

    return tab



