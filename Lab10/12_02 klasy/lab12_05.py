# Napisz klasę LiczbaZespolona
# która przechowuje liczby zespolone: a+bi.
# Niech część rzeczywista nazywa się re (od real),a urojona im (od imagine).
# Poza tymi dwoma polami zdefiniuj metody:
# - modul(), oblicza moduł liczby zespolonej a+bi: sqrt(a**2+b**2)
# - add(), multiply(), subtract() (statyczne); obliczają odpowiednio sumę, iloczyn, rożnicę dwóch liczb zespolonych
# oraz zdefiniować metodę dzielenia dóch liczb division()
import math


class Zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def wypisz(self):
        if self.im < 0:
            print(f"{self.re}{self.im}i")
        else:
            print(f"{self.re}+{self.im}i")

    def modul(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

    @staticmethod
    def dodaj(z1, z2):
        return Zespolona(z1.re + z2.re, z1.im + z2.im)

    @staticmethod
    def odejmij(z1, z2):
        return Zespolona(z1.re - z2.re, z1.im - z2.im)

    # (a+bi) * (c+di) = ac-bd + (bc+ad)i
    @staticmethod
    def mnoz(z1, z2):
        a = z1.re
        b = z1.im
        c = z2.re
        d = z2.im
        # return Zespolona(a*c-b*d, b*c+a*d)
        ze1 = (complex(z1.re, z1.im) / complex(z2.re, z2.im)).real
        ze2 = (complex(z1.re, z1.im) / complex(z2.re, z2.im)).imag
        return Zespolona(ze1, ze2)


def main():
    z1 = Zespolona(3, 4)
    z2 = Zespolona(2, 6)
    z1.wypisz()
    print(z1.modul())
    Zespolona.dodaj(z1, z2).wypisz()
    Zespolona.odejmij(z1, z2).wypisz()
    x1 = Zespolona.mnoz(z1, z2)
    print(type(x1), x1.im)


if __name__ == "__main__":
    main()
