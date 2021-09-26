import json
import os

def recup_unicode (piece):
    '''
    permet de récupérer le carctère unicode de la piece en paramètre
    in : piece -> str
    out : unicode -> str
    '''
    path=os.getcwd()+'\pieces\\'+piece+'.json'
    f=open(path,'r')
    dic=json.load(f)
    return dic["unicode"]



def affiche_tableau(tableauDeJeu):
    '''
    Permet d'afficher le tableau de jeu pour le joueur blanc (True)
    '''
    mainLine='   |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  '
    separation='---|------------------------------------------------'

    i=len(tableauDeJeu)-1
    ligne=8

    while (i>0):

        line=' '+str(ligne)+' |'
        for j in range (8):
            if (tableauDeJeu[(ligne-1)*8+j] !=' '):
                symbole=recup_unicode(tableauDeJeu[(ligne-1)*8+j]).strip()
            else:
                symbole=' '

            line+='  '+str(symbole)+'  |'
            i-=1

        print(line)
        ligne-=1
        print(separation)
    print (mainLine)



def affiche_tableau_reverse(tableauDeJeu):
    '''
    Permet d'afficher le tableau de jeu pour le joueur noir (False)
    '''
    mainLine='   |  8  |  7  |  6  |  5  |  4  |  3  |  2  |  1  |  '
    separation='---|------------------------------------------------'

    i=0
    ligne=1

    while (i<len(tableauDeJeu)):

        line=' '+str(ligne)+' |'
        for j in range (8):
            if (tableauDeJeu[ligne*8-(j+1)] !=' '):
                symbole=recup_unicode(tableauDeJeu[ligne*8-(j+1)]).strip()
            else:
                symbole=' '

            line+='  '+str(symbole)+'  |'
            i+=1

        print(line)
        ligne+=1
        print(separation)
    print (mainLine)