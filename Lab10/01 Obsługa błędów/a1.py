# Obsługa wyjątków try/except

# brak obsługi wyjątków
num = float(input("Wprowadź liczbę: "))
print('------------------------------')

# obsługa wyjątków
try:
    num = float(input("Wprowadź liczbę: "))
except:
    print("Wystąpił jakiś błąd!")
print('------------------------------')

# obsługa konkretnego wyjątku
try:
    num = float(input("Wprowadź liczbę: "))
except ValueError:
    print("Podana zmienna nie jest liczbą !")
print('KONIEC SKRYPTU')
