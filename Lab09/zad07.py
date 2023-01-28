# 7. Liczenie wartości funkcji podanej z klawiatury np. (x*x+2x+4 lub 1/(x+1))(wykorzystać funkcję eval())
# oraz zapisanie do pliku binarnego wartości x (od 0 do 50 o kroku 0.1) oraz y .
# Następnie wyświetlamy dane z pliku binarnego.
import pickle

if __name__ == "__main__":
    wynik = []
    tekst = open("wyniki_funkcja2.tct", "wb")
    for i in range(500):
        x = i * 0.1
        m = eval("x * x + 2 * x + 4")
        wynik.append(m)
    pickle.dump(wynik, tekst)
    tekst.close()
    tekst = open("wyniki_funkcja2.tct", "rb")
    data = pickle.load(tekst)
    for i in range(len(data)):
        print(data[i])
    tekst.close()