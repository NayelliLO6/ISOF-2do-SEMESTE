
# Actividad realizada en clase

# actividad en la que se realizaran intentos para adivinar cierto numero
# que te arrojaran aleatoriamente

from random import Random


intentos_realizados=0
print("Jugando a asivinar el numero, tienes 5 intentos ")
Numero=Random.randint(1,10)
while intentos_realizados<=5:
    Numero_ingresado=int(input("Ingresa un numero entre el 1-10  "))
    if Numero_ingresado>Numero:
        print("El numero ingresado es mayor")
    elif Numero_ingresado<Numero:
        print("El numero ingresado es meron ")
    else:
        print("Felicidades lo has encontrado ")
        break
intentos_realizados=intentos_realizados+1