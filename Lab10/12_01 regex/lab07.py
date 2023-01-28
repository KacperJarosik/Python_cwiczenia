# Napisz wyrażenie regularne dla TABLIC REJESTRACYJNYCH
import re

if __name__ == '__main__':
    rejestracja = 'ERA 75TM'
    wynik = re.match('^[0-9A-Z]{2,3} [0-9A-Z]{4,5}$', rejestracja)
    wymagany_ciag_znakow = ['B', 'C', 'D', 'E', 'F', 'G', 'K', 'L', 'N', 'O', 'P', 'R', 'S', 'T', 'W', 'Z']
    print(wynik)
    if wynik:
        for i in wymagany_ciag_znakow:
            if i == rejestracja[0]:
                print('No')
            else:
                print('Ok')
                break
    else:
        print('No')
# nie spawdza powiatów i pojazdów słóżb specjalnych
