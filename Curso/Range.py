# range(): Crea una lista inmutable de números enteros en sucesión aritmética.

def opcion29():
    numeros = range(5) # [0, 1, 2, 3, 4]

    print(numeros[1])

    numeros1 = range(4, 10) # [4, 5, 6, 7, 8, 9, 10]
    print(numeros1[5])

    numeros2 = range(10, 100, 8)
    print(numeros2[9])