'''
/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
'''

ansGryffindor = 0
ansSlytherin = 0
ansHufflepuff = 0
ansRavenclaw = 0

qAndA = [
    ["¿Que cualidad valoras mas de ti mismo?", "Valentia", "Ambicion", "Lealtad", "Sabiduria"],
    ["¿Que harias si te encontraras con un animal herido?", "Lo ayudarias valientemente, arriesgando tu seguridad", "Buscarias alguna ventaja para ti, tal vez puedas sacar algo", "Lo cuidarias con dedicacion hasta que se recupere", "Investigarias la mejor manera de tratar al animal"],
    ["¿Que lugar prefieres en Hogwarts?", "La torre de Gryffindor", "Las mazmorras", "Cualquier lugar de la cocina", "La biblioteca"],
    ["¿Cual de estos valores es mas importante para ti?", "Coraje", "Poder", "Amistad", "Conocimiento"],
    ["¿Como reaccionas ante un desafio?", "Lo enfrentas con valentia", "Lo usas para mejorar tu posicion", "Buscas apoyo y trabajas en equipo", "Lo analizas y planeas tu estrategia"]
]

for i in qAndA:
    print(i[0] + "\n")
    numAns = 1
    for ans in i[1:]:
        print(f"{numAns} - {ans}")
        numAns += 1
    userAns = ""
    while True:
        userAns = input("Ingresar respuesta: ")
        try:
            userAns = int(userAns)
            if userAns >= 1 and userAns <= 4:
                break
            else:
                print("Respuesta invalida")
        except ValueError:
            print("Respuesta invalida")
    if userAns== 1:
        ansGryffindor += 1
    elif userAns == 2:
        ansSlytherin += 1
    elif userAns == 3:
        ansHufflepuff += 1
    elif userAns == 4:
        ansRavenclaw += 1

max = max(ansGryffindor, ansHufflepuff, ansRavenclaw, ansSlytherin)

if ansSlytherin == max:
    print("Eres de Slytherin")
elif ansGryffindor == max:
    print("Eres de Gryffindor")
elif ansRavenclaw == max:
    print("Eres de Ravenclaw")
else:
    print("Eres de Hufflepuf")