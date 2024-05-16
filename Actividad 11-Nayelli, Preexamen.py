# Actividad en clase 
#practica para examen


def contar_letras(palabra):
    return len(palabra)


def main():
    palabra = input("Ingresa una palabra: ")
    cantidad_letras = contar_letras(palabra)
    print(f"La cantidad de letras en la palabra {palabra} es: {cantidad_letras}")


if __name__ == "__main__":
    main()