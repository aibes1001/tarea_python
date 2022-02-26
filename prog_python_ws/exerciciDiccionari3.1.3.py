

from functools import reduce


def get_minimum_dicc(diccionario):
    lista_valores = diccionario.values()
    return reduce(lambda m, n : min(m,n), lista_valores)


d = {"a" : 1, "b": -3, "c": 2, "d":10}

res = get_minimum_dicc(d)
print (res)