# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.}
# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.

import time

hora = time.localtime()

if hora.tm_hour >= 19:
    print("ya es hora de ir para la casa")
else:
    seg = 60 - hora.tm_sec
    min = 59 - hora.tm_min
    hor = 18 - hora.tm_hour

    print("te quedan para finalizar el trabajo:")
    print("horas:", hor)
    print("minutos:", min)
    print("segundos:", seg)
