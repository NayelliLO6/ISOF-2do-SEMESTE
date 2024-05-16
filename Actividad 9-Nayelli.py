

# Acatividad realizada e clase

#solicitar al usuario que agregue una palabra de la cual escogera una letra a buscar

Palabra=input("Ingresa una palabra:  ")
Letra=input("Ingresa la letra que desea buscar:  ")
for Letra_consecutiva in Palabra:
    if Letra==Letra_consecutiva:
        print(f"la letra {Letra} se encontro en a palabra {Palabra}")
        break
    else:
        print(f"La letra {Letra} no se encontro en la palabra {Palabra}")
        break

    
    
