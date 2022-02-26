

def squares_greater(lista_numeros):
    return [i**2 for i in lista_numeros if i > 10]

l = [10, 12, 15]

res = squares_greater(l)
print(res)