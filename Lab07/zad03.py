# 3. Czytamy wszystkei dane z pliku cereals.csv (wykorzystać moduł csv)
# Dodajemy do pliku cereals.csv na końcu jednego wiersza z dowolnymi danymi.
# np. "Miodek","G ","C ",100,4,2,340,1,16,8,60,25,1,1,0.75,3.755922,1,0,0,0,1,0,0
if __name__ == "__main__":
    tekst = open("cereals.csv", "r")
    for line in tekst.readlines():
        print(line)
    tekst.close()
    tekst = open("cereals.csv", "a")
    x = "\"Miodek\", \"G\" , \"C\" , 100, 4, 2, 340, 1, 16, 8, 60, 25, 1, 1, 0.75, 3.755922, 1, 0, 0, 0, 1, 0, 0"
    tekst.write(x + "\n")
    tekst.close()
