"""Calculadora de tarifa mòbil"""


tarifa_base = 10.0
minuts_consumits = int(input("Minuts que has consumit: "))

tarifa_final = 0


if minuts_consumits >= 0:
    if minuts_consumits <= 180:
        tarifa_final = tarifa_base

    elif minuts_consumits > 180 and minuts_consumits <= 240:
        tarifa_final = tarifa_base + (minuts_consumits - 180) * 0.1

    else:
        tarifa_final = tarifa_base + (60 * 0.1) + (minuts_consumits - 240) * 0.2
    1
    print("El cost de la tarifa és de", tarifa_final, "€")

else:
    print("Entrada no vàlida. Els minuts ha de ser una xifra de 0 o majors")



