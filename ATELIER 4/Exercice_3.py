"""
Exercice 3 de l'atelier 4 : Jeu du pendu
file       = "Exercice_3.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

import random
import io

def placesLettre(char: str, mot: str) -> list:
    """ Transform text (Uppercase for Name, Lowercase for surname)
       char -- The letter
       mot -- The word
       return the formated list
       """
    char = char[0]
    if not char in mot:
        return []
    else:
        res = []
        for i in range(0, len(mot)):
            if mot[i] == char:
                res.append(i)
        return res


print(placesLettre('l', 'hellol'))


def outputStr(mot: str):
    str = ""
    for i in mot:
        str += '_'
    return str


print(outputStr('hello'))


def runGame():
    dico = []
    with io.open("littre.txt", 'r', encoding='utf8') as f:
        dico = f.read().split('\n')

    word = random.randint(0, len(dico))
    word = dico[word]
    game_str = outputStr(word)

    i = 0
    while i <= 5:
        if (not '_' in game_str):
            print("Gagné !!")
            return 1

        print("Nb de coup restant : ", 5 - i)
        print(game_str)
        char = input('Saisir une lettre : ')[0]

        pos = placesLettre(char, word)
        if pos != []:
            for j in range(0, len(pos)):
                game_str = game_str[:pos[j]] + char + game_str[pos[j] + 1:]
        else:
            i += 1
            print("LOUPé")
    print("PERDU !!! Le mot était " + word)


runGame()
