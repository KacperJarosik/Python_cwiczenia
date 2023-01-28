# należy sprawdzić działanie obsługi błędów uruchamiając skrypt z kolejnymi zakomentowanymi liniami
try:
    pass
    #raise NameError('Nowy błąd z opisem')
    #import xxx
    #a = 1/0
    #a = float('dane tekstowe')
except NameError as e1:
    print(e1)
except ZeroDivisionError as e1:
    print(e1)
except ModuleNotFoundError as e1:
    print(e1)
except:
    print('inne błędy')
    raise   #przekazanie błędu dalej
else:
    print ('Kod wykonywany gdy nie wystąpił żaden błąd - Wszystko OK')
finally:
    print('Kod zawsze wykonywany - OK')
