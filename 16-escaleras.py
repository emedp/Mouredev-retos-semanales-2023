'''
/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */
'''

def stairs (steps: int):
    output = ""
    
    if steps == 0:
        output = "__"
    
    elif steps > 0:
        output = "  " * steps + "_" + "\n"
        for step in range(steps):
            output += "  " * (steps - 1 - step) + "_|" + "\n"

    elif steps < 0:
        output = " _" + "\n"
        for step in range(abs(steps)):
            output += ("  " * (step + 1)) + "|_" + "\n"

    print(output)

user_said = int(input("Introduce el número de escaleras a dibujar: "))
stairs(user_said)