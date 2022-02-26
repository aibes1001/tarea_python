

def nuevo_diccionario(diccionario, lista_palabras):
    lista_claves = diccionario.keys()
    res = filter(lambda s : lista_palabras.count(s) == 1, lista_claves)
    return {i : diccionario[i] for i in res}

d = {"ab": 1, "b":2, "c": 4, "d":2}

l = ["ab", "c", "f"]
print(nuevo_diccionario(d,l))