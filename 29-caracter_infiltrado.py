'''
/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */
'''

def compare_texts (text_1: str, text_2: str):
    texts_diffs = []

    # Comprueba si las longitudes de ambos strings coinciden
    if len(text_1) != len(text_2):
        return print("Los texto no tienen la misma longitud")
    
    for index in range(len(text_1)):
        char_1 = text_1[index]
        char_2 = text_2[index]

        if char_1 != char_2:
            texts_diffs.append(char_2)

    return texts_diffs

print(compare_texts("Me llamo mouredev", "Me llemo mouredov"))
print(compare_texts("Me llamo.Brais Moure", "Me llamo brais moure"))