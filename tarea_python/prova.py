print([chr(i + 65) for i in range(5)])

str_seats_per_row = ""
for i in range(5):
    str_seats_per_row += chr(i+65)

print(str_seats_per_row)

dic = {123: "Juan", 456: "Maria", 789: "Pedro", "sdfas": 344} 
print(dic)

#Añadir/modificar un item
dic[122] = "Eva" #si no existe lo añade
dic["sdfas"] = 355 #si existe lo modifica
print("Modifico clave 'sdfas' y añado la 122: ",dic)

#Otra forma de añadir/modificar el valor de una clave
dic.update({124: "Manolo"}) #si no existe lo añade
dic.update({123: "Pepe"}) #si existe lo modifica
print("Modifico clave 123 y añado la 124: ",dic)