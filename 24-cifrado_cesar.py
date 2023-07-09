'''
/*
 * Crea un programa que realize el cifrado César de un texto y lo imprima.
 * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
 *
 * Te recomiendo que busques información para conocer en profundidad cómo
 * realizar el cifrado. Esto también forma parte del reto.
 */
'''

def cesar_cipher (text: str, displacement: int, decrypt: bool):
    cipher = ""
    if decrypt:
        displacement = displacement * -1

    for letter in text:
        if letter != " ":
            cipher += chr(ord(letter) + displacement)
        else:
            cipher += " "

    print(cipher)
    return cipher
    

user_text = input("Introduce el texto a utilizar la encriptación César:\n")
user_displacement = int(input("Introduce el número de salto del algoritmo: "))
user_cipher = bool(int(input("¿Es una encriptación (0) o una desencriptación (1)?: ")))

cesar_cipher(user_text, user_displacement, user_cipher)