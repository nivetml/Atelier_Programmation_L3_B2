"""
Exercice 2 de l'atelier 4 : Mots croisés
file       = "Exercice_2.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""


def separer(number_list: list) -> list:
    """ Sort by sign function without ascending or descending sorting
    Keyword argument:
    number_list -- List of number to sum
    return the sorted list
    """
    LSEP = []
    count_negative = 0
    for e in number_list:
        if e < 0:
            LSEP.insert(0, e)
            count_negative += 1
        elif e > 0:
            LSEP.append(e)
        else:
            LSEP.insert(count_negative, e)

    return LSEP