# 2. Oblicz sumę liczb parzystych sum_even(a,b) z przedziału podanego jako parametry funkcji 
#   (korzystamy z funkcji is_even(a) z zadania 1, która zwraca True lub False 
#   - wykorzystujemy instrukcję import zad01 albo from zad01 import * ).
#   W pliku zad01.py dodajemy w kodzie w odpowiednim miejscu sprawdzenie czy if __name__ == '__main__':
import zad01


def sum_even(a, b):
    suma = 0
    for i in range(a, b):
        if zad01.is_even(i):
            suma += i
    return suma


if __name__ == '__main__':
    a = int(input('Podaj liczbe = '))
    b = int(input('Podaj liczbe = '))
    print(sum_even(a, b))
