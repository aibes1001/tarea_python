

def clean_list(usuarios, baneados):
    res = filter(lambda x: baneados.count(x) == 0, usuarios)
    return list(res)

u = ["a", "b", "c"]
b = ["a", "e", "i"]

res = clean_list(u, b)
print(res)