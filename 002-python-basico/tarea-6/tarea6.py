class Vehiculo:
    color = "rojo"
    ruedas = 5
    puertas = 5


class Coche(Vehiculo):
    velocidad = "120 km/h"
    cilindrada = "1.6 turbo"


Auto = Coche()

print(Auto.color)
print(Auto.ruedas)
print(Auto.puertas)
print(Auto.velocidad)
print(Auto.cilindrada)
