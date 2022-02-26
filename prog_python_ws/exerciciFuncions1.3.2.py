

from functools import reduce


def get_minimum(lista_numeros):
    return reduce(lambda m, n : min(m,n), lista_numeros)


l = [3,-27,-1,5]

res = get_minimum(l)
print(res)