# obsługa konkretnych wyjątków razem
try:
    num = float(input("Wprowadź liczbę: "))
    wynik = 1/num
except (ValueError, ZeroDivisionError):
    print("Podana zmienna nie jest liczbą lub dzielenie przez zero!")
print('------------------------------')
print(wynik)

# obsługa konkretnych wyjątków osobno
try:
    import xxx
    num = float(input("Wprowadź liczbę: "))
    wynik = 1/num
except ValueError:
    print("Podana zmienna nie jest liczbą !")
except ZeroDivisionError:
    print("Dzielenie przez zero !")
print('------------------------------')
print(wynik)
