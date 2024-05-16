

# Actividad 6 realizada en clase

# hacer una funcion donde mande 3 parametros, 
# el primero y el segundo seran numeros y el tercero sera la operacion que desee realizar 
# Si la operacion es suma, sumara y regresara el resultado en un mensaje, 
# el mismo caso para la resta, multiplicacion y resta

print("Ingresa 2 Numeros y la operacion que desee realizar; Suma, resta, Multiplicacion o Division")

Dato_1=int(input("Agrega un numero: "))
Dato_2=int(input("Agrega un numero; "))
Operacion=int(input("Operacion a realizar: 1 suma, 2 resta, 3 multiplicacion y 4 divicion"))


if Operacion ==1:
    sum=Dato_1+Dato_1
    print(f"la suma de {Dato_1} + {Dato_2} es {sum} ")
elif Operacion ==2:
    res=Dato_1-Dato_1
    print(f"la resta de {Dato_1} - {Dato_2} es {res} ")
elif Operacion ==3:
    mult=Dato_1*Dato_2
    print(f"la multiplicaciom de {Dato_1}*{Dato_2} es {mult} ")
elif Operacion==4:
    div=Dato_1/Dato_2
    print(f"la divicion de {Dato_1}/{Dato_2} es {div} ")
else:
    print("La operacion que desea realizar no se encuenta disponible")