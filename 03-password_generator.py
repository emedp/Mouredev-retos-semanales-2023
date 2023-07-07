'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
'''

import random

def password_generator (longitude: int, with_mayus: bool, with_numbers: bool, with_symbols: bool):
    
    generated_password = ""
    valid_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if longitude < 8 or longitude > 16:
        return print("La longitud debe ser entre 8 y 16.")
    
    if with_mayus:
        valid_chars += ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    if with_numbers:
        valid_chars += ['1','2','3','4','5','6','7','8','9','0']

    if with_symbols:
        valid_chars += ['!','$','%','&','=','?','¿','@','#','~','€','¬','¡','+','-',',',';','.',':','_','*']


    for index in range(0, longitude):
        picker = random.randint(0,len(valid_chars)-1)
        generated_password += valid_chars[picker]

    return generated_password


longitude = int(input("Introduce la longitud de la contraseña (entre 8 y 16): "))
mayus = bool(input("Escribe 'SI' para que contenga mayúsculas: ") == "SI")
numbers = bool(input("Escribe 'SI' para que la contraseña contenga números: ") == "SI")
symbols = bool(input("Escribe 'SI' para que la contraseña contenga símbolos: ") == "SI")

print(password_generator(longitude, mayus, numbers, symbols))