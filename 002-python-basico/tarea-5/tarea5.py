def es_bisiesto(year=0):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("El año", year, "es bisiesto")
                return
            else:
                print("El año", year, "no es bisiesto")
                return
        else:
            print("El año", year, "es bisiesto")
            return
    else:
        print("El año", year, "no es bisiesto")
        return


# Ejemplos:
es_bisiesto(2012)  # Es bisiesto
es_bisiesto(1600)  # Es bisiesto
es_bisiesto(1900)  # No es Bisiesto
es_bisiesto(1984)  # Es bisiesto
es_bisiesto(1983)  # No es bisiesto
