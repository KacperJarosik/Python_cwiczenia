# 3. Dokładamy dodatkowy parametr podający jakie liczby chcemy wybrać 
#    suma(typ,a,b), gdzie typ jest typ to True lub False. 
#    True oznacza liczby parzyste, False liczby nieparzyste.
import zad01


def sum_even(typ, a, b):
    suma = 0
    if typ:
        for i in range(a, b):
            if zad01.is_even(i):
                suma += i
    else:
        for i in range(a, b):
            if not zad01.is_even(i):
                suma += i
    return suma


if __name__ == '__main__':
    typ = (input('Podaj typ parzyste - True, Nieparzyste - False\n'))
    a = int(input('Podaj liczbe = '))
    b = int(input('Podaj liczbe = '))
    if typ == 'False':
        print(sum_even(False, a, b))
    else:
        print(sum_even(True, a, b))
