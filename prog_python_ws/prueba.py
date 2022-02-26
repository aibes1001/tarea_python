#Importar moduls complets
import math

#Importar funcions de moduls
from math import factorial as fact


print("Hola món")
x =10
y = 3.9

print(y)

""" Recordar que el casting de un float a int
    trunca el valor """
print(int(y)) 

print(int("345"))

#Tipus de variable
print(type(y))

#Operacions:

#Suma i resta
a = 1 + 5.5
b = 2.5 - 3

#Multiplicació 
c = 3 * 2

#Divisió amb resultat sempre decimal (float)
d = 4 / 2
e = 5 / 2
print(d)
print(e)

#Divisió amb resultat sempre enter (int)
d = 4 // 2
e = 5 // 2 #trunca
print(d)
print(e)

#Rest
e = 5%2
print(e)

#Potència a ^ b
a = 2 ** 3 # = 8
print(a)


#Manejar cadenes
print("El resultat és" + str(a))

print("El resultat {0} es parell?".format(a))

a = 10 / 3

print("Resultat de a: {0:.2f}".format(a))

#Introducció de dades per teclat
#a = int(input('Introdueix un enter: '))
#b = int(input('Introdueix un altre enter: '))

#print(a+b)
#print('El resultat de',a,'i', b,'es', a+b )

x = 16
print("L'arrel quadrada de", x, "és", math.sqrt(x))

print(fact(5))

#If-elif-else

color = "roig"

if color == "roig":
    print("El color es roig")
elif color == "blau":
    print("El color es blau")
else:
    print("El color es no es roig ni blau")


a = 1


print(a == 0 or a == 1)
print(a >= 0 and a == 1)
print(not a > 1)# not false = true (a no és major que 1)