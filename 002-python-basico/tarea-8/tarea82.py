# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle


class Vehiculo:
    puertas = None
    color = None

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self) -> str:
        return f'El color del vehiculo es {self.color} y la cantidad de puertas son {self.puertas}'


peugeot301 = Vehiculo("blanco", 5)

print(peugeot301)

file = open("Vehiculo_objeto.bin", 'wb')
pickle.dump(peugeot301, file)
file.close()


file = open("Vehiculo_objeto.bin", 'rb')
nueva_peugeot = pickle.load(file)
file.close()

print(nueva_peugeot)
