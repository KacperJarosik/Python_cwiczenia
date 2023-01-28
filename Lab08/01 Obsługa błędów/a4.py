# propagacja błędów dalej, obsługa błędów w funkcji - example1
def x():
    try:
        a = float('dane tekstowe')
    except Exception as e2:
        print('obsługa wew.', e2)
        raise   #przekazanie błędu dalej

try:
    x()
except Exception as e:
    print('obsługa zew', e)