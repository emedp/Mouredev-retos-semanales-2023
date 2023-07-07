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

def sheldon_game (game: list):
    player_1_points = 0
    player_2_points = 0

    for par in game:
        player_1_pick = par[0]
        player_2_pick = par[1]

        if player_1_pick == "🗿":
            if   player_2_pick == "🗿": pass
            elif player_2_pick == "📄": player_2_points += 1
            elif player_2_pick == "✂️": player_1_points += 1
            elif player_2_pick == "🦎": player_1_points += 1
            elif player_2_pick == "🖖": player_2_points += 1
        
        if player_1_pick == "📄":
            if   player_2_pick == "🗿": player_1_points += 1
            elif player_2_pick == "📄": pass
            elif player_2_pick == "✂️": player_2_points += 1
            elif player_2_pick == "🦎": player_2_points += 1
            elif player_2_pick == "🖖": player_1_points += 1

        if player_1_pick == "✂️":
            if   player_2_pick == "🗿": player_2_points += 1
            elif player_2_pick == "📄": player_1_points += 1
            elif player_2_pick == "✂️": pass
            elif player_2_pick == "🦎": player_1_points += 1
            elif player_2_pick == "🖖": player_2_points += 1

        if player_1_pick == "🦎":
            if   player_2_pick == "🗿": player_2_points += 1
            elif player_2_pick == "📄": player_1_points += 1
            elif player_2_pick == "✂️": player_2_points += 1
            elif player_2_pick == "🦎": pass
            elif player_2_pick == "🖖": player_1_points += 1

        if player_1_pick == "🖖":
            if   player_2_pick == "🗿": player_1_points += 1
            elif player_2_pick == "📄": player_2_points += 1
            elif player_2_pick == "✂️": player_1_points += 1
            elif player_2_pick == "🦎": player_2_points += 1
            elif player_2_pick == "🖖": pass


    if player_1_points == player_2_points:
        print("Tie")
    elif player_1_points > player_2_points:
        print("Player 1 Wins")
    elif player_1_points < player_2_points:
        print("Player 2 Wins")

sheldon_game([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])