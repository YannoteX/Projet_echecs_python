from commandes import *
from gestionFichiers import rechercheFichier

stop=False

print("Bienvenue dans le jeu d'echecs. Pour voir la liste des commandes disponibles, tapez 'regles'")

while(stop==False):
    cmd=input("Voulez vous 'demarrer' une partie ou 'charger' une partie ? :")
    if (cmd.lower()=="regles" or cmd.lower()=="regle"):
        cmd_rules()

    elif(cmd.lower()=='demarrer'):
        tableauDeJeu=cmd_demarrer()
        joueur=True
        cmd_affichage(tableauDeJeu, joueur)
        stop=True

    elif(cmd.lower()=='charger'):
        nomPartie=input("Entrez le nom de votre partie : ")
        if (rechercheFichier(nomPartie)==True):
            Partie=cmd_charger(nomPartie)
            joueur=Partie["joueur"]
            tableauDeJeu=Partie["tableau"]
            cmd_affichage(tableauDeJeu, joueur)
            stop=True
        else:
            print("Cette partie n'existe pas")

    else:
        print ("\nCette commande n'existe pas, entrez-en une autre ou tapez 'regles' :\n")


stop=False

while(stop==False):
    if (joueur==True):                                                     #tour du joueur blanc

        cmd=input("\nJoueur blanc, c'est a vous ! Entrez votre commande :\n")
        if(ord(cmd[0])>=49 and ord(cmd[0])<= 56):

            coup=cmd_tour(int(cmd), joueur, tableauDeJeu)
            if (coup!=False):

                tableauDeJeu=coup
                joueur=False
                cmd_affichage(tableauDeJeu, joueur)

        else:

            if (cmd.lower()=="afficher"):

                cmd_affichage(tableauDeJeu, joueur)

            elif (cmd.lower()=="deplacement"):

                coord=input("Entrez les coordonnees de la piece : ")
                cmd_voirDeplacements(int(coord), tableauDeJeu)


            elif (cmd.lower()=="sauvegarder"):

                nomSave=input("Choisissez le nom de la sauvegarde :")
                if(rechercheFichier(nomSave)==True):

                    stopVerif=False
                    while (stopVerif==False):

                        verif=input("Une sauvegarde existe déjà sous ce nom. Voulez-vous l'écraser ? (oui/non) :")

                        if(verif.lower()=="oui"):

                            cmd_sauvegarder(tableauDeJeu, nomSave, joueur)
                            stopVerif=True

                        elif (verif.lower()=="non"):

                            stopVerif=True
                else:
                    cmd_sauvegarder(tableauDeJeu, nomSave, joueur)


            elif (cmd.lower()=="charger"):

                stopVerif=False
                while (stopVerif==False):

                    verif=input ("En etes-vous sur (pensez a sauvegarder) ? oui/non :")
                    if(verif.lower()=="oui"):

                        stopVerif=True
                        nomLoad=input("Entrez le nom de la sauvegarde :")

                        if (rechercheFichier(nomLoad)==True):

                            Partie=cmd_charger(nomLoad)
                            joueur=Partie["joueur"]
                            tableauDeJeu=Partie["tableau"]
                            cmd_affichage(tableauDeJeu, joueur)

                        else:

                            print("La Sauvegarde n'existe pas.")

                    elif (verif.lower()=="non"):

                        stopVerif=True

            elif( cmd.lower()=="regle" or cmd.lower()=="regles"):
                cmd_rules()

            elif (cmd.lower()=="stop"):

                stopVerif=False
                while (stopVerif==False):

                    verif=input ("En etes-vous sur (pensez a sauvegarder) ? oui/non :")
                    if(verif.lower()=="oui"):

                        stopVerif=True
                        stop=True

                    elif (verif.lower()=="non"):

                        stopVerif=True


    else:                                                           #tour du joueur noir
        cmd=input("\nJoueur noir, a vous de jouer ! Entrez votre commande :\n")
        if(ord(cmd[0])>=49 and ord(cmd[0])<= 56):

            coup=cmd_tour(int(cmd), joueur, tableauDeJeu)
            if (coup!=False):

                tableauDeJeu=coup
                joueur=True
                cmd_affichage(tableauDeJeu, joueur)

        else:

            if (cmd.lower()=="afficher"):

                cmd_affichage(tableauDeJeu, joueur)

            elif (cmd.lower()=="sauvegarder"):

                nomSave=input("Choisissez le nom de la sauvegarde :")
                if(rechercheFichier(nomSave)==True):

                    stopVerif=False
                    while (stopVerif==False):

                        verif=input("Une sauvegarde existe déjà sous ce nom. Voulez-vous l'écraser ? (oui/non) :")

                        if(verif.lower()=="oui"):

                            cmd_sauvegarder(tableauDeJeu, nomSave, joueur)
                            stopVerif=True

                        elif (verif.lower()=="non"):

                            stopVerif=True
                else:
                    cmd_sauvegarder(tableauDeJeu, nomSave, joueur)

            elif (cmd.lower()=="charger"):

                while (stopVerif==False):

                    verif=input ("En etes-vous sur (pensez a sauvegarder) ? oui/non :")
                    if(verif.lower()=="oui"):

                        stopVerif=True
                        nomLoad=input("Entrez le nom de la sauvegarde :")

                        if (rechercheFichier(nomLoad)==True):

                            Partie=cmd_charger(nomLoad)
                            joueur=Partie["joueur"]
                            tableauDeJeu=Partie["tableau"]
                            cmd_affichage(tableauDeJeu, joueur)

                        else:

                            print("La Sauvegarde n'existe pas.")

                    elif (verif.lower()=="non"):

                        stopVerif=True

            elif( cmd.lower()=="regle" or cmd.lower()=="regles"):
                cmd_rules()

            elif (cmd.lower()=="stop"):

                stopVerif=False
                while (stopVerif==False):

                    verif=input ("En etes-vous sur (pensez a sauvegarder) ? oui/non :")
                    if(verif.lower()=="oui"):

                        stopVerif=True
                        stop=True

                    elif (verif.lower()=="non"):

                        stopVerif=True