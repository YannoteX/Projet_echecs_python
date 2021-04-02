from colored import *

def affiche_tableau(x):
    '''
    Permet d'afficher le tableau de jeu

    input -> x = tableau (de jeu)
    output -> none
    '''
    mainLine='   |   a    b    c    d    e    f    g    h  '
    separation='   |'

    i=0
    ligne=1
    print(mainLine)
    while (i<len(x)):

        print(separation)

        line=' '+str(ligne)+' |'
        for j in range (8):

            line+='  '+x[i]
            i+=1

        print(line)
        ligne+=1

affiche_tableau(['t1b', 'c1b', 'f1b', 'r1b', 'R1b', 'f2b', 'c2b', 't2b', 'p1b', 'p2b', 'p3b', 'p4b', 'p5b', 'p6b', 'p7b', 'p8b', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', 'p1n', 'p2n', 'p3n', 'p4n', 'p5n', 'p6n', 'p7n', 'p8n', 't1n', 'c1n', 'f1n', 'R1n', 'r1n', 'f2n', 'c2n', 't2n']
)

