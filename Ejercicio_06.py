'''
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */
'''
from enum import Enum

class Moves(Enum):
    piedra = 0
    papel = 1
    tijera = 2
    lagarto = 3
    spock = 4

def who_wins(game: list):
    playerOnePoints = 0
    playerTwoPoints = 0
    winsTo = [[0, -1, 1, 1, -1],
              [1, 0, -1, -1, 1],
              [-1, 1, 0, 1, -1],
              [-1, 1, -1, 0, 1],
              [1, -1, 1, -1, 0]]
    for p1, p2 in game:
        try:
            p1, p2 = Moves[p1.lower()].value ,Moves[p2.lower()].value
        except KeyError:
            return f"Invalid value {p1}, {p2}"

        if winsTo[p1][p2] == 1:
            playerOnePoints += 1
        elif winsTo[p1][p2]  == -1:
            playerTwoPoints += 1

    return "Tie" if playerOnePoints == playerTwoPoints else "Player 1" if playerOnePoints > playerTwoPoints else "Player 2"


moves = [("piedra","Tijera"), ("tijera","piedra"), ("papel","tijera")]
print(who_wins(moves))
moves = [("liedra","Tijera"), ("tijera","piedra"), ("papel","tijera")]
print(who_wins(moves))

        
