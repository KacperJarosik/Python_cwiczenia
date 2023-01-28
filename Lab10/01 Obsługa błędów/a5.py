# propagacja błędów dalej, obsługa błędów w funkcji - example2
def x():
    try:
        import xyz
        wynik = 1/0
    except ValueError as e:
        print('Komunikat1 :', e)
    except ZeroDivisionError as e1:
        print('Komunikat2 :', e1)
    except Exception as e:
        print('Komunikat3 :', e)
        raise

try:
    x()
except Exception as e:
    print('Błąd zew.', e)

