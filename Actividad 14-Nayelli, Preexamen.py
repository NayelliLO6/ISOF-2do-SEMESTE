
#palabra mas larga de una lista de palabras

def palabra_mas_larga(lista):
    palabra_mas_larga = ""
    for palabra in lista:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga
    
lista = ["cinta", "lista", "cacahuate", "codigo", "palabras"]
resultado = palabra_mas_larga(lista)
print("La palabra más larga de mi lista es:", resultado)