# 9. Zapropnuj słownik lub listę do sprawdzenia oceny w zależności od liczby punktów
# podanej z klawiatury (do wyboru oceny od 2-5 stosujemy słownik lub listę)
# Jeżeli zmienią się zakresy na liście lub oceny to także wynik końcowy może być inny.
# 	5 - (80%-100%>
# 	4 - (60%-80%>
# 	3 - (50-60%>
# 	2 - <=50%>
import sys

if __name__ == '__main__':
    max_punkty = 20
    zdobyte_punkty = float(input("Ile zdobyles punktow?\n"))
    oceny = [0, 0.5 * max_punkty, 0.6 * max_punkty, 0.8 * max_punkty, max_punkty]
    if zdobyte_punkty < oceny[0] or zdobyte_punkty > oceny[4]:
        sys.exit(1)
    if zdobyte_punkty <= oceny[1]:
        print(2)
        sys.exit(0)
    if zdobyte_punkty <= oceny[2]:
        print(3)
        sys.exit(0)
    if zdobyte_punkty <= oceny[3]:
        print(4)
        sys.exit(0)
    print(5)
