#!/usr/bin/env python3
from getpass import getpass

NORMAL = '\033[0m'
CYAN = '\033[0;36m'
VERT = '\033[0;32m'
ROUGE = '\033[0;31m'
JAUNE = '\033[0;33m'

def image():
    print(f"{ROUGE}--- JEU DU PENDU ---")
    print(f"\n ------ ")
    print(f"|      |")
    print(f"|      |")
    print(f"|      O")
    print(f"|     -|-")
    print(f"|      |")
    print(f"|     / \\")
    print(f"|{NORMAL}")

image()

def choisir_mots():
    mots = getpass(f"\n{CYAN}Choisie ton mots secret >{NORMAL} ")
    return mots

def init_mot_cache(mot):
    return "_" * len(mot)

def maj_mot_cache(mot_cache, mot_secret, lettre):
    nouveau_mot_cache = ''
    for i in range(len(mot_secret)):
        if mot_secret[i] == lettre:
            nouveau_mot_cache += lettre
        else:
            nouveau_mot_cache += mot_cache[i]
    return nouveau_mot_cache

def jeu_du_pendu():
    mot_secret = choisir_mots()
    mot_cache = init_mot_cache(mot_secret)
    vies = 8

    while vies > 0:
        print(mot_cache)
        lettre = input("\nEntrez une lettre > ")

        if len(lettre) != 1:
            print(f"{ROUGE}Veuillez entrer une seule lettre valide{NORMAL}")
            continue

        if lettre in mot_secret:
            mot_cache = maj_mot_cache(mot_cache, mot_secret, lettre)
            if mot_cache == mot_secret:
                print(f"\n{VERT}Félicitations ! Vous avez deviné le mot cache qui était {mot_secret}{NORMAL}")
                break
        else:
            vies -= 1
            print(f"\n{JAUNE}Lettre incorrecte. Il vous reste {vies} vies{NORMAL}")

    if vies == 0:
        image()
        print(f"Vous avez épuisé toutes vos vies. Le mot secret était {VERT}{mot_secret}{NORMAL}")

    replay = input('Veux-tu rejouer (y/n) > ')
    if replay == 'y':
        jeu_du_pendu()
    else:
        exit()
        
jeu_du_pendu()