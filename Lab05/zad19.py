# 19. Dana jest lista składająca się z liczb całkowitych:
# dane = [7, 3, 3, 9, 18, 6, 5, 24, 24, 4, 4, 5, 3, 7, 3, 24]
# Należy wyeliminować powtarzające się wartości w danej liście i posortować malejąco.
# (program ma działać dla dowolnej liczby składającej się z liczb całkowitych)
if __name__ == '__main__':
    dane = [7, 3, 3, 9, 18, 6, 5, 24, 24, 4, 4, 5, 3, 7, 3, 24]
    for i in dane[:]:
        if dane.count(i) > 1:
            for k in range(1, dane.count(i)):
                dane.remove(i)
    dane.sort(reverse=True)
    print(dane)
