# Pobierz i zainstaluj Sqlite Tools oraz SQLiteBrowserPortable.
# I. Pobieramy narzędzia linii poleceń SQLite Tools ze strony https://sqlite.org/download.html
# -- link do pliku:
# https://www.sqlite.org/2022/sqlite-tools-win32-x86-3400000.zip
#
# II. Pobieramy DB Browser for SQLite - PotabaleApp ze strony https://sqlitebrowser.org/dl/
# -- link do pliku
# https://download.sqlitebrowser.org/SQLiteDatabaseBrowserPortable_3.12.2_English.paf.exe

# Zadania do wykonania
# 1. Urucham program sqlite3.exe, utwórz bazę danych test.db w aktualnym katalogu programu
#    i sprawdź polecenie .databases
# 2. Utwórz tabelę Emp
#   create table Emp (id INTEGER PRIMARY KEY, name TEXT, salary NUMERIC);
# 3. Wstaw trzy rekordy do bazy
#   insert into Emp values (1,'John',250),(2,'Adam',150.344),(3,'Sara',200.9);
# 4. Wyświetl wprowadzone dane
#   select * from Emp;
# 5. Wybierz tylko osoby, które zarabiają więcej niż 150.00 i posortuj względem pensji
#   select id, name, salary from Emp where salary >=200 order by salary;
# 6. Wyświetl istniejące tabele w bazie poleceniem
#   .tables
# 7. Wyjdź z programu poleceniem
#   .quit
# 8. W narzędziu DB Browser for SQLite - PotabaleApp otwieramy bazę test.db
#   i sprawdzamy czy tabela Emp istnieje i wykonujemy zapytanie jak w pkt. 5.
# 9. Tworzymy własną tabelę Customers z polami ID, NAME, CITY.
#   Wypełnij przykładowymi danymi (3 rekordy)
#   Wyświetl wszystkie elementy posortowane wg. pola NAME
# 10. Kończymy pracę z narzędziem.

# W następnych zadaniach wykorzystujemy tylko język Python do operacji na bazie danych.
