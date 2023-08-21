'''
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
'''

def number_excel_col (col: str):
    col_number = 0
    diff_ascii = 64

    #value = ord(col) - diff_ascii
    #print(value)

    # reverse the string
    col = col[::-1]
    
    # iterate position by base 26
    for index, letter in enumerate(col):
        base26 = ord(letter) - diff_ascii
        if index != 0:
            col_number += base26 * 26 ** index
        else:
            col_number += base26

    return print(col_number)


number_excel_col(input("Introduce la columna excel a calcular su número: "))