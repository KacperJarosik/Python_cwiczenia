# 4. Na podstawie funkcji z zadania 3, tworzymy funkcję sum_all(a,b), 
#    która liczy sumę liczb parzystych i nieparzystych razem. 
#    Nie definiujemy od początku sumowania wszystkich liczb od początku tylko wykorzystujemy funkcję sum(typ,a,b)
import zad03


def sum_all(a, b):
    suma = zad03.sum_even(True, a, b)
    suma += zad03.sum_even(False, a, b)
    return suma


if __name__ == '__main__':
    suma = 0
    a = int(input('Podaj liczbe = '))
    b = int(input('Podaj liczbe = '))
    print(sum_all(a, b))
