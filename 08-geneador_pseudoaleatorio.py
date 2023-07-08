'''
/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
'''

import time

random_number = None
seed = time.time()
last_2 = str(seed)[-2:]
last_2 = int(last_2) # cast to int
# Sumandole 1 a la semilla si no es 0, permite que el rango sea [0-100], ya que 100 - (99 + 1) = 0 || 100 - (0) = 100
if last_2 != 0: last_2 += 1
random_number = 100 - last_2
print(random_number)