'''
/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
 * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */
'''

from pynput.keyboard import Key, KeyCode, Listener

KONAMI_CODE = [Key.up, Key.up,
               Key.down, Key.down,
               Key.left, Key.right,
               Key.left, Key.right,
               KeyCode.from_char("b"), KeyCode.from_char("a"),
               Key.spaceba ]

konami_index = 0

def konami_code (key):
    print(key)

    global konami_index 

    if key == KONAMI_CODE[konami_index]:
        konami_index += 1
    else:
        konami_index = 0

    if konami_index == len(KONAMI_CODE):
        print("""
        \n
        ╦╔═╔═╗╔╗╔╔═╗╔╦╗╦  ╔═╗╔═╗╔╦╗╔═╗
        ╠╩╗║ ║║║║╠═╣║║║║  ║  ║ ║ ║║║╣ 
        ╩ ╩╚═╝╝╚╝╩ ╩╩ ╩╩  ╚═╝╚═╝═╩╝╚═╝
        \n
        """)
        return False

with Listener(on_press=konami_code) as listener:
    listener.join()