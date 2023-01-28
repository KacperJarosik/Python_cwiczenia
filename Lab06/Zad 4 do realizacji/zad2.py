# 2. Napisać funkcję countChar(filename_in), która zlicza:
#   - liczbę znaków w pliku,
#   - liczbę białych znaków w pliku (białe znaki to spacja, tabulator, znacznik końca wiersza),
#   Wynikiem funkcji jest tablica złożona z 2 liczb całkowitych po jednej dla wymienionych podpunktów.
def countChar(filename_in):
    print(filename_in)
    for i in range(len(filename_in)):
        lista[0] += 1
        if filename_in[i] == ' ' or filename_in[i] == '\t' or filename_in[i] == '\n':
            lista[1] += 1
    print("Wszystkie znaki: ", lista[0], "\nBiale znaki: ", lista[1])
    return


if __name__ == "__main__":
    lista = [0, 0]
    y = """"""
    f = open("wyniki1.txt", 'r')
    for line in f.readlines():
        y += line
    countChar(y)
    f.close()
