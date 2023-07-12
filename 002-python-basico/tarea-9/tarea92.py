# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.


from functools import reduce


def filYsum(lista):
    resultado = list(filter((lambda x: x % 2), lista))
    print(resultado)
    resultado = reduce((lambda x, y: x + y), resultado)
    print(resultado)


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 1010]


filYsum(lista1)
filYsum(lista2)
