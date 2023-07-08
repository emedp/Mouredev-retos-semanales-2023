'''
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
'''

def sombrero_seleccionador ():
    houses_names = ["Gryffindor", "Slytherin" , "Hufflepuff", "Ravenclaw"]
    houses_points = [0, 0, 0, 0]
    house_assigned = ""

    ask_1 = "¿Qué poción crearías?:\n"+"1.Gloria\n"+"2.Poder\n"+"3.Amor\n"+"4.Sabiduría\n"
    ask_2 = "¿Qué te resulta más difícil de manejar?:\n"+"1.Sentirte inútil\n"+"2.Ser ignorado\n"+"3.Soledad\n"+"4.Aburrimiento\n"
    ask_3 = "¿En una batalla cuál es tu rol?:\n"+"1.Luchador\n"+"2.Espía\n"+"3.Sanador\n"+"4.Táctico\n"
    ask_4 = "¿Qué entorno te representa más?:\n"+"1.Cualquiera es bueno\n"+"2.Ciudad\n"+"3.Campo\n"+"4.Biblioteca\n"
    ask_5 = "¿Qué color prefieres?:\n"+"1.Rojo\n"+"2.Verde\n"+"3.Amarillo\n"+"4.Azul\n"

    print("Responde a las preguntas escribiendo el número de tu elección")
    response_1 = int(input(ask_1)) - 1
    response_2 = int(input(ask_2)) - 1
    response_3 = int(input(ask_3)) - 1
    response_4 = int(input(ask_4)) - 1
    response_5 = int(input(ask_5)) - 1

    # Reparto de puntos
    houses_points[response_1] += 1
    houses_points[response_2] += 1
    houses_points[response_3] += 1
    houses_points[response_4] += 1
    houses_points[response_5] += 1

    # ALGORITMO SELECCIONADOR
    index_house = houses_points.index(max(houses_points))
    house_assigned = houses_names[index_house]
    
    print("A partir de ahora perteneces a la casa de... " + house_assigned)

sombrero_seleccionador()