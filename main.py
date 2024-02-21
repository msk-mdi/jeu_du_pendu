#!/usr/bin/env python3
import getpass

##################################################################
### ici l'utilisateur choisie le mots et le cache avec getpass ###
##################################################################

# couleur
NORMAL = '\033[0m'
CYAN = '\033[0;36m'
VERT = '\033[0;32m'
ROUGE = '\033[0;31m'
JAUNE = '\033[0;33m'

# affichage d'introduction au jeu du pendu
print(f"{ROUGE}--- JEU DU PENDU ---")
print(f"\n ------ ")
print(f"|      |")
print(f"|      |")
print(f"|      O")
print(f"|     -|-")
print(f"|      |")
print(f"|     / \\")
print(f"|{NORMAL}")

# creation d'une variable vide pour la fonction d'apres
mots = ""

# le sous programme va demander à l'utilisateur de choisir son mots secrets et il sera cachée grace à getpass, ensuite il sera stocker dans la variable mots
def choisir_mots():
    mots = getpass.getpass(f"\n{CYAN}Choisie ton mots secret >{NORMAL} ")
    return mots

# pour permettre de mettre des tirets quand l'utilisateur n'a pas trouver la lettre et de remplacer le tiret quand il à trouver le mot
def init_mot_cache(mot):
    # on fais tant de _ selon la taille du mot, c'est pour sa qu'on fais _ x taille du mot
    return "_" * len(mot)

# pour  mettre à jour le mot trouver
def maj_mot_cache(mot_cache, mot_secret, lettre):
    # crée une variable vide pour plus tard
    nouveau_mot_cache = ""
    # permet de parcourir chaque caractère du mot
    for i in range(len(mot_secret)):
        # verifie si le mot secret est égal à lettre
        if mot_secret[i] == lettre:
            # ajoute lettre dans la variable
            nouveau_mot_cache += lettre
        else:
            # ajoute mot_cache[i] dans la variable
            nouveau_mot_cache += mot_cache[i]
    # renvoie le resultat
    return nouveau_mot_cache

# le sous programme du jeu du pendu
def jeu_du_pendu():
    # le mot secrets est le mots que le 1er sous programme à choisie dans la liste_mots
    mot_secret = choisir_mots()
    mot_cache = init_mot_cache(mot_secret)
    vies = 8

    # si le nombre de vie est supérieur à 0, alors il demande à l'utilisateur de rentrer une lettre
    while vies > 0:
        print(mot_cache)
        lettre = input("\nEntrez une lettre > ")

        # si la lettre n'est pas seul, alors il lui dis qu'il faut entrer une lettre valide
        if len(lettre) != 1:
            print(f"{ROUGE}Veuillez entrer une seule lettre valide{NORMAL}")
            continue

        # si la lettre est dans le mot secrets, la variable mot_cache inclura le sous programme maj_mot_cache
        if lettre in mot_secret:
            mot_cache = maj_mot_cache(mot_cache, mot_secret, lettre)
            # si le mot cache est le mot secret, alors l'utilisateur à gagné
            if mot_cache == mot_secret:
                print(f"\n{VERT}Félicitations ! Vous avez deviné le mot cache qui était {mot_secret}{NORMAL}")
                break
        else:
            vies -= 1
            print(f"\n{JAUNE}Lettre incorrecte. Il vous reste {vies} vies{NORMAL}")

    # si il n'a plus de vie, alors il indique à l'utilisateur qu'elle sont épuisé et lui donne le mot secret
    if vies == 0:
        print(f"\n{ROUGE} ------ ")
        print(f"|      |")
        print(f"|      |")
        print(f"|      O")
        print(f"|     -|-")
        print(f"|      |")
        print(f"|     / \\")
        print(f"|{NORMAL}")
        print(f"Vous avez épuisé toutes vos vies. Le mot secret était {VERT}{mot_secret}{NORMAL}")

# lance le sous programme et donc le jeu
jeu_du_pendu()
