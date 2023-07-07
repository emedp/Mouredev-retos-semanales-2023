'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
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
 */
'''

def tennis_game (game: list):

    point_values = ["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0

    for point in game:
        # SE REPARTE EL PUNTO
        if point == "P1":
            p1_points += 1
        if point == "P2":
            p2_points += 1
        
        # SE MUESTRA COMO VA EL PARTIDO
        if p1_points > 2 and p2_points > 2 and abs(p1_points - p2_points) == 0:
            print("Deuce")
        elif p1_points > 2 and p2_points > 2 and abs(p1_points - p2_points) == 1:
            if p1_points > p2_points: print("Ventaja P1")
            if p1_points < p2_points: print("Ventaja P2")
        elif p1_points > 3 or p2_points > 3 and abs(p1_points - p2_points) == 2:
            # FINALIZADO EL PARTIDO SE NOMBRA EL GANADOR
            if p1_points > p2_points: print("Ha ganado el P1")
            if p1_points < p2_points: print("Ha ganado el P2")
            break
        else:
            print(point_values[p1_points] + " - " + point_values[p2_points])
    

tennis_game(["P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P2", "P2"])