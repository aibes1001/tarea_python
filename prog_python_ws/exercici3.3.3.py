"""Reserva en restaurant"""

estil_vestir1 = int(input("Quin es l'estil de vestir del comensal 1? "))
estil_vestir2 = int(input("Quin es l'estil de vestir del comensal 2? "))


if (estil_vestir1 >= 0 and estil_vestir1 <= 10) and (estil_vestir2 >= 0 and estil_vestir2 <= 10):
    if (estil_vestir1 <= 2 or estil_vestir2 <= 2):
        print("Ho senc però no teniu taula.")
    elif (estil_vestir1 >= 8 or estil_vestir2 >= 8):
        print("Teniu taula!")
    else:
        print("No sabem si tindrem taula...")

else:
    print("Entrades no vàlides. Les valoracions han de ser entre 0 i 10")

