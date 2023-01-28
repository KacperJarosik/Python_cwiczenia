# 11. Pobierz od użytkownika n liczb i zapisz je na liście.
# Wydrukuj: elementy listy i ich indeksy (enumerate),
# elementy w odwrotnej kolejności, posortowane elementy.
# Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika.
# Usuń z listy element o podanym indeksie.
# Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.
# Wybierz z listy elementy od indeksu i do j.
if __name__ == '__main__':
    lista = []
    info = int(input("ile chcesz podać liczb?\n"))
    for i in range(info):
        lista += input("Podaj liczbe\n")
    for i in range(info):
        print(lista[i], i)
    print("\n")
    for i in range(info):
        print(lista[info - i - 1], info - i - 1)
    print(lista)
    x = input("Jaka liczbe chcesz usunąć?\n")
    lista.remove(x)
    print(lista)
    x = int(input("Z jakiego indeksu chcesz usunąć liczbę?\n"))
    lista.pop(x)
    print(lista)
    x = input("Jakiej liczby chcesz zliczyć ilość powtórzeń?\n")
    print(lista.count(x))
    if lista.count(x):
        print(lista.index(x))
    else:
        print("Brak elementu w liście")
    print(lista)
    x = int(input("Podaj pierwszy i ostatni indeks elementow listy, które wyświetlić\n"))
    y = int(input())
    print(lista[x:y + 1])
