# 1. Zapisywanie sesji gry (np. rzucanie dwoma kostkami aż wyrzucimy 6,6) do pliku dla danej osoby,
# ilości rzutów w danej sesji, daty
import random
import datetime

if __name__ == "__main__":
    y = ""
    first = 0
    second = 0
    how_many = 0
    while first != 6 or second != 6:
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        how_many += 1
        print(first, second)
    # print(how_many)

    f = open("wyniki1.txt", 'a')
    # y=f.readline()
    print(y)
    y = str(how_many)
    y += " - "
    y += str(datetime.datetime.now())
    y += ",\n"
    print(y)
    f.write(y)
    f.close()
