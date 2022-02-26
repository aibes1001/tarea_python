
def clean_list(usuarios, baneados):
    return [i for i in usuarios if baneados.count(i) == 0]

u = ["o", "s", "i"]
b = ["a", "e", "i"]

res = clean_list(u, b)
print(res)