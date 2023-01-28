# 8. Zadanie (do przeanalizowania z funkcjami z modułu os)
# Etapy:
# 1. Zaimportuj moduły os i time
# 2. Poproś użytkownika o wprowadzenie ścieżki dostępu do katalogu i zapisz pobrany napis w zmiennej dir
# 3. Jeśli wprowadzony napis nie wskazuje na katalog, wyświetl komunikat i zakończ skrypt
# 4. W przeciwnym razie poproś użytkownika o wprowadzenie nazwy pliku i zapisz pobrany napis w zmiennej file
# 5. Korzystając z odpowiedniej funkcji modułu os połącz ze sobą katalog z plikiem tworząc pełną ścieżkę. Wynik zapamiętaj w zmiennej path
# 6. Jeżeli plik wskazywany przez path nie istnieje, wyświetl komunikat i zakończ skrypt
# 7. Wyświetl informację o tym, że poniżej będą wyświetlane właściwości pliku path, a potem wyświetl:
# - datę ostatniej modyfikacji
# - rozmiar w bajtach
# - informację o biżącym katalogu
# - ścieżkę względną do pliku
#
# ----------------------------------------------------------------------------------------------------------
import os
import time

dir = input('enter directory name: ')

if not os.path.isdir(dir):
    print("%s must be a directory" % dir)
else:

    file = input('enter filename saved in directory %s: ' % dir)

    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print('File %s does not exist!' % path)

    else:

        print('displaying properties of file %s' % path)

        print('Last modified date', time.localtime(os.path.getmtime(path)))
        print('Size in bytes', os.path.getsize(path))

        print('Current directory is: ', os.getcwd())
        print('Relative path to the file is', os.path.relpath(path))