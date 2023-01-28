# 5. Wykorzystanie modułu shelve do zapisania rzutów dwoma kostkami,
# aż do wyrzucenia wartości 12 (zapisujemy kolejne sumy).
# Powtarzamy tą operację jeszcze 10 razy i każdą z serii zapisujemy do nowego zestawu danych.
# Następnie czytamy dane z pliku i podajemy ile rzutów potrzebujemy, w każdej serii
# do wyrzucenia sumy równej 12. Następnie liczymy jedną wartość średnią z wszystkich serii.
import random

if __name__ == "__main__":
    plik = open("zad05.txt", "w")
    for k in range(10):
        seria = []
        while (1):
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            wynik = d1 + d2
            seria.append(wynik)
            if wynik == 12:
                break
        plik.write(str(seria) + "\n")
    plik.close()
    plik = open("zad05.txt", "r")
    ilosc_rzutow = 0
    numer_serii = 1
    for i in plik.readlines():
        i = i.split(",")
        print("W serii ", numer_serii, ". wykonano ", len(i), " rzutów")
        ilosc_rzutow += len(i)
        numer_serii += 1
    print("Średnio potrzebujemy ", int(ilosc_rzutow / 10), " rzuty aby suma kostek wynosiła 12")
