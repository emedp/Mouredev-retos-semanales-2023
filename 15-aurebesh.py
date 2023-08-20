'''
/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 */
'''

spanish_aurebesh = {
    "a": "aurek",
    "b": "besh",
    "c": "cresh",
    "d": "dorn",
    "e": "esk",
    "f": "forn",
    "g": "grek",
    "h": "herf",
    "i": "isk",
    "j": "jenth",
    "k": "krill",
    "l": "leth",
    "m": "mern",
    "n": "nerm",
    "o": "osk",
    "p": "peth",
    "q": "qek",
    "r": "resh",
    "s": "senth",
    "t": "trill",
    "u": "usk",
    "v": "vev",
    "w": "wesk",
    "x": "xesh",
    "y": "yirt",
    "z": "zerek",
    "ch": "cherek",
    "ae": "enth",
    "eo": "onith",
    "kh": "krenth",
    "ng": "nen",
    "oo": "orenth",
    "sh": "shen",
    "th": "thesh",
}

def translate_spanish_aurebesh (text: str, is_aurebesh: bool):
    text_translated = ""
    text = text.lower()
    
    for char in text:
        text_translated += spanish_aurebesh.get(char, char)
    
    return text_translated

input_text = input("Introduce el texto a traducir: ")
translated = translate_spanish_aurebesh(input_text, False)
print(translated)

