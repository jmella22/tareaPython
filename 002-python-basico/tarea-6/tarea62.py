# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        if self.nota >= 4.0:
            print("el Alumno", self.nombre, "si aprobo con nota", self.nota)
        else:
            print("el Alumno", self.nombre, "no aprobo con nota", self.nota)


alumno1 = Alumno("Juan", 4.2)
alumno2 = Alumno("Erik", 3.5)
alumno3 = Alumno("Pedrita", 7.0)

alumno1.aprobado()
alumno2.aprobado()
alumno3.aprobado()
