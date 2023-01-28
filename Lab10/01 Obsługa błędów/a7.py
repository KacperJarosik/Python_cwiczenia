# Obsługa błędu przy otwieraniu pliku do odczytu, który nie istnieje.
if __name__=="__main__":
    try:
        tekst = open("witam", "r")
    except:
        print('Brak podanego pliku')