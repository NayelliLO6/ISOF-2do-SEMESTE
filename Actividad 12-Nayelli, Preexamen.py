#Actividad de clase
#preexamen
def promedio_calificaciones():
        
    valores = [5]
       
    while valores<5:
        calificacion= int(input("ingreasa la Calificación: "))
        if calificacion ==  0:
            break 
        else:
            valores.append(calificacion)
            
    promedio = valores / len(valores)
            
    print("Tu promedio es de:",promedio)   
    print(valores) 