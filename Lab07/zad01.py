# 1. Wyświetlamy, każdą kolumnę i wartości w kolumnie występujące w pliku california1.txt.
# Całość zapisujemy do pliku california.csv jako plik tekstowy z separatorem średnik ';'.
# Jaka jest populacja ludzi we wszystkich miastach w przedziale wieku 18 - 64 lata
# i jaki to procent wszystkich ludzi. Plik california1.txt jest taki sam jak pobrany w poprzednich zajęciach.

if __name__ == "__main__":
    f = open("california1.txt", "r")
    g = open("california.csv", "w")
    for line in f.readlines():
        print(line)
        line = line.split()
        x = ";"
        line = x.join(line)
        g.write(line + '\n')
    f.close()
    g.close()
    h = open("california.csv", "r")
    populacja18_64 = 0
    poplacja_wszyscy = 0
    for line in h.readlines()[1:]:
        line = line.split(";")
        z = float(line[-5])
        y = float(line[-3])
        populacja18_64 += (z * y) / 100
        poplacja_wszyscy += float(line[-5])
    print("Populacja ludzi 18-64: ", int(populacja18_64),
          "\nProcent w całej populacji {:0.2f}%".format(populacja18_64 / poplacja_wszyscy))
