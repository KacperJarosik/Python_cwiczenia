# 6. Napisać skrypt, który zmodyfikuje składowane w tabeli EMPLOYEES dane
# (polecenie UPDATE) zwiększając o 10% wartość SALARY (dla wszystkich osób)
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('test1.db')
    print("Połączenie z bazą danych - nawiązane")
    conn.execute("UPDATE EMPLOYEES set SALARY = 1.1*SALARY")
    conn.commit()
    print("Total number of rows updated: ", conn.total_changes)
    cursor = conn.execute("SELECT id, name, address, salary from EMPLOYEES")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    conn.close()
    print("Połączenie z bazą danych - zakończone")
