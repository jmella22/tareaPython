# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

class Miarchivo:
    nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre

    def escribir(self, datos):
        f = open(self.nombre, 'a')
        for linea in datos:
            if not linea.endswith('\n'):
                linea += '\n'
            f.write(linea)

        f.close()
        print("su texto fue escrito exitosamente")


lista1 = ["hola", "Perro", "ciudad"]
lista2 = ["Manzana", "Peras", "Platanos"]


miLista1 = Miarchivo("texto.txt")

miLista1.escribir(lista1)
miLista1.escribir(lista2)
