

def word_length(lista_palabras):
    return [len(i) for i in lista_palabras if i != "el"]


l = ["el", "la", "los", "las"]

print(word_length(l))