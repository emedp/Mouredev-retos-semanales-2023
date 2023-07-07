'''
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
'''

def fizzbuzz ():
    for index in range(1,101):
        
        is_multiple_3 = index % 3 == 0
        is_multiple_5 = index % 5 == 0

        if is_multiple_3 and is_multiple_5:
            print("fizzbuzz")
        elif is_multiple_3:
            print("fizz")
        elif is_multiple_5:
            print("buzz")
        else:
            print(index)

fizzbuzz()