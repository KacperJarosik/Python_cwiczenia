# 5. Napisać skrypt, który pobierze i wyświetli wszystkie krotki z tabeli EMPLOYEES.
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('test1.db')
    print("Połączenie z bazą danych - nawiązane")

    cursor = conn.execute("SELECT  id, name, address, salary from EMPLOYEES")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
        conn.close()
        print("Połączenie z bazą danych - zakończone")
