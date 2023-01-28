# sprawdź czy kod pocztowy jest poprawny
# (poza kodem nic nie może się pojawiać w zmiennej o nazwie kod,
# np. jeśli kod = '45-51711' to wynik poprawności kodu jest negatywny)
import re

kod = '45-517'
# wynik = re.match('[0-9][0-9]-[0-9][0-9][0-9]', kod)
# wynik = re.match('[0-9]{2}-[0-9]{3}', kod)
# wynik = re.match('\d{2}-\d{3}', kod)
# wynik = re.search('\d{2}-\d{3}', kod)
wynik = re.fullmatch('\d{2}-\d{3}', kod)
# czym się różni re.match od re.fullmatch czy re.search?
# fullmatch - dokładne dopasowanie, match sprawdzka początek stringa,
# search - szuka dowolnego dopasowania w stringu

# Wykorzystaj każdą z funkcji.

print(wynik)
if wynik:
    print('Ok')
    print(kod)
else:
    print('No')
