# 6. Liczenie wartości funkcji podanej z klawiatury np. (x*x+2x+4 lub 1/(x+1)) (wykorzystać funkcję eval())
# oraz zapisanie do pliku wzoru oraz wartości x, y dla 500 elementów od 0 do 50 o kroku 0.1.
# Jeżeli będzie dzielenie przez zero to należy obsłużyć błąd i zamknąć plik.
if __name__ == "__main__":
    tekst = open("wyniki_funkcja", "w")
    tekst.write("x*x+2x+4")
    for i in range(500):
        x = i * 0.1
        m = eval("x * x + 2 * x + 4")
        tekst.write("\n" + str(m))
    tekst.close()
