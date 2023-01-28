# 4. Wykorzystć moduł pickle do zapisania w pliku dane.dat
# wygenerowanych 10000 liczb całkowitych o wartości od 0 do 100.
# Następnie czytamy dane z tego pliku i szukamy, które z wygenerowanych liczb jest najwięcej.
import pickle
import random

if __name__ == "__main__":
    wynik = []
    wylosowane_liczby_plik = open("dane.dat", "wb")
    for i in range(10000):
        m = random.randint(0, 100)
        wynik.append(m)
    pickle.dump(wynik, wylosowane_liczby_plik)
    wylosowane_liczby_plik.close()
    wylosowane_liczby_plik = open("dane.dat", "rb")
    data = pickle.load(wylosowane_liczby_plik)
    wszystkie_liczby = []
    for i in range(len(data)):
        wszystkie_liczby.append(data[i])
    wylosowane_liczby_plik.close()
    print("Najczęściej pojawia się liczba: ", max(wszystkie_liczby, key=wszystkie_liczby.count))
