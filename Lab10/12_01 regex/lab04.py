# sprawdź ile wyrazów PYthon pisany dowolnymi literami jest w zdaniu
import re

zdanie = 'PYTHON. To jest kolokwium z przedmiotu Programowanie skryptowe, ' \
         'które wykorzystuje język python. PythoN jest OK, PythON'

wynik = re.findall('python', zdanie, re.IGNORECASE)
print(wynik)
print(wynik.__len__())
wynik1 = re.sub('python', 'PYTHON', zdanie, flags=re.IGNORECASE)
print(wynik1)

wynik2 = re.split("\s", zdanie)
print(wynik2.__len__())
