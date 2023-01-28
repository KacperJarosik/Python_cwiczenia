# próba obsługi błędów danych podanych z klawiatury (np. 'a', 0, 1)
# Obsługa wyjątków try/except
# obsługa konkretnych wyjątków osobno
# argument wyjątku
# składnia else i finally

try:
    num = float(input("Wprowadź liczbę: "))
    wynik = 1/num
except ValueError as e:
    print("Komunikat 1 :",e)
except ZeroDivisionError as e:
    print("Komunikat 2 :",e)
else:
    print('Ok')
    print(num)
    print(wynik)
finally:
    print('Koniec skryptu')
