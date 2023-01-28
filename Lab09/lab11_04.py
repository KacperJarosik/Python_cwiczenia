# 4. Do tabeli: EMPLOYEES wprowadzić 3-4 krotki (rekordy).
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('test1.db')
    print('połączaenie z bazą danych - nawiązane')

    conn.execute("INSERT INTO EMPLOYEES VALUES (4,'Kamil',36,'Opole',12000.00);")
    conn.execute("INSERT INTO EMPLOYEES VALUES (5,'Kacper',20,'Gdańsk',23000.00);")
    conn.execute("INSERT INTO EMPLOYEES VALUES (6,'Krzysztof',64,'Malbork',8000.00);")
    conn.commit()
    conn.close()
    print('Połączenie z bazą danych - zakończone')
