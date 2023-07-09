'''
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
'''

def url_params (url: str):

    params = dict()

    # check URL contains params
    if url.count("?") == 0:
        return print("La URL no contiene parametros.")

    url_split = url.split("?")
    url_split = url_split[1].split("&")

    for param in url_split:
         param = param.split("=")
         params[param[0]] = param[1]

    print(params)
    return params


url_params("https://retosdeprogramacion.com?year=2023&challenge=0")