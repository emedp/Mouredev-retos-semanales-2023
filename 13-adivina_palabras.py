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

words = ["software", "esternocleidomastoideo", "programacion", "adivinanza"]

def guess_word ():
    
    attempts = 3

    # word_selected
    word_selected = random.choice(words)
    
    # word_incompleted
    word_incompleted = ""
    hidden_letters_num = int(len(word_selected) / 2) # 50%
    hidden_letters_index = random.sample(range(len(word_selected)), hidden_letters_num)
    
    # calculating word_incompleted
    for index, letter in enumerate(word_selected):
        word_incompleted += "_" if index in hidden_letters_index else letter
    
    print("ADIVINA LA PALABRA\n" + "Escribe letras para completar la palabra o si ya sabes cuál es intenta adivinarla. ¡Buena suerte!")
    while attempts > 0:
        print(f"Número de intentos restantes: {attempts}")
        print(word_incompleted)
        player_said = input("Introduce una letra o la palabra: ")

        if len(player_said) == 1:
            word_incompleted_new = ""
            for index, letter in enumerate(word_selected):
                if player_said == letter:
                    word_incompleted_new += letter
                else:
                    word_incompleted_new += word_incompleted[index]

            word_incompleted = word_incompleted_new
        else:
            if player_said == word_selected:
                word_incompleted = player_said
            else:
                print("La palabra que has dicho no es correcta.")

        # Si el usuario introduce la palabra o introduce la ultima letra a adivinar finaliza el juego ganando el jugador
        if word_incompleted == word_selected:
            print("¡Felicidades! Has acertado la palabra")
            break

        attempts += -1

    if attempts == 0:
        print("Has perdido. La solución era: " +  word_selected)


guess_word()