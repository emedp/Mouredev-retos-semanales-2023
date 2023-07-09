'''
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
'''

text = input("Introduce el texto a analizar:")
phrases = text.split(". ")
print(phrases)

# STADISTICS
total_phrases = 0
total_words = 0
longest_word = ""
len_words = []

for phrase in phrases:

    # total de oraciones
    total_phrases += 1

    words = phrase.split(" ")
    print(words)

    for word in words:

        # total de palabras
        total_words += 1

        # longitud media de palabras
        len_word = len(word)
        len_words.append(len_word)

        # palabra más larga
        if len_word > len(longest_word):
            longest_word = word

print(f"El total de oraciones del texto es {total_phrases} oraciones.")
print(f"El total de palabras del texto es {total_words} palabras.")
print(f"La media de longitud media de las palabras es {sum(len_words)/len(len_words)} letras/palabra.")
print(f"La palabra más larga es: '{longest_word}'")