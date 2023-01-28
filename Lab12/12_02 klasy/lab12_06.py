# Napisz klasę Ulamek,
# która przechowuje ułamki postaci a/b.
# Klasa przechowuje dwa pola: licznik i mianownik.
# Napisz metody:
# skroc(), skraca ułamek, wymaga obliczenia największego wspólnego dzielnika
# dodaj(), odejmij(), mnoz(), dziel() (statyczne) – obliczają odpowiednio sumę i iloczyn dwóch ułamków
import math


class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def wypisz(self):
        print(f"({self.licznik})/({self.mianownik})")

    def skroc(self):  # math.gcd() liczy największy współny dzielnik
        nwd = math.gcd(self.licznik, self.mianownik)
        self.licznik //= nwd
        self.mianownik //= nwd

    @staticmethod
    def dodaj(u1, u2):
        lewy_licznik = u1.licznik * u2.mianownik
        prawy_licznik = u2.licznik * u1.mianownik
        wynik = Ulamek(lewy_licznik + prawy_licznik, u1.mianownik * u2.mianownik)
        wynik.skroc()
        return wynik

    @staticmethod
    def odejmij(u1, u2):
        lewy_licznik = u1.licznik * u2.mianownik
        prawy_licznik = u2.licznik * u1.mianownik
        wynik = Ulamek(lewy_licznik - prawy_licznik, u1.mianownik * u2.mianownik)
        wynik.skroc()
        return wynik

    @staticmethod
    def mnoz(u1, u2):
        wynik = Ulamek(u1.licznik * u2.licznik, u1.mianownik * u2.mianownik)
        wynik.skroc()
        return wynik

    @staticmethod
    def dziel(u1, u2):
        wynik = Ulamek(u1.licznik * u2.mianownik, u1.mianownik * u2.licznik)
        wynik.skroc()
        return wynik


def main():
    u1 = Ulamek(1, 4)
    u2 = Ulamek(2, 6)
    u1.wypisz()
    u2.wypisz()
    u1.skroc()
    u1.wypisz()
    u2.skroc()
    u2.wypisz()
    print("Dodawanie")
    Ulamek.dodaj(u1, u2).wypisz()
    print("Odejmowanie")
    Ulamek.odejmij(u1, u2).wypisz()
    print("Mnozenie")
    Ulamek.mnoz(u1, u2).wypisz()
    print("Dzielenie")
    Ulamek.dziel(u1, u2).wypisz()


if __name__ == "__main__":
    main()
