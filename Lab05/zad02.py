# 2. Dana jest lista:
# lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]
# Oblicz sumę, wartość średnią, wartość minimalną i maksymalną z wykorzystaniem
# i bez korzystania z funkcji wbudowanych sum, min, max, len.
if __name__ == '__main__':
    lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]
    print(sum(lista))
    print(sum(lista) / len(lista))
    print(min(lista))
    print(max(lista))

    i = 0
    suma = 0
    minimum = lista[0]
    maximum = lista[0]
    for x in lista:
        suma += lista[i]
        if lista[i] < minimum:
            minimum = lista[i]
        if lista[i] > maximum:
            maximum = lista[i]
        i += 1
    print(suma)
    print(suma / i)
    print(minimum)
    print(maximum)
