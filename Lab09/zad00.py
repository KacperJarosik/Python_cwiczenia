# 0. (zadanie z ostatnich zajęć)
# - nie kopiujemy pliku do danego katalogu, tylko próbujemy otworzyć plik z katalogu Lab08)
# Mamy plik tekstowy z danymi medycznymi california1.txt
# Należy podać ile jest w danym pliku linii,
# Następnie ile jest kobiet i mężyczyzn
# (sprawdzić czy istnieją rekordy gdzie nie pojawia się informacja jaka jest płeć - wypisać te rekordy)
# Podać ilość precentowy kobiet i męzczyzn w tej populacji.
if __name__ == "__main__":
    plik = open("california1.txt", "r")
    ile_kobiet = 0
    ile_mezczyzn = 0
    ile_lini = 0
    cala_populacja = 0
    for line in plik.readlines()[1:]:
        ile_lini += 1
        line = line.split()
        ile_mezczyzn += int(float(line[-1]) / 200 * float(line[-5]))
        ile_kobiet += int(line[-5]) - int(float(line[-1]) / 200 * float(line[-5]))
        cala_populacja += int(line[-5])
    print("Tekst ma ", ile_lini, " linii")
    print("Ilość mężczyzn: ", ile_mezczyzn)
    print("Ilość kobiet: ", ile_kobiet)
    print("Procentowa lość mężczyzn w populacji : %.2f " % (ile_mezczyzn / cala_populacja), "%")
    print("Procentowa lość kobiet w populacji : %.2f " % (ile_kobiet / cala_populacja), "%")
