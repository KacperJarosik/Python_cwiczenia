# 7. Tabliczka mnożenia z wykorzystaniem instrukcji while i ewentualnie if (liczymy do 100) - efekt jak w zdaniu zad06.py
i = 1
while i < 11:
    for m in range(1, 11):
        x = m * i
        if x < 10:
            print("", x, end="  ")
        else:
            if x < 100:
                print("", x, end=" ")
            else:
                print(x, end=" ")
        m += 1
    print("\n")
    i += 1
