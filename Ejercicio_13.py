'''
/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
'''
import random
from math import floor

palabras: list = ["Luis", "Illojuan", "Twitch", "Hololive"]
palabra: str = palabras[random.randint(0, len(palabras)-1)].lower()
palabraOculta: str = ""
maxLetrasOcultas: int = floor(len(palabra)*0.6)
for letra in palabra:
    if random.randint(0,1) == 1 or maxLetrasOcultas == 0:
        palabraOculta += letra
    else:
        palabraOculta +='_'
        maxLetrasOcultas -= 1

cantItentos = 3
print("Palabra oculta:")
while cantItentos > 0:
    print(palabraOculta)
    intento: str = input(f"Ingresar una letra o palabra con la misma longitud, te quedan {cantItentos} intentos: ")
    intento = intento.lower()
    if len(intento) > len(palabra):
        print("Fallaste, la palabra ingresada es muy larga")
        cantItentos -= 1
        continue

    if len(intento) > 1:
        if intento == palabra:
            break
        else:
            print("La palabra ingresada no es correcta")
            cantItentos -= 1
        continue

    posLetras = [i for i, letra in enumerate(palabra) if intento == letra]
    if len(posLetras) == 0:
        print("La letra no forma parte de la palabra")
        cantItentos -= 1
    else:
        for i in posLetras:
            palabraOculta = palabraOculta[:i] + palabra[i] + palabraOculta[i+1:]
        if palabraOculta == palabra:
            print(palabraOculta)
            break

if cantItentos == 0: 
    print("Perdiste :(") 
else:
    print("Felicidades, ganaste :)")