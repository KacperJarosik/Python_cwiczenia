# 9. Utworzyć w pamięci RAM tabelę z autonumeracją pola ID.
# conn = sqlite3.connect(':memory:')
# Zrealizować wstawianie danych na podstawie listy (tuple).
# Dodatkowo wstawianie i prezentacja danych powinna być zrealizowana na podstawie opracowanej do tego funkcji.
# Opracowane funkcje mają przyjmować określone atrybuty w zależności od ich przeznaczenia.
# Zaprezentować prawidłowe działanie tych funkcji
# import sqlite3
# def czytaj_dane():
#     """Funkcja pobiera i wyświetla dane z bazy."""
# def utworz_tabele(): #gotowa funkcja
#     """Tworzenie tabeli bez parametrów"""
#     conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
#     (ID INTEGER PRIMARY KEY ASC,
#     NAME TEXT NOT NULL,
#     AGE INT NOT NULL,
#     ADDRESS CHAR(50),
#     SALARY REAL);''')
# def wstaw_dane(lista):
#     """Wstawiamy wiele rekordów na podstawie listy tuple"""
import sqlite3


def czytaj_dane():
    # """Funkcja pobiera i wyświetla dane z bazy."""
def utworz_tabele():  # gotowa funkcja
    conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
    (ID INTEGER PRIMARY KEY ASC,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL);''')
def wstaw_dane(lista):
    for k in lista:
        #Poprawić cur.executemany
        conn.execute("INSERT INTO EMPLOYEES VALUES ",lista[k],";")
    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect(':memory:')
    lista=[(7,'Jan',32,'Warszawa',20000.00),(8,'Piotr',25,'Łódź',15000.00),(9,'Adam',32,'Kraków',15000.00)]
    wstaw_dane(lista)
