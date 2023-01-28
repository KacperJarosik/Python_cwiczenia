results = []
f = open("dane.txt","r")
#iteracja po wierszach - w każdym kroku wczytywany tylko jeden wiersz
for line in f:
    #ignorujemy komentarz
    if line[0] == "#": continue
    #wydobycie danych tym razem bardziej "pythonowo"
    all = [float(val) for val in line.split()]
    results.append(all)
#zamykamy plik
f.close()
#sprawdzamy wynik
for i in results[0:]: print(i)