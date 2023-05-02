
romanos = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

numero = 'md'


def convertir_romano_a_decimal(numero_romano):
    if len(numero_romano) == 1:
        return romanos[numero_romano]
    else:
        if romanos[numero_romano[0]] >= romanos[numero_romano[1]]:
            return romanos[numero_romano[0]] + convertir_romano_a_decimal(numero_romano[1:])
        else:
            return - romanos[numero_romano[0]] + convertir_romano_a_decimal(numero_romano[1:])

print("El numero romano",numero, "equivale a",convertir_romano_a_decimal(numero), "en decimal.")