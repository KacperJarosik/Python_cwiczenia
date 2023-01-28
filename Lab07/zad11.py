# Zadanie 11 (do przeanalizowania)
# Napisz program, który zapyta użytkownika o adresy www i zapisze je w pliku.
#
# -Zaimportuj moduł os
# -Zadeklaruj pustą listę webaddresses
# -Poproś użytkownika o wprowadzenie adresu strony www. Wynik zapamiętaj w zmiennej line
# -Napisz pętlę, która będzie się wykonywać tak długo  póki line nie jest puste, a w tej pętli
# -Dodaj line do listy webaddresses i ponownie poproś użytkownika o wprowadzenie adresu strony www zapisując ją w zmiennej line
# (Kiedy użytkownik będzie chciał zakończyć wprowadzanie adresów wystarczy, że naciśnie ENTER. W tym przypadku zmienna web addresses będzie pusta i pętla while się zakończy. Na tym etapie będziesz już mieć listę webaddresses zawierającą wprowadzone przez użytkownika adresy)
# -W zmiennej dirname zapamiętaj ścieżkę do katalogu bieżącego
# -Poproś użytkownika o wprowadzenie nazwy pliku i wynik zapamiętaj w zmiennej filename)
# -Korzystając z funkcji os.path.join połącz ze sobą dirname i filename zapamiętując wynik w filepath
# -Otwórz plik znajdujący się pod ścieżką filename do zapisu. Zmienna wskazująca na plik może nazywać się file
# -Dla każdego z adresów znajdujących się na liście webaddresses zapisz ten adres dodając do niego znak nowej linii w pliku.
# -Zamknij plik
# (na tym etapie masz plik, którego zawartością są wprowadzone przez użytkownika adresy www)

#---------------------------------------------------------------------------------------------
import os

webaddresses = []
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
while line != '':
    webaddresses.append(line)
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')

print(webaddresses)
dirname = os.getcwd()
filename = input("Enter the file name (without directory): ")
filepath = os.path.join(dirname, filename)
file = open(filepath, 'w+')
for webaddress in webaddresses:
    file.write(webaddress + "\n")
file.close()

