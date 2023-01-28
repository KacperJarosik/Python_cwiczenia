# 2. Konwersja kilometry na mile i odwrotnie.
#    W programie wybieramy w pętli aż podamy poprawny wybór np.
#    'Podaj typ konwersji [km->mile]- 0, [mile->km]-1'.
#    Na tej podstawie wykonujemy funkcje wcześniej zdefiniowaną
#    km_mile(distance) lub mile_km(distance)
def km_mile(distace):
    return distace * 0.621371192
def mile_km(distance):
    return distance * 1.609344
print('Wybierz opcje\n0 - [km->mile]\n1 - [mile->km]')
x = int(input())
if x == 0:
    distance = float(input('podaj kilometry:\n'))
    print('mile: ')
    print(km_mile(distance))
if x == 1:
    distance = float(input('podaj mile:\n'))
    print('kilometry: ')
    print(mile_km(distance))
if x != 1 and x !=0:
    print('Poprawnie wybierz opcje')