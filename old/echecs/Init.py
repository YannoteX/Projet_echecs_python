from json import *
import os
from case import place_decimal


def saisie_pieces(x, y, couleur):
    '''
    Cette fonction permet de remplir le tableau de jeu (echiquier) que va utiliser le module affiche, et de créer les dictionnaires des pieces.

    input : x -> tableau de jeu (ici toute les valeurs sont à zero)
            y -> Chaine de caractère (les pièces à placer)
            couleur -> couleur des pièces choisie

    output : x -> tableau de jeu (rempli)

    '''

# n° des pieces (pour éviter d'avoir plusieurs fois la même)
    IDpion=1
    IDfou=1
    IDcheval=1
    IDtour=1

    A=[]
    i=0
    while(i<(len(y))):

        if (y[i]!=' '):

# Cette partie permet de créer les dictionnaires

            B={}
            nom=""
            position=""
            for j in range(2):

                nom+=y[i]
                if(y[i]=='p'):
                    nom+=str(IDpion)
                    IDpion+=1
                elif(y[i]=='f'):
                    nom+=str(IDfou)
                    IDfou+=1
                elif(y[i]=='c'):
                    nom+=str(IDcheval)
                    IDcheval+=1
                elif(y[i]=='t'):
                    nom+=str(IDtour)
                    IDtour+=1
                elif(y[i]=='r'):
                    nom+='1'
                elif(y[i]=='R'):
                    nom+='1'

                elif(y[i]=='n'):
                    couleur='noir'
                elif(y[i]=='b'):
                    couleur='blanc'
                i+=1


            for h in range(2):

                position+=y[i]
                i+=1

            B['nom']=nom
            B['couleur']=couleur
            B['position']=position
            B['possibilités']=''
            A.append(B)
        i+=1

# Cette partie permet de stocker les dictionnaires dans un fichier json d'un repertoire personnalisé

    path=os.getcwd()+'\json\pieces'+couleur+'.json'
    f=open(path,'w')
    f.write(str(A))
    f.close

    for i in range(len(A)):

        place=place_decimal(A[i]['position'][0], A[i]['position'][1])
        x[place]=A[i]['nom']


    return x

def posit():

    tableauDeJeu=[]

    for i in range(64):
        tableauDeJeu.append('   ')

    saisie_pieces(tableauDeJeu, 'tna8 tnh8 cnb8 cng8 fnc8 fnf8 Rnd8 rne8 pna7 pnb7 pnc7 pnd7 pne7 pnf7 png7 pnh7', 'noir')
    saisie_pieces(tableauDeJeu, 'tba1 tbh1 cbb1 cbg1 fbc1 fbf1 Rbe1 rbd1 pba2 pbb2 pbc2 pbd2 pbe2 pbf2 pbg2 pbh2', 'blanc')
    print (tableauDeJeu)
posit()