# Napisz wyrażenie regularne dla CZASU w formacie hh:min.sec
import re

if __name__ == '__main__':
    liczba = '05:08.50'
    wynik = re.match('\d{2}:\d{2}.\d{2}', liczba, re.IGNORECASE)
    if wynik:
        print('Ok')
    else:
        print('No')
