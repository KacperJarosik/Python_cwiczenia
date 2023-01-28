# 7. Podajemy funkcję (na stałe w programie)
# np. liniową (y=x-1), kwadratową (y=3*x**2+7*x-19), hiberbolę(y=1/x+5)
# i sprawdzamy jej wartość w pkt. podanym z klawiatury 
# (nie obsługujemy błędów nawet jeśli będzie dzielenie przez zero)
if __name__ == '__main__':
    print('Twoja funkcja to: y=x-1. Podaj x dla którego chcesz sprawdzić wartość ')
    x = float(input())
    print('Dla twojego x funkcja przjmuje wartosc: ', x-1)
