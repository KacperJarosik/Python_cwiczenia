# app02
# Do zadania numer 1 dodajemy wyświetlanie typu zmiennej a,b,c (funkcja type())
# Sprawdź jak działa funkcja isinstance() do sprawdzenia i wyświetlenia typu danych danej zmiennej.
a = float(input('Podaj a = '))
b = input('Podaj b = ')
c = a + float(b)
# wyniki
print('wynik = ', c)
print(type(a))
print(type(b))
print(type(c))

#if isinstance(c,(int,float)):
#    print('typ int lub float')
#else:
#    print('inny typ')

input('Press any key !')
