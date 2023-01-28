# Napisz wyrażenie regularne dla numeru PESEL
import re

if __name__ == '__main__':
    liczba = '81020366662'
    wynik = re.match('^\d{11}$', liczba, re.IGNORECASE)
    if wynik:
        print('Ok')
    else:
        print('No')
