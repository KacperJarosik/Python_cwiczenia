# zdanie dodatkowe dla chętnych - nieobowiązkowe
# ----------------------------------------------
# 9. Gramy w oczko dwoma kostkami (do 21) - my decydujemy ile razy rzucamy kostką. Po każdej partii:
# - liczymy ile zabrakło nam do 21 (sumujemy ilość gier) - liczymy średnią,
# - liczymy ile było było wartości 21 (sumujemy ilość gier),
# - liczymy o ile przekroczyliśmy wartość 21 (sumujemy ilość gier przegranych) - liczymy średnią
import random

gra_dalej = 'tak'
wybor = 'tak'
x_rowno = 0
suma_brak = 0
suma_nadwyzka = 0
ilosc_gier = 0
oczka_kostki = 0
aktualny_wynik = 0
ilosc_rzutow_kostka = 0
while gra_dalej == 'tak':
    ilosc_gier += 1
    while wybor == 'tak':
        ilosc_rzutow_kostka += 1
        oczka_kostki = random.randint(1, 6)
        aktualny_wynik += oczka_kostki
        print('Twoj ', ilosc_rzutow_kostka, '. lopierwszy rzut kostka to:', oczka_kostki, 'twoj aktualny wynik to: ',
              aktualny_wynik, '\n')
        wybor = (input('Czy rzucasz dalej? tak/nie\n'))
    ilosc_rzutow_kostka = 0
    if aktualny_wynik == 21:
        x_rowno += 1
    if aktualny_wynik > 21:
        suma_nadwyzka = aktualny_wynik - 21
    if aktualny_wynik < 21:
        suma_brak = 21 - aktualny_wynik
    gra_dalej = (input('Czy grasz dalej? tak/nie\n'))
    aktualny_wynik = 0
    wybor = 'tak'

print('Twoje statystyki to:\nIlosc zdobytych 21pkt: ', x_rowno, '\nIle srednio brakowało do 21pkt: ',
      suma_brak / ilosc_gier,
      '\nIle srednio bylo powyzej 21pkt: ', suma_nadwyzka / ilosc_gier)
