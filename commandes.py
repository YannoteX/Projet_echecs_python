'''
répertorie et execute toutes les commandes entrées par les joueurs
'''

from affichage import *
from case import *
from deplacements import *
from gestionFichiers import *
import json

def cmd_tour(cmd, couleur, tableauDeJeu):
    '''
    in : cmd -> int
         couleur -> boolean (couleur du joueur True-blanc False-noir)
         tableauDeJeu -> c'est dans le nom
    out : tableauDeJeu, False sinon
    '''
    if(cmd >=1111 and cmd<=8888):
        caseD=int(cmd/100)
        caseA=cmd-caseD*100

        if(dans_tableau(caseD)==True and dans_tableau(caseA)==True):
            if(get_piece(tableauDeJeu, caseD) != False):
                if(get_couleur(get_piece(tableauDeJeu, caseD))==couleur):

                    nomPieceD=get_piece(tableauDeJeu, caseD)
                    path=os.getcwd()+'\pieces\\'+nomPieceD+'.json'
                    f=open(path,'r')
                    pieceD=json.load(f)
                    f.close()


                    for i in range (len(pieceD["allowed"])):
                        if (pieceD["allowed"][i]==caseA):
                            if(get_piece(tableauDeJeu, caseA)!=False):
                                if(get_couleur(get_piece(tableauDeJeu, caseA))!=couleur):

                                    nomPieceA=get_piece(tableauDeJeu, caseA)
                                    path=os.getcwd()+'\pieces\\'+nomPieceA+'.json'
                                    f=open(path,'r')
                                    pieceA=json.load(f)
                                    f.close()

                                    suppr_piece(nomPieceA, pieceA)

                            tableauDeJeu[get_position(caseA)]=tableauDeJeu[get_position(caseD)]
                            tableauDeJeu[get_position(caseD)]=" "


                            nvDeplacements=calculDeplacement(caseA, nomPieceD, tableauDeJeu)
                            pieceD["allowed"]=nvDeplacements
                            sauvegardeDeplacement(pieceD, nomPieceD)

                            return tableauDeJeu
    print("Le coup n'est pas valide")

    return False




def cmd_charger(name):

    return charger(name)



def cmd_sauvegarder(tableauDeJeu, name, joueur):

    if(sauvegarde(tableauDeJeu, name, joueur)==True):
        print("Sauvegarde effectuee")
        return True

    return False



def cmd_affichage(tableauDeJeu, couleur):

    if(couleur==True):
        affiche_tableau(tableauDeJeu)

    else:
        affiche_tableau_reverse(tableauDeJeu)


def cmd_demarrer():

    return initialisation()

def cmd_voirDeplacements(coor, tableauDeJeu):
    '''
    in : coor -> int (la case par exemple 11)
         tableauDeJeu -> le tableau courant
    '''

    if(dans_tableau(coor)==True and get_piece(tableauDeJeu, coor)!=False):

        nomPiece = get_piece(tableauDeJeu, coor)
        path=os.getcwd()+'\pieces\\'+nomPiece+'.json'
        f=open(path,'r')
        piece=json.load(f)
        f.close()

        print("Deplacements possibles :")
        tab=piece["allowed"]
        for i in range(len(tab)):
            print(tab[i])

    return True



def cmd_rules():
    print("\nDeplacer un pion : 'caseDcaseA' (ligne-colonne) (ex : 1256 (Depart: 12 (ligne 1 colonne 2) Arrivee : 56 (ligne 5 colonne 6)))")
    print("Afficher le tableau de Jeu : 'afficher'")
    print("Sauvegarder une partie : 'sauvegarder'")
    print("Charger une partie : 'charger'")
    print("Arreter une partie : 'stop'\n")

