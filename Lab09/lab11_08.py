# 8. Obsługa błędu np. przy tworzeniu tabeli, która już istnieje
# (bez IF NOT EXISTS w poleceniu CREATE TABLE)
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('test1.db')
    print("Połączenie z bazą danych - nawiązane")
    try:
        conn.execute('''CREATE TABLE EMPLOYEES
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);''')
    except sqlite3.OperationalError:
        print("Tabela już istnieje")
    finally:
        if conn:
            conn.close()
            print("Połączenie z bazą danych - zakończone ")
