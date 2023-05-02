objetos_en_mochila = ['Agua','Brujula','Comida','Mapa Estelar', 'Sable de Luz']

def usar_la_fuerza (objetos_en_mochila, objetos_fuera = 0):

    if len(objetos_en_mochila) == 0:
        print("La mochila está vacía")
        return objetos_fuera
    elif objetos_en_mochila[0] == "Sable de Luz":
        print(f"Se encontró un Sable de Luz en la Mochila")
        return objetos_fuera + 1
    else:
        return usar_la_fuerza(objetos_en_mochila[1:], objetos_fuera+1)

objetos_fuera = usar_la_fuerza(objetos_en_mochila)
print(f"Fue necesario sacar {objetos_fuera - 1} objetos de la mochila para encontrar el Sable de Luz")