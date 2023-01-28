# 5. Wykorzystaj moduł datetime do podania w jednej linijce
#   rok-miesiąc-dzień oraz godzina:minuty:sekundy
#   w danym momencie z wykorzystaniem najnowszego formatowania danych f-string (f').
import datetime
import time

if __name__ == '__main__':
    now = datetime.datetime.now()
    rok = now.year
    miesiac = now.month
    dzien = now.day
    godzina = now.hour
    minuta = now.minute
    sekunda = now.second
    print(f"{rok}-{miesiac}-{dzien}     {godzina}:{minuta}:{sekunda}")
