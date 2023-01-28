# 2. Mamy do despozycji plik baseball.txt
# Należy wyświetlić wszystkich zawodnikaów z drużyny 'OAK'
# Którzy zawodnicy rzucili najwięcej za trzy punkty?
# Którzy zawodnicy rzucili najwięcej za trzy punkty średnio w jednym meczu?

if __name__ == "__main__":
    f = open("baseball.txt", "r")
    print("Zawodnicy drużyny OAK:")
    for line in f.readlines()[1:]:
        line = line.split()
        if line[3] == "OAK":
            name = line[0] + " " + line[1]
            if name[0] == "*" or name[0] == "#":
                name = name[1:]
            print(name)
    f.close()
    print("Najwięcej rzutów za trzy:")
    f = open("baseball.txt", "r")
    w = f.readlines()
    m = w[1]
    m = m.split()
    for x in w[1:]:
        x = x.split()
        if x[9] > m[9]:
            m = x

    name = m[0] + " " + m[1]
    if name[0] == "*" or name[0] == "#":
        name = name[1:]
    print(name)
    f.close()
    print("Najwięcej rzutów za trzy średnio na mecz:")
    f = open("baseball.txt", "r")
    w = f.readlines()
    m = w[1]
    m = m.split()
    for x in w[1:]:
        x = x.split()
        if (float(x[9]) / float(x[4])) > (float(m[9]) / float(m[4])):
            m = x

    name = m[0] + " " + m[1]
    if name[0] == "*" or name[0] == "#":
        name = name[1:]
    print(name)
    f.close()
