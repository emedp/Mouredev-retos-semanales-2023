'''
/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */
'''

def validate_math_expression (math_expression: str) -> bool:
    operations = ['+', '-', '*', '/', '%']

    print("Analizando: " + math_expression)

    expression_splitted = math_expression.split(" ")
    print(expression_splitted)

    # comprobación de que la expresión tiene el tamaño mínimo que es (numero, operación y número)
    # comprobación de que la expresión tiene un número impar de elementos
    if len(expression_splitted) < 3 or len(expression_splitted) % 2 == 0:
        return False

    for index, element in enumerate(expression_splitted):

        # Comprobación si los elementos impares son operaciones y los pares números
        if index % 2 != 0:
            if element not in operations:
                return False
        else:
            if not element.isnumeric():
                return False

    return True

user_said = input("Introduce la expresión matemática a analizar: ")
print(validate_math_expression(user_said))
print("******")
print("TESTS:")
print("******")
print("Sin espacios")
print(validate_math_expression("1+2"))
print("número par de elementos")
print(validate_math_expression("1 + 3 +"))
print("operación inválida")
print(validate_math_expression("1 es 4"))
print("expresión válida")
print(validate_math_expression("5 + 6 / 7 - 4"))