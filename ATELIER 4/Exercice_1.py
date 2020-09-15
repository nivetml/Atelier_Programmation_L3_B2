"""
Exercice 1 de l'atelier 4 : Manipulations simples
file       = "Exercice_1.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""


def full_name(str_arg: str) -> str:
    """ Transform text (Uppercase for Name, Lowercase for surname)
    str_arg -- The string who contain the name/surname
    return the formated text
    """
    res = str_arg.split()
    return res[0].upper() + " " + res[1].capitalize()


def is_mail(str_arg: str) -> (int, int):
    """ Check if email is valid
       str_arg -- The string who contain the email
       return error code or succes code
       """

    res = (1, 0)

    if not '@' in str_arg:
        res = (0, 2)
    mail = str_arg.split('@')
    if mail[0] == '':
        res = (0, 1)
    elif not '.' in mail[1]:
        res = (0, 4)
    elif mail[1] == '' or '/' in mail[1] or '@' in mail[1] or '\\' in mail[1]:
        res = (0, 3)

    return res


def test_exercice1():
    """
    Test for Exercice 1
    """
    print("Test full_name (musk elon) : ", full_name('musk elon'))
    print("Test is_mail (elon.musk@tes\\la.money) : ", is_mail('elon.musk@tes\\la.money'))
    print("Test is_mail (elon.musk@tesla.money) : ", is_mail('elon.musk@tesla.money'))


test_exercice1()
