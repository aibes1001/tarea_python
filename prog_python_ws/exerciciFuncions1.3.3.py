

def every_element_greater_than(numero, lista):
    res = filter(lambda x: x > numero, lista)
    return len(list(res)) == len(lista)


l = [6, 7, 8]
res = every_element_greater_than(5, l)
print(res)