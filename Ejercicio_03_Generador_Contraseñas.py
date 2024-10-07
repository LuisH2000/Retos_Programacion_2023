'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
'''

import random

def generate_password():
    while True:
        passLength = input("Ingresar la longitud de la password (8 a 16 caracteres): ")
        passLength = int(passLength)
        if passLength >= 8 and passLength <= 16:
            break
        print("Valor invalido, ingresar un valor entre 8 y 16")

    while True:
        capitalLetters = input("Contraseña con mayusculas [Y/N]: ").lower()
        if capitalLetters == 'y':
            capitalLetters = True
            break
        elif capitalLetters == 'n':
            capitalLetters = False
            break
        else:
            print("Valor invalido")

    while True:
        numbers = input("Contraseña con numeros [Y/N]: ").lower()
        if numbers == 'y':
            numbers = True
            break
        elif numbers == 'n':
            numbers = False
            break
        else:
            print("Valor invalido")
    
    while True:
        symbols = input("Contraseña con simbolos [Y/N]: ").lower()
        if symbols == 'y':
            symbols = True
            break
        elif symbols == 'n':
            symbols = False
            break
        else:
            print("Valor invalido")

    characters = list(range(97,123))
    if capitalLetters:
        characters.extend(range(65,91))
    if numbers:
        characters.extend(range(48,58))
    if symbols:
        characters += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))

    password = ""

    while len(password) < passLength:
        password += chr(random.choice(characters))

    return password

print(generate_password())
    
