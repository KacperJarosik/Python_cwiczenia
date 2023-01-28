# 6. Tabliczka mnożenia od 1..10 z tym, że liczby wyrównujemy w kolumnach do prawej strony (liczymy do 100)
for i in range(1, 11):
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
