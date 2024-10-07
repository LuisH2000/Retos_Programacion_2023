'''
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
'''
def showPoints(playerOne: int, playerTwo: int):
    if playerOne >= 3 and playerTwo >= 3:
        if playerOne == playerTwo:
            print("Deuce")
            return
        if playerOne - playerTwo == 1:
            print("Ventaja P1")
        elif playerOne - playerTwo == 2:
            print("Ha ganado P1")
        elif playerOne - playerTwo == -1:
            print("Ventaja P2")
        else:
            print("Ha ganado P2")
        return
    
    points = ("Love", "15", "30", "40")
    if playerOne == playerTwo:
        print(f"{points[playerOne-1]} All")
        return
    if playerOne == 4 and playerTwo < 3:
        print(f"Ha ganado P1")
        return
    if playerTwo == 4 and playerOne < 3:
        print("Ha ganado P2")
        return

    string_points = f"{points[playerOne-1]} - {points[playerTwo-1]}"
    print(string_points)


def main():
    match_points = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
    #match_points = ["P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P1", "P2", "P2"]
    P1_points = 0
    P2_points = 0

    for i in match_points:
        if i == "P1": 
            P1_points += 1
        if i == "P2": 
            P2_points += 1
        showPoints(P1_points, P2_points)

main()

    