'''
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
'''

piece_cords = [(0,0), (1,0), (1,1), (1,2)]

def rotate ():
    pass

def left ():
    new_cords = []

    for (row, col) in piece_cords:
        if col == 0:
            return print("No puedes mover la pieza más a la izquierda.")
        
        new_cords.append((row, col - 1))

    piece_cords.clear()
    piece_cords.extend(new_cords)

def right ():
    new_cords = []

    for (row, col) in piece_cords:
        if col == 9:
            return print("No puedes mover la pieza más a la derecha.")
        
        new_cords.append((row, col + 1))

    piece_cords.clear()
    piece_cords.extend(new_cords)

def down ():
    new_cords = []

    for (row, col) in piece_cords:
        if row == 9:
            return print("No puedes mover más la pieza hacia abajo.")
        
        new_cords.append((row + 1, col))

    piece_cords.clear()
    piece_cords.extend(new_cords)

def table ():
    for row in range(10):
        for col in range(10):
            if (row, col) in piece_cords:
                print("🔳", end="")
            else:
                print("🔲", end="")
        print()

continue_loop = True
while (continue_loop):
    table()
    print("Introduce una orden:")
    print("1. Rotar")
    print("2. Mover a la izquierda")
    print("3. Mover a la derecha")
    print("4. Mover hacia abajo")
    print("Pulsa cualquier otra tecla más intro para cerrar el programa.")
    command = int(input())

    if command == 1:
        rotate()
    elif command == 2:
        left()
    elif command == 3:
        right()
    elif command == 4:
        down()
    else:
        continue_loop = False
