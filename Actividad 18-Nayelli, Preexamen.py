#Peliculas 


Lista_peliculas = {
    "valiente": "Todas las edades",
    "Chucky": "Mayores de 18 años",
    "cenicienta": "Todas las edades",
    "Deadpool": "Mayores de 18 años",
    "El rey león": "Todas las edades"
    }

print(Lista_peliculas)
Edad=int(input("ingresa tu edad: "))

if Edad>=18:
    print(f"peliculas que puedes ver: ",Lista_peliculas)
elif Edad<18:
    print(Lista_peliculas[0,2,3])