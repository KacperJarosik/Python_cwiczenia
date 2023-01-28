# 8. Rozwiązywanie równania kwadratowego w dziedzinie liczb rzeczywistych
#    - rozwiązanie tworzymy na początku bez funkcji ale
#    - docelowo definiujemy funkcje quadratic_equation(a,b,c) zwracjące listę w postaci [x1, x2, 'komentarz ile jest rozwiązań']
#    Podać przykład uruchomienia funkcji, gdzie mamy jedno rozwiązanie, 2 rozwiązania lub brak rozwiązania.
import math


def quadratic_equation(a, b, c):
    x1 = 0
    x2 = 0
    if a == 0:
        if b == 0:
            if c == 0:
                return 'Jest nieskonczonosc rozwiazan'
            else:
                return 'brak rozwiazan'
        x1 = (-c / b)
        return x1, 'Jest 1 rozwiązanie'
    delta = b * b - 4 * a * c
    if delta < 0:
        return 'brak rozwiazan'
    if delta == 0:
        x1 = (-b / 2 * a)
        return x1, 'Jest 1 rozwiazanie'
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        return x1, x2, 'Sa 2 rozwiazania'


if __name__ == '__main__':
    a = int(input('Podaj liczbe a = '))
    b = int(input('Podaj liczbe b = '))
    c = int(input('Podaj liczbe c = '))
    print(quadratic_equation(a, b, c))
    # a = 0,b = 1,c = 1 - 1 rozwiazanie
    # a = 1, b = 1, c = 2 - brak rozwiazan
    # a = 1, b = 6, c = -1 - 2 rozwiazania
    # a = 0, b = 0, c = 0 - nieskonczonosc rozwiazan
