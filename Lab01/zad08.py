# app08
# Rzucamy czterema kośćmi aż wyrzucimy cztery szóstki lub cztery jedynki
# jednocześnie liczymy ile razy losowaliśmy aby zaistniała taka sytuacja.
# Wyświetlamy tylko ilość rzutów oraz informację czy wyrzuculiśmy jedynki czy szóstki 
# import random
#
# d1 = 0
# d2 = 0
# d3 = 0
# d4 = 0
# acount = 0
# while True:
#     acount += 1
#     d1 = random.randint(1, 6)
#     d2 = random.randint(1, 6)
#     d3 = random.randint(1, 6)
#     d4 = random.randint(1, 6)
#     if d1 == d2 and d2 == d3 and d3 == d4 and (d4 == 1 or d4 == 6):
#         print(d1, d2, d3, d4)
#         print("Liczba prob:", acount)
#         break
# Modyfikujemy naszą aplikację aby można rzucać maksymalnie 100 kośćmi - podawanych z klawiatury.
import random

x = 0
d1 = 0
d2 = 0
d3 = 0
d4 = 0
acount = 0
while True:
    n_dices = int(input('Podaj liczbe kosci max 100 '))
    if 0 < n_dices <= 100:
        break
while True:
    acount += 1
    dn = []
    for i in range(0, n_dices):
        # dn[i] = random.randint(1, 6)
        dn.append(random.randint(1, 6))
        i += 1
    if dn[0] == 1 or dn[0] == 6:
        for i in range(1, n_dices):
            if dn[i - 1] != dn[i]:
                break
            i += 1
        if i == n_dices:
            x = 1
    if x == 1:
        print("Liczba prob:", acount, "wylosowane cyfry:", dn[0])
        break
    print(acount)
