# 6. Jaka to liczba? Komputer wybiera losowo liczbę z zakresu od 1 do 100.
#    Gracz próbuje ją odgadnąć, a komputer go informuje,
#    czy podana przez niego liczba jest:
#    za duża, za mała, prawidłowa
#    (na końcu podajemy ile liczb podaliśmy aby zgadnąć wylosowaną liczbę)
import random

if __name__ == '__main__':
    x = random.randint(1, 100)
    while True:
        y = int(input('Zgadnij jaka wylosowana liczbe calkowita od 1 do 100\n'))
        if y == x:
            print('Brawo!!!\nZgadles prawidlowa liczbe')
            break
        if y < x:
            print('Podana liczba jest za mala\n')
        if y > x:
            print('Podana liczba jest za duza\n')
