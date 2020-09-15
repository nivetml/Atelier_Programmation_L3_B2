"""
Exercice 5 de l'atelier 4 : Vérification d'expressions arithmétiques
file       = "Exercice_5.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""


def ouvrante(car: str) -> bool:
    """  Check if  a char is an opening parenthesis, hook or hug
    car -- Char to analyse
    return True if car is an opening parenthesis, hook or hug
    """
    car = car[0]
    return bool((ord(car) == 40 or ord(car) == 91 or ord(car) == 123))


def fermante(car: str) -> bool:
    """  Check if  a char is an closing parenthesis, hook or hug
     car -- Char to analyse
     return True if car is an closing parenthesis, hook or hug
     """
    car = car[0]
    return ord(car) == 41 or ord(car) == 93 or ord(car) == 125


def renverse(car: str) -> str:
    """ Replace an parenthesis, hook or hug by its reverse
     car -- Char to analyse
     return the inverted char
     """
    car = car[0]
    if ord(car) == 40:
        return chr(41)
    elif ord(car) == 91:
        return chr(93)
    elif ord(car) == 123:
        return chr(125)
    else:
        return car


def operateur(car: str) -> bool:
    """ Check if a char is an operator
        car -- Char to analyse
        return True if car is an operator
    """
    car = car[0]
    return ord(car) == 42 or ord(car) == 43 or ord(car) == 45 or ord(car) == 47


def nombre(car: str) -> bool:
    """ Check if a char is a number
        car -- Char to analyse
        return True if car is a number
    """
    return car.isdigit()


def caractere_valide(car: str) -> bool:
    """ Check if a char is valid
        car -- Char to analyse
        return True if is valid
    """
    return ouvrante(car) or fermante(car) or nombre(car) or operateur(car)


def verif_parenthese(expression: str):
    """ Check if an expression is valid
        expression -- str to analyse
        return True if is vlid
    """
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


def test_exercice5():
    """
       Test for exercice 5
    """
    print("Test ouvrante avec ( - TRUE : ", ouvrante("("))
    print("Test ouvrante avec { - TRUE : ", ouvrante("{"))
    print("Test ouvrante avec [ - TRUE : ", ouvrante("["))
    print("Test ouvrante avec ) - FALSE : ", ouvrante(")"))
    print("\nTest fermante avec ) - TRUE : ", fermante(")"))
    print("Test fermante avec } - TRUE : ", fermante("}"))
    print("Test fermante avec ] - TRUE : ", fermante("]"))
    print("Test fermante avec ( - FALSE : ", fermante("("))
    print("\nTest renverse avec (  : ", renverse("("))
    print("Test renverse avec {  : ", renverse("{"))
    print("Test renverse avec [  : ", renverse("["))
    print("Test renverse avec )  : ", renverse(")"))
    print("Test renverse avec }  : ", renverse("}"))
    print("Test renverse avec ]  : ", renverse("]"))
    print("Test renverse avec ]  : ", renverse("1"))
    print("\nTest nombre avec 4 -> TRUE  : ", nombre("4"))
    print("Test nombre avec g -> FALSE  : ", nombre("g"))
    print("\nTest caractère_valide avec 4 -> TRUE : ", caractere_valide("4"))
    print("Test caractère_valide avec ) -> TRUE : ", caractere_valide("4)"))
    print("Test caractère_valide avec g -> FALSE  : ", caractere_valide("g"))
    print("\nTest expression_valide avec (3+2) * 6-1 -> TRUE : ", caractere_valide("(3+2) * 6-1"))
    print("Test expression_valide avec (3+2] * 6-1 -> FALSE : ", caractere_valide("(3+2] * 6-1"))


test_exercice5()
