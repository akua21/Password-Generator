# Generador de Contraseñas

# Imports
import random
import string
from datetime import datetime
from string import punctuation

import argparse

# Parser argumentos
ap = argparse.ArgumentParser()
# Añadimos argumentos al parser (FLAGS)
ap.add_argument("-l", "--length", required=False, help="longitud contraseña")

ap.add_argument("-u", "--upper", required=False, help="solo letras en mayúscula", action="store_true")

ap.add_argument("-w", "--lower", required=False, help="solo letras en minúscula", action="store_true")

ap.add_argument("-a", "--anyletters", required=False, help="cualquier letra", action="store_true")

ap.add_argument("-n", "--numbers", required=False, help="solo números", action="store_true")

ap.add_argument("-s", "--special", required=False, help="solo caracteres especiales", action="store_true")


args = vars(ap.parse_args())


# Tamaño por defecto de la contraseña si no se especifica por comando
default = 5

# Flag -l
l = args['length']


# LETRAS -----------------------------------------------------------------------
# Letras en mayúscula y minúscula
def letters():
    passw = ''
    default = 5
    if l != None:
        default = int(l)
    for i in range(default):
        passw += random.choice(string.ascii_letters)

    return passw

# Letras solo minúsculas
def lowLetters():
    passw = ''
    default = 5
    if l != None:
        default = int(l)
    for i in range(default):
        passw += random.choice(string.ascii_lowercase)

    return passw

# Letras solo mayúsculas
def upLetters():
    passw = ''
    default = 5
    if l != None:
        default = int(l)
    for i in range(default):
        passw += random.choice(string.ascii_uppercase)

    return passw


# NÚMEROS ----------------------------------------------------------------------
# Números de 0 a 9
def numbers():
    random.seed(datetime.now())
    passw = ''
    default = 5
    if l != None:
        default = int(l)
    for i in range(default):
        passw += str(random.randint(0, 9))

    return passw

# C.ESPECIALES -----------------------------------------------------------------
def specialC():
    set(punctuation)
    passw = ''
    default = 5
    if l != None:
        default = int(l)
    for i in range(default):
        passw += random.choice(punctuation)

    return passw

# MEZCLA -----------------------------------------------------------------------
def mix():
    passw = ''
    default = 5
    if l != None:
        default = int(l)
    for i in range(default):
        r = random.randint(0, 4)
        aux = ''

        if r == 0:
            aux = random.choice(string.ascii_letters)
        elif r == 1:
            aux = random.choice(string.ascii_lowercase)
        elif r == 2:
            aux = random.choice(string.ascii_uppercase)
        elif r == 3:
            aux = str(random.randint(0, 9))
        else:
            set(punctuation)
            aux = random.choice(punctuation)

        passw += aux

    return passw

# COMBINACIÓN ------------------------------------------------------------------
def combine(cond):
    passw = ''
    default = 5
    if l != None:
        default = int(l)

    for i in range(default):
        r = random.choice(cond)
        aux = ''

        if r == '0':
            aux = random.choice(string.ascii_uppercase)
        elif r == '1':
            aux = random.choice(string.ascii_lowercase)
        elif r == '2':
            aux = random.choice(string.ascii_letters)
        elif r == '3':
            aux = str(random.randint(0, 9))
        else:
            set(punctuation)
            aux = random.choice(punctuation)

        passw += aux

    return passw


# Comprobamos el número de condiciones para generar la contraseña y cuales son
counter = 0
conditions = []
for i in args:
    if args[i]:
        if i == 'upper':
            counter += 1
            conditions.append('0')

        elif i == 'lower':
            counter += 1
            conditions.append('1')

        elif i == 'anyletters':
            counter += 1
            conditions.append('2')

        elif i == 'numbers':
            counter += 1
            conditions.append('3')

        elif i == 'special':
            counter += 1
            conditions.append('4')


# Si el número es mayor que uno llamamos al método combine, sino al que corresponda
if counter > 1:
    password = combine(conditions)

else:
    if args['upper']:
        password = upLetters()

    elif args['lower']:
        password = lowLetters()

    elif args['anyletters']:
        password = letters()

    elif args['numbers']:
        password = numbers()

    elif args['special']:
        password = specialC()

    else:
        password = mix()


print("Contraseña: ", password)
