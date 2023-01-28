# 4. Wykorzystując moduł time i funkcję time obliczyć ile trwa pętla
#    składająca się z 100000 iteracji dla listy i dla typu tuple (np. sumowanie).
import time

if __name__ == '__main__':
    lista = list(range(10000000))
    mytuple = tuple(range(10000000))
    i = 0;
    t1 = time.time()
    for x in lista:
        i += 1
    t2 = time.time() - t1
    print(t2)

    for x in mytuple:
        i += 1
    t3 = time.time() - t1 - t2
    print(t3)
