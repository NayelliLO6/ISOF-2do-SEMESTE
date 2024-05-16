#numeros aleatorios

from random import Random


intentos_realizados=0
print("Adivina el numero y seras acreedor de un cupon ")
Numero=Random.randint(1,10)
while intentos_realizados<=2:
    Numero_ingresado=int(input("Ingresa un numero entre el 1-10  "))
    if Numero_ingresado>Numero:
        print("El numero ingresado es mayor")
    elif Numero_ingresado<Numero:
        print("El numero ingresado es meron ")
    else:
        print("Felicidades seras acreedor de un cupon ")
        break
intentos_realizados=intentos_realizados+1