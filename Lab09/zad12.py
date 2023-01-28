# Zadanie 12 (do przeanalizowania)
# W tym zadaniu wczytujemy i analizujemy plik utworzony w poprzenim zadaniu
#
# - Zaimportuj moduł os
# - Wczytaj od użytkownika ścieżkę dostępu do pliku utworzonego w poprzednim zadaniu. Wynik zapisz w zmiennej filename
# - Uwaga: ścieżka wprowadzona przez użytkownika mogła wskazywać na nieistniejący plik, dlatego napisz pętlę while, która będzie się wykonywać tak długo aż użytkownik wprowadzi ścieżkę do istniejącego pliku. Możesz w tym celu korzystać z funkcji os.path.isfile
# - Jeżeli plik nie istnieje to w pętli wyświetl komunikat i poproś o ponowne wprowadzenie poprawnej ścieżki
# (na tym etapie masz wczytaną ścieżkę do istniejącego pliku)
# - Zadeklaruj zmienną webaddresses, która będzie pustą listą
# - Otwórz plik wskazywany przez filename na odczyt. Wczytuj zawartość pliku linijka po linijce, zamieniaj w tak wczytanej linii znak końca linii (\n) na napis pusty i dodawaj wczytane linie do zmiennej webaddresses
# - W zależności od sposobu otwarcia pliku, może być wymagane zamknięcie pliku
# - Dla każdej linijki znajdującej się na liście webaddresses, jeżeli ta linijka kończy się na .pl to wyświetl "adres+...+ jest adresem z Polski" w przeciwnym razie wyświetl "adres ... nie jest adresem z Polski"

#-------------------------------------------------------------------------------------------------------

import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')

