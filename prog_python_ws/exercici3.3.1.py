"""Implementar programa que llig l'hora en format 24h i transforma a 12h"""

hora = int(input("Introdueix l'hora: "))

if hora < 0 or hora > 23:
    print("Hora no vàlida. L'hora ha de ser entre 0 i 23")

else:
    minuts = int(input("Introdueix els minuts: "))

    if minuts < 0 or minuts > 59:
        print("Minuts no vàlida. Han de ser entre 0 i 59")
    else:
        
        ampm = ""
        hora12h = hora % 12

        if hora // 12 == 0:
            ampm = "AM"
        else:
            ampm = "PM"

        
        print("Son les {0:02d}:{1:02d} {2}".format(hora12h, minuts, ampm))




