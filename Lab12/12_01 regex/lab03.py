# sprawdź ile adresów email jest poprawnych
import re

email = 'a1_f@wp.pl, a1_f@wp.pl,a3@wp.pl'

wynik = re.findall('[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', email, re.IGNORECASE)
print(wynik)
print(wynik.__len__())
if wynik:
    print('ok')
else:
    print('No')
