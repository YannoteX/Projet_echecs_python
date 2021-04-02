def place_decimal(x, y):
    '''
    Cette fonction permet de transformer la valeur str en décimal d'une pièce.

    input : x -> colonne
            y -> ligne
    output : x -> valeur décimale
    '''

    ligne=(ord(y)-49)*8
    colonne=ord(x)-97

    return ligne+colonne

def place_str(x):
    '''
    Cette fonction permet de tranformer la valeur décimale en str d'une pièce.

    input -> valeur décimale à changer en chaine
    output -> chaine de caractère
    '''

    ligne=chr((x//8)+49)
    colonne=chr((x%8)+97)

    return colonne+ligne



def case_est_dans_tableau(x):
    '''
    Cette fonction vérifie si la case entrée par le joueur existe

    input : x -> chaine à vérifier
    output : True ou False
    '''
    place=place_decimal(x)
    if (place<64 and place>=0):
        return True

    print (x,"n'est pas une place valide" )
    return False


def case_occupee(x, y):
    '''
    Cette fonction vérifie si la case est occupée et par quoi.

    input : x -> chaine à vérifier
            y -> tableau de jeu
    output : x -> False ou la piece sur la case
    '''

    place=place_decimal(x)
    if (y[place]!='   '):
        return y[place]

    return False