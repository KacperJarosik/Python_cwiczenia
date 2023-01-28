# 3. W bazie danych test1.db założyć tabelę (na podstawie materiałów z wykładów):
#   EMPLOYEES z kolumnami:
#   - ID
# 	- NAME
# 	- AGE
# 	- ADDRESS
# 	- SALARY
#   Zaproponować właściwe typy danych w każdej z kolumn dla bazy sqlite.
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('test1.db')
    print('połączaenie z bazą danych - nawiązane')
    conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEES
    (ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL);''')
    print('Tabela utworzona - poprawnie')

    conn.execute("INSERT INTO EMPLOYEES VALUES (1,'Jan',32,'Warszawa',20000.00);")
    conn.execute("INSERT INTO EMPLOYEES VALUES (2,'Piotr',25,'Łódź',15000.00);")
    conn.execute("INSERT INTO EMPLOYEES VALUES (3,'Adam',32,'Kraków',15000.00);")
    conn.commit()
    conn.close()
    print('Połączenie z bazą danych - zakończone')
