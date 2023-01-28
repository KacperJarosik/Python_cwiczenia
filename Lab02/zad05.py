# 5. Sprawdź czy podana liczba jest liczbą pierwszą (funkcja) 
#    - wymyślamy swój algorytm niekoniecznie optymalny (2 jest liczbą pierwszą, <2 nie, >2 zależy od liczby)
def pierwsze (a):
    for i in range (2,a):
        if a%i == 0:
            return 'nie jest pierwsza'
    return 'jest pierwsza'
if __name__ == '__main__':
    a = int(input('Podaj liczbe = '))
    print(pierwsze(a))