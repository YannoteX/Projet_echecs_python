'''
Bibliothèque de gestion de fichiers.
'''

import json
import os
from deplacements import *
from case import *

def initialisation():
    '''
    A la création d'une nouvelle partie. Cette fonction créer un tableau et de nouveaux dictionnaires pour les pieces
    in : name -> String(nom de la partie)
    out : tableauDeJeu -> tableau (de jeu :) )
    '''
    piece={"unicode":"","allowed":[]}

    tableauDeJeu=[]
    for i in range (64):
        tableauDeJeu.append(" ")

    tableauDeJeu[0]="t1b"
    tableauDeJeu[1]="c1b"
    tableauDeJeu[2]="f1b"
    tableauDeJeu[3]="r1b"
    tableauDeJeu[4]="k1b"
    tableauDeJeu[5]="f2b"
    tableauDeJeu[6]="c2b"
    tableauDeJeu[7]="t2b"
    tableauDeJeu[8]="p8b"
    tableauDeJeu[9]="p7b"
    tableauDeJeu[10]="p6b"
    tableauDeJeu[11]="p5b"
    tableauDeJeu[12]="p4b"
    tableauDeJeu[13]="p3b"
    tableauDeJeu[14]="p2b"
    tableauDeJeu[15]="p1b"
    tableauDeJeu[48]="p1n"
    tableauDeJeu[49]="p2n"
    tableauDeJeu[50]="p3n"
    tableauDeJeu[51]="p4n"
    tableauDeJeu[52]="p5n"
    tableauDeJeu[53]="p6n"
    tableauDeJeu[54]="p7n"
    tableauDeJeu[55]="p8n"
    tableauDeJeu[56]="t1n"
    tableauDeJeu[57]="c1n"
    tableauDeJeu[58]="f1n"
    tableauDeJeu[59]="k1n"
    tableauDeJeu[60]="r1n"
    tableauDeJeu[61]="f2n"
    tableauDeJeu[62]="c2n"
    tableauDeJeu[63]="t2n"

    deplacements=calculDeplacement(get_coor(8), tableauDeJeu[8], tableauDeJeu)
    piece["unicode"]="\u2659"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[8])

    deplacements=calculDeplacement(get_coor(9), tableauDeJeu[9], tableauDeJeu)
    piece["unicode"]="\u2659"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[9])

    deplacements=calculDeplacement(get_coor(10), tableauDeJeu[10], tableauDeJeu)
    piece["unicode"]="\u2659"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[10])

    deplacements=calculDeplacement(get_coor(11), tableauDeJeu[11], tableauDeJeu)
    piece["unicode"]="\u2659"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[11])

    deplacements=calculDeplacement(get_coor(12), tableauDeJeu[12], tableauDeJeu)
    piece["unicode"]="\u2659"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[12])

    deplacements=calculDeplacement(get_coor(13), tableauDeJeu[13], tableauDeJeu)
    piece["unicode"]="\u2659"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[13])

    deplacements=calculDeplacement(get_coor(14), tableauDeJeu[14], tableauDeJeu)
    piece["unicode"]="\u2659"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[14])

    deplacements=calculDeplacement(get_coor(15), tableauDeJeu[15], tableauDeJeu)
    piece["unicode"]="\u2659"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[15])

    deplacements=calculDeplacement(get_coor(48), tableauDeJeu[48], tableauDeJeu)
    piece["unicode"]="\u265F".strip()
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[48])

    deplacements=calculDeplacement(get_coor(49), tableauDeJeu[49], tableauDeJeu)
    piece["unicode"]="\u265F".strip()
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[49])

    deplacements=calculDeplacement(get_coor(50), tableauDeJeu[50], tableauDeJeu)
    piece["unicode"]="\u265F"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[50])

    deplacements=calculDeplacement(get_coor(51), tableauDeJeu[51], tableauDeJeu)
    piece["unicode"]="\u265F"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[51])

    deplacements=calculDeplacement(get_coor(52), tableauDeJeu[52], tableauDeJeu)
    piece["unicode"]="\u265F"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[52])

    deplacements=calculDeplacement(get_coor(53), tableauDeJeu[53], tableauDeJeu)
    piece["unicode"]="\u265F"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[53])

    deplacements=calculDeplacement(get_coor(54), tableauDeJeu[54], tableauDeJeu)
    piece["unicode"]="\u265F"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[54])

    deplacements=calculDeplacement(get_coor(55), tableauDeJeu[55], tableauDeJeu)
    piece["unicode"]="\u265F"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[55])

    deplacements=calculDeplacement(get_coor(0), tableauDeJeu[0], tableauDeJeu)
    piece["unicode"]="\u2656"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[0])

    deplacements=calculDeplacement(get_coor(1), tableauDeJeu[1], tableauDeJeu)
    piece["unicode"]="\u2658"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[1])

    deplacements=calculDeplacement(get_coor(2), tableauDeJeu[2], tableauDeJeu)
    piece["unicode"]="\u2657"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[2])

    deplacements=calculDeplacement(get_coor(3), tableauDeJeu[3], tableauDeJeu)
    piece["unicode"]="\u2655"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[3])

    deplacements=calculRoi(get_coor(4))
    piece["unicode"]="\u2654"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[4])

    deplacements=calculDeplacement(get_coor(5), tableauDeJeu[5], tableauDeJeu)
    piece["unicode"]="\u2657"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[5])

    deplacements=calculDeplacement(get_coor(6), tableauDeJeu[6], tableauDeJeu)
    piece["unicode"]="\u2658"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[6])

    deplacements=calculDeplacement(get_coor(7), tableauDeJeu[7], tableauDeJeu)
    piece["unicode"]="\u2656"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[7])

    deplacements=calculDeplacement(get_coor(56), tableauDeJeu[56], tableauDeJeu)
    piece["unicode"]="\u265C"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[56])

    deplacements=calculDeplacement(get_coor(57), tableauDeJeu[57], tableauDeJeu)
    piece["unicode"]="\u265E"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[57])

    deplacements=calculDeplacement(get_coor(58), tableauDeJeu[58], tableauDeJeu)
    piece["unicode"]="\u265D"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[58])

    deplacements=calculRoi(get_coor(59))
    piece["unicode"]="\u265A"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[59])

    deplacements=calculDeplacement(get_coor(60), tableauDeJeu[60], tableauDeJeu)
    piece["unicode"]="\u265B"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[60])

    deplacements=calculDeplacement(get_coor(61), tableauDeJeu[61], tableauDeJeu)
    piece["unicode"]="\u265D"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[61])

    deplacements=calculDeplacement(get_coor(62), tableauDeJeu[62], tableauDeJeu)
    piece["unicode"]="\u265E"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[62])

    deplacements=calculDeplacement(get_coor(63), tableauDeJeu[63], tableauDeJeu)
    piece["unicode"]="\u265C"
    piece["allowed"]=deplacements
    sauvegardeDeplacement(piece, tableauDeJeu[63])

    print("Initialisation terminee, la partie peut commencer.")

    return tableauDeJeu




def sauvegarde(tableauDeJeu, name, joueur):
    '''
    Cette fonction sauvegarde le tableau de jeu courant.
    in : tableauDeJeu -> tableau echiquier à sauvegarder (tableau)
         name -> str nom de la sauvegarde (peut-être un nom existant)
         joueur -> boolean la couleur du joueur qui reprendra (True-blanc False-noir)
    out : True
    '''
    print("Sauvegarde en cours")
    partie = {"tableau":"","joueur":""}
    partie["tableau"]=tableauDeJeu
    partie["joueur"]=joueur

    path=os.getcwd()+'\saves\\'+name+'.json'
    f=open(path,'w')
    json.dump(partie, f)
    f.close

    return True



def sauvegardeDeplacement(dic, piece):
    '''
    Cette fonction sauvegarde le dictionnaire de la piece dans le bon fichier.
    in -> dic -> dictionnaire de la piece
          piece -> str (nom de la piece)
    out -> true si tout va bien
    '''

    path=os.getcwd()+'\pieces\\'+piece+'.json'
    f=open(path,'w')
    json.dump(dic, f)
    f.close

    return True



def chargerDeplacement(piece):
    '''
    Cette fonction charge le dictionnaire de la piece en paramètre.
    in : piece -> str (nom de la piece
    out : dic -> dictionnaire de la piece
    '''
    path=os.getcwd()+'\pieces\\'+piece+'.json'
    f=open(path,'r')
    dic=json.load(f)

    return dic



def charger(name):
    '''
    Permet de charger une partie depuis son nom.
    in : name -> str (nom de la partie)
    out : partie -> dictionnaire de la partie
    '''
    print("Chargement en cours")

    path=os.getcwd()+'\saves\\'+name+'.json'
    f=open(path,'r')
    partie=json.load(f)
    f.close()

    for i in range (len(partie["tableau"])):
        if (partie["tableau"][i]!=' '):
            piece=chargerDeplacement(partie["tableau"][i])
            deplacements=calculDeplacement(get_coor(i), partie["tableau"][i], partie["tableau"])
            sauvegardeDeplacement(piece, partie["tableau"][i])

    print("Chargement réussi")
    return partie





    print ("Chargement termine")

    return partie




def rechercheFichier(name):
    '''
    Permet de vériffier qu'un fichier existe.
    in : name -> str (nom)
    out : True si existe, False sinon
    '''
    path=os.getcwd()+'\saves\\'
    file=name+".json"

    tab= os.listdir(path)

    if (file in tab):
        return True
    return False



def suppr_piece(piece, dic):
    '''
    Efface les déplacements possible de la piece (car ne peut plus jouer)
    in : piece -> str (la piece)
         dic -> dictionnaire (pour effacer les déplacements)
    out : True si tout va bien
    '''
    dic["allowed"]=[]

    path=os.getcwd()+'\pieces\\'+piece+'.json'
    f=open(path,'w')
    json.dump(dic, f)
    f.close

    return True