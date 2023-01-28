# app05
# wyświetl tabliczkę mnożenia (instrukcja for - 9 kolumn i 9 wierszy)
for i in range(1, 10):
    for m in range(1, 10):
        x = m * i
        if x < 10:
            print("", x, end=" ")
        else:
            print(x, end=" ")
        m += 1
    print("\n")
    i += 1
