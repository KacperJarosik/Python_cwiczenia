# app01 
# Podaj z klawiatury dwie liczby pod zmienne a oraz b (funkcja input()).
# Następnie dodaj te dwie liczby i wyświetl wynik
# Zakładamy, że podajemy liczby całkowite lub zmiennoprzecinkowe (nie sprawdzamy tego)

a = float(input('Podaj a = '))
b = input('Podaj b = ')
c = a + float(b)
# wyniki
print('wynik = ', c)


#if isinstance(c,(int,float)):
#    print('typ int lub float')
#else:
#    print('inny typ')

input('Press any key !')
