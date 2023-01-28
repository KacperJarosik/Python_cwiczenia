results = []
f = open("dane.dat", "r")
# wczytujemy wiersze, pomijamy komentarz
lines = f.readlines()[4:]
# zamykamy plik
f.close()
# wydobywamy dane z wczytanych ciągów znaków
for line in lines:
    # dzielimy wiersz na pola
    fields = line.split(' ')
    # zamieniamy napisy na liczby
    time = float(fields[0])
    pos = float(fields[1])
    vel = float(fields[2])
    # dopisujemy do listy z wynikami
    all = (time, pos, vel)
    results.append(all)
# sprawdzamy wynik
for i in results[0:]:
    print(i)
