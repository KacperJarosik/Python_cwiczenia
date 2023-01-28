# 2. Utworzyć i nawiązać połączenie do bazy test.db w bieżącym katalogu:
# (można także skopiować wcześniej utworzoną bazę danych test.db)
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('test1.db')
    print("Połączenie z bazą danych - nawiązane");
    conn.close()
    print("Połączenie z bazą danych - zakończone ");
