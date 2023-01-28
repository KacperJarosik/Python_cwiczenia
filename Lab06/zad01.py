# 1. Dana jest lista:
# lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 16, 256, 3, 19, 71, 21]
# Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej.
# Takich par liczb może być wiele
if __name__ == '__main__':
    lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 16, 256, 3, 19, 71, 21]
    for k in range(len(lista) - 1):
        if lista[k] * lista[k] == lista[k + 1]:
            print(lista[k], lista[k + 1])
