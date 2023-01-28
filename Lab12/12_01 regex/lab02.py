# sprawdź czy adres email jest poprawny
# sprawdzić czy email postaci student@p.lodz.pl oraz student@p..pl
# jest poprawny (jeśli nie to poprawić wyrażenie regularne)
import re

email = 'student@p.lodz.pl'

wynik = re.match('^[A-Z0-9._+%-]+@[A-Z0-9-.]+\.[A-Z]{2,}$', email, re.IGNORECASE)
zabroniony_ciag_znakow = '\.\.'
print(wynik)
if wynik:
    if re.search(zabroniony_ciag_znakow, email):
        print('No')
    else:
        print('Ok')
else:
    print('No')
