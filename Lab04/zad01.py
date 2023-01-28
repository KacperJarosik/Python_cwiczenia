# 1. Rozwiązywanie równania kwadratowego w dziedzinie liczb urojonych (zespolonych)
#    definiujemy funkcje quadratic_equation_im(a,b,c) zwracjące listę w postaci [x1, x2]
#    Podać przykład uruchomienia funkcji.
import math


def quadratic_equation_im(a, b, c):
    if a == 0:
        return 'Funkcja nie jest kwadratowa'
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        print(x1, ', ', x2)
    if delta == 0:
        x1 = (-b) / 2 * a
        print(x1)
    if delta < 0:
        delta = delta * (-1)
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        print(x1, 'i, ', x2, 'i')


if __name__ == '__main__':
    quadratic_equation_im(-8, 8, 9)
