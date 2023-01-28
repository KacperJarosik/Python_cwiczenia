# 10. Ostatni przykład, wstawić powyższe 3 funkcje do oddzielnego modułu modul_db.py
#   oraz wykonać powyższe funkcje (pamiętajmy, iż zmienna conn jest dostępna w ramach jedengo skryptu.
#   Jednak gdy przeniesiemy je do oddzielnego modułu to parametrem wejściowym powinna być zmienna conn)
    # modul_db.py
    # def czytaj_dane(connection):
    #     """Funkcja pobiera i wyświetla dane z bazy."""
    # def utworz_tabele(connection): #gotowa funkcja
    #     """Tworzenie tabeli bez parametrów"""
    #     connection.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
    #     (ID INTEGER PRIMARY KEY ASC,
    #     NAME TEXT NOT NULL,
    #     AGE INT NOT NULL,
    #     ADDRESS CHAR(50),
    #     SALARY REAL);''')
    # def wstaw_dane(lista,connection):
    #     """Wstawiamy wiele rekordów na podstawie listy tuple"""
