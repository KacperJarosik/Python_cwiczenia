# 6. Napisać funkcję find_word(filename_in, word),
# której zadaniem jest znalezienie wszystkich wierszy w pliku, które zawierają szukane słowo.
# Wszystkie wiersze, które zawierają słowo powinny zostać zapisane w
# pliku wynikowym filnename_out wraz z nr wiersza (z pierwszego pliku).
# Plik wejściowy to dowolny plik tekstowy.

if __name__ == '__main__':
    szukane_slowo = input("Podaj szukane slowo\n")
    # np. puzzle, are
    f = open("tekstdo6.txt", 'r')
    licznik = 0
    lista_wczytane = f.readlines()
    print("Szukane słowo jest w linijkach:")
    for i in range(len(lista_wczytane)):
        if szukane_slowo in lista_wczytane[i]:
            print(i, " ")
    f.close()
