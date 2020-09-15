def ouvrante(car : str):
    car = car[0]
    return bool((ord(car) == 40 or ord(car) == 91 or ord(car) == 123))

def fermante(car : str):
    car = car[0]
    return bool(ord(car) == 41 or ord(car) == 93 or ord(car) == 125)

def renverse(car : str):
    car = car[0]
    if (ord(car) == 40):
        return chr(41)
    elif (ord(car) == 91):
        return chr(93)
    elif (ord(car) == 123):
        return chr(125)
    else:
        return car

def operateur(car : str):
    car = car[0]
    return (ord(car) == 42 or ord(car) == 43 or ord(car) == 45 or ord(car) == 47)

def nombre(car : str):
    return isdigit(car)

def caractere_valide(car : str):
    return ouvrante(car) or fermante(car) or nombre(car) or operateur(car)

def verif_parenthese(expression : str):
    ouvrante = False

    for i in expression:
        if (not caractere_valide(expression)):
            return False

        if (ouvrante(i)):
            ouvrante = True
        elif (fermante(i) and not ouvrante):
            return False
        elif (fermante(i)):
            ouvrante = False
    return True