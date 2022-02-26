

from functools import reduce


def greater_than_average(x, data_array):
    #Mitjana
    res = reduce(lambda x, y: x + y, data_array) / len(data_array)
    return x > res

l = [1, 2, 3]
res = greater_than_average(3, l)
print(res)

