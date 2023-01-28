# 5. Czytanie danych z internetu z pliku tekstowego (wykorzystać moduł urllib.request) i wyświetlamy w programie wszystkie dane.
#Plik znajduje się w lokalizacji:      
#http://www.imsi.pl/imsi/api/download.php?file=user/u23/Programowanie%20skryptowe/CAL.TXT
import urllib.request
if __name__ =='__main__':
    req = urllib.request.Request('http://www.imsi.pl/imsi/api/download.php?file=user/u23/Programowanie%20skryptowe/CAL.TXT')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page)