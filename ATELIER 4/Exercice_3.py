import random

def placesLettre(char : str, mot : str)->list:
    char = char[0]
    
    if (not char in mot):
        return []
    else:
        res = []
        for i in range(0, len(mot)):
            if (mot[i] == char):
                res.append(i)
        return res

print(placesLettre('l', 'hellol'))

def outputStr(mot : str):
    str = ""
    for i in mot:
        str += '_'
    return str

print(outputStr('hello'))

def runGame():
    dico = [
        ("hello", 5),
        ("world", 5),
    ]

    word = random.randint(0, len(dico))
    word = dico[word][0]
    game_str = outputStr(word)

    i = 0
    while i <= 5:
        if (not '_' in game_str):
            print("Gagné !!")
            break
        
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

runGame()

