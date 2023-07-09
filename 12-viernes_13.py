'''
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
'''

import datetime

def friday_13 (month: int, year: int):
    
    is_friday_13 = False

    date = datetime.datetime(year, month, 13)
    
    if date.weekday == 4:
        is_friday_13 = True

    print(is_friday_13)
    return is_friday_13


friday_13 (7,2023)