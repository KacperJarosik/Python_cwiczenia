# 1. Sprawdź czy podana liczba jest parzysta czy nieparzysta 
#    (definiujemy funkcję is_even(a), która zwraca True lub False (typ bool))

def is_even(a):

   if a % 2 == 0:
      return True
   else:
      return False

if __name__ == '__main__':
   a = int(input('Podaj liczbe = '))
   print(is_even(a))