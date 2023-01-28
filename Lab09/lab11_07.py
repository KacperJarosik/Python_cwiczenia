# 7. Napisać skrypt, który usunie z tabeli EMPLOYEES rekordy o ID <=2 (polecenie DELETE)
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('test1.db')
    print("Połączenie z bazą danych - nawiązane")
    conn.execute("DELETE from EMPLOYEES where ID<=2;")
    conn.commit()
    print("Total number of rows deleted: ", conn.total_changes)
    cursor = conn.execute("SELECT id, name, address, salary from EMPLOYEES")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    conn.close()
    print("Połączenie z bazą danych - zakończone")
