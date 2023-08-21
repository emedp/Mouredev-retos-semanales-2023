'''
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
'''

abacus =  [
    "O---OOOOOOOO",
    "OOO---OOOOOO",
    "---OOOOOOOOO",
    "OO---OOOOOOO",
    "OOOOOOO---OO",
    "OOOOOOOOO---",
    "---OOOOOOOOO",
]

def read_abacus (abacus: list):
    
    result = ""
    
    if len(abacus) != 7:
        return print("El ábaco no contiene un número de 7 filas")
    
    for index, row in enumerate(abacus):
        count_number = len(row.split("---")[0])

        if index == 1 or index == 4:
            result += "."
        
        result += str(count_number)
    
    print("Resultado:", result)

read_abacus(abacus)