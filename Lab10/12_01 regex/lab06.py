# Napisz wyrażenie regularne dla LICZB SZESTNASTKOWYCH
import re

liczba = '0678ABF'
wynik = re.match('^[0-9A-F]+$', liczba, re.IGNORECASE)
if wynik:
    print('Ok')
else:
    print('No')
