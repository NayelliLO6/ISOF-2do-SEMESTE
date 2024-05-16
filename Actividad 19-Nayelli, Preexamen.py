# indice de masa corporal

def masa_corporal(a,b):
    return (a/b*b)

print("Calcularemos su indice de masa corporal")

Peso=int(input("Cuanto pesa? "))
Estatura=int(input("Cuanto mides?"))

print(f" El indice de masa corporal es: {masa_corporal}")