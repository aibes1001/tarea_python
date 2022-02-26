"""Canviador de dòlars a euros"""

tasa_canvi_dolar_euro = 0.85

quantitat_dolars = float(input("Introdueix la quantitat de dòlars: "))
canvi_dolar_euro = quantitat_dolars * tasa_canvi_dolar_euro

print("El canvi a euros de", quantitat_dolars, "dòlar/1s és", canvi_dolar_euro)
