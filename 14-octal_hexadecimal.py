'''
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
'''

b_08_values = [0,1,2,3,4,5,6,7]
b_16_values = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']


def decimal_base_changer (decimal_number: int, new_base: int, new_base_values: list, new_base_number: str):
    
    quotient = decimal_number / new_base
    remainder = decimal_number % new_base

    new_base_number = str(new_base_values[int(remainder)]) + new_base_number

    if quotient >= 1:
        new_base_number = decimal_base_changer(quotient, new_base, new_base_values, new_base_number)
    
    return new_base_number
    



def octal_hexadecimal (decimal_number: int):
    b_08 = decimal_base_changer(decimal_number, 8, b_08_values, "")
    b_16 = decimal_base_changer(decimal_number, 16, b_16_values, "")
    
    print(b_08)
    print(b_16)

input_number = int(input("Introduce el número a cambiar a base octal y base hexadecimal: "))
octal_hexadecimal(input_number)