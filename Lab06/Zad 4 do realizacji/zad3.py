# 3. Zapisywanie trzech najlepszych wyników gry (np. rzucanie dwoma kostkami aż wyrzucimy 6,6) 
# do pliku score.txt i przechowujemy ilości rzutów w danej sesji, datę i czas w postaci YYYY-MM-DD HH24:MIN:SEC. 
# Jeżeli wynik jest taki sam a data jest starsza to nie zastępujemy jej.

import random
import datetime

if __name__ == "__main__":

    max = 0
    max_id = 0
    y = ""
    score = ["", "", ""]
    line = ["", "", ""]
    first = 0
    second = 0
    how_many = 0
    while first != 6 or second != 6:
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        how_many += 1
        # print(first,second)
    print(how_many)
    f = open("score.txt", 'r')
    for y in range(3):
        line[y] = f.readline()
        x = line[y].split(' ', 1)
        # print(x)
        score[y] = x[0]
        print(score[y])
    max = int(score[0])
    max_id = 0
    if int(score[1]) > int(score[0]):
        max = int(score[1])
        max_id = 1
        if int(score[2]) > int(score[1]):
            max = int(score[2])
            max_id = 2
    elif int(score[2]) > int(score[0]):
        max = int(score[2])
        max_id = 2
    for y in range(3):
        if how_many < int(max) or len(line) < 3:
            line[max_id] = str(how_many)
            line[max_id] += " - "
            line[max_id] += str(datetime.datetime.now())
            line[max_id] += ",\n"
            break
    print(line)
    f.close()
    f = open("score.txt", 'w')
    for i in line:
        f.write(i)  # add the whole zoo to the output.txt
    f.close()
