'''
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
'''

import time

def countdown (start: int, gap: int):

    now = time.time()

    # check start and gap are positive numbers
    if start <= 0 or gap <= 0:
        print("Los parámetros introducidos no son válidos.")

    while start >= 0:
        print(start)
        time.sleep(gap)
        start += -1

    print("La cuenta atrás ha finalizado.")

user_start = int(input("Introduce el número de cuenta atrás: "))
user_gap = int(input("Introduce el número de segundos para que baje el contador: "))

countdown(user_start, user_gap)