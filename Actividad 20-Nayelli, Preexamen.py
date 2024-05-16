#examen

def calcular_calificacion(total_preguntas, preguntas_correctas, preguntas_incorrectas):
    puntaje = (preguntas_correctas / total_preguntas) * 100

    print("Resultados del examen:")
    print("Total de preguntas:", total_preguntas)
    print("Preguntas correctas:", preguntas_correctas)
    print("Preguntas incorrectas:", preguntas_incorrectas)
    print("Puntaje obtenido:", puntaje)


    if puntaje >= 70:
        print("Calificación: Aprobado")
    else:
        print("Calificación: No aprobado")

def main():
    total_preguntas = int(input("Ingrese el total de preguntas del examen: "))
    preguntas_correctas = int(input("Ingrese la cantidad de preguntas correctas: "))
    preguntas_incorrectas = int(input("Ingrese la cantidad de preguntas incorrectas: "))

    if total_preguntas < 0 or preguntas_correctas < 0 or preguntas_incorrectas < 0:
        print("Por favor, ingrese valores válidos (números positivos).")
    elif preguntas_correctas + preguntas_incorrectas > total_preguntas:
        print("La cantidad total de preguntas correctas e incorrectas no puede ser mayor que el total de preguntas.")
    else:
        calcular_calificacion(total_preguntas, preguntas_correctas, preguntas_incorrectas)

if __name__ == "__main__":
    main()
