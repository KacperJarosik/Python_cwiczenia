# 9. Z wykładu definiujemy funkcję silnia(a)
#  i porównujemy wyniki z funkcją math.factorial().
#  Śledzimy za pomocą debugera wykonanie rekurencyjne naszej funkcji silnia.
#  Dodatkowo wykorzystujemy funkcję time() z biblioteki time do sprawdzenia,
#  które z obliczeń działa szybciej (sprawdzić dla dość dużych liczb)
import math
import time


def silnia(a):
    x =1
    for i in range(1, a+1):
        x = x * i
    return x


if __name__ == '__main__':
    a = int(input('Podaj warosc silni: '))
    print('twoja silnia to:', silnia(a))
    print(time.time())
    print('twoja silnia to:', math.factorial(a))
    print(time.time())