'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

def prime (number: int):
    if number <= 1: return False

    for i in range(2,number):
        if number % i == 0: return False

    return True


def fibonacci (number: int, num_1, num_2):
    sum = num_1 + num_2

    if number == sum:
        return True
    elif number < sum:
        return False
    else:
        return fibonacci(number, num_2, sum)

def even_odd (number: int):
    return number % 2 == 0

def analize_number (number: int):
    result = str(number)

    
    if prime (number):
        result += " es primo"
    else:
        result += " no es primo"

    if fibonacci(number, 0, 1):
        result += ", es fibonacci"
    else:
        result += ", no es fibonacci"

    if even_odd(number):
        result += " y es par"
    else:
        result += " y es impar"

    print(result)

analize_number(int(input("Introduce el número a analizar: ")))