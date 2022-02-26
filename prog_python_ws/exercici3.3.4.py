"""Alarma despertador"""

#Suposem que els dies de la setmana són de 1 a 7 (de dilluns a divendres)
dia_setmana = int(input("Dia de la setmana (de l'1 al 7): "))
vacances = str(input("Estàs de vacances? (si o no) "))


hora_despertador = 0

if(dia_setmana >= 1 and dia_setmana <= 7) and (vacances == "si" or vacances == "no"):

    if (dia_setmana >= 1 and dia_setmana <= 5):
        if vacances == "si":
            print("El despertador sonarà a les 10:00")
        else:
            print("El despertador sonarà a les 08:00")
    else:
        if vacances == "si":
            print("Despertador apagat")
        else:
            print("El despertador sonarà a les 10:00")

else:
    print("Entrades no vàlides")