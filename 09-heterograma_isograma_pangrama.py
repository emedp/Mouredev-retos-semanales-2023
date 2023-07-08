'''
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
'''

# Ninguna letra repetida
def heterograma (text: str):

    text = text.lower()
    text = text.replace(" ","")

    for letter in text:
        if text.count(letter) != 1:
            return False
        
    return True

# Cada letra aparece el mismo número de veces
def isograma (text: str):

    orden = None
    text = text.lower()
    text = text.replace(" ","")

    for letter in text:
        if orden == None:
            orden = text.count(letter)

        if text.count(letter) != orden:
            return False
        
    return True

# Aparecen todas las letras del abecedario
# CURIOSIDAD: si también es un heterograma se le llama PANGRAMA PERFECTO
def pangrama(text: str):

    alphabet = dict(map(chr, range(97, 123)))
    print(alphabet)
    
    text = text.lower()
    text = text.replace(" ","")

    for letter in text:
        alphabet[letter] += 1

    for letter in alphabet:
        if alphabet[letter] == 0:
            return False

    return True



texto = input("Introduce el texto a analizar:\n")

if heterograma(texto):
    print("Es un heterograma, por lo tanto un isograma de primero orden")

if isograma(texto):
    print("Es un isograma")

if pangrama(texto):
    print("Es un pangrama")