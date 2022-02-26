

import re


def without_first_letter(lista_palabras):
    res = map(lambda s : s[0], lista_palabras)
    return list(res)


l = ["Aitor", "hola", "clon"]

res = without_first_letter(l)
print(res)