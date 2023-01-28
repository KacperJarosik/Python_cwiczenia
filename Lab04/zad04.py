# 4. Obliczanie BMI jako funkcja bmi(height, mass) zwraca informację
#    w postaci liczby BMI, a następnie funkcję bmi_opis(height, mass),
#    która zwraca opis słowny, niedowaga, waga poprawna
#    itd. wykorzystując w swoim ciele funkcję bmi(height, mass)
def bmi(height, mass):
    BMI = mass / (height * height)
    if BMI < 16:
        x = 'wyglodzenie'
    if 16 <= BMI < 17:
        x = 'wychudzenie'
    if 17 <= BMI < 18.5:
        x = 'niedowaga'
    if 18.5 <= BMI < 25:
        x = 'waga prawidlowa'
    if 25 <= BMI < 30:
        x = 'nadwaga'
    if 30 <= BMI < 35:
        x = 'I stopien otylosci'
    if 35 <= BMI < 40:
        x = 'II stopien otylosci'
    if BMI >= 40:
        x = 'otylosc skrajna'
    return x


if __name__ == '__main__':
    height = float(input('Podaj wysokosc: '))
    mass = float(input('\nPodaj mase: '))
    print(bmi(height, mass))
