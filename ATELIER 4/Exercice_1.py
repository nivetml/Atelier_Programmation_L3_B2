import re

def full_name(str_arg : str)->str:
    res = str_arg.split()
    return res[0].upper() + " " + res[1].capitalize()

print(full_name('varamo baptiste'))

def is_mail(str_arg : str)->(int, int):
    if (not '@' in str_arg):
        return (0, 2)
    
    mail = str_arg.split('@')

    if (mail[0] == ''):
        return (0, 1)
    elif (not '.' in mail[1]):
        return (0, 4)
    elif (mail[1] == '' or '/' in mail[1] or '@' in mail[1] or '\\' in mail[1]):
        return (0, 3)
    else:
        return (1, 0)

print(is_mail('baptiste.varamo@gm\\ail.com'))